import os
import wave
import gradio as gr
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Khởi tạo môi trường
load_dotenv()
client = genai.Client()
MODEL_ID = "gemini-3.1-flash-tts-preview"

# 2. Hàm xử lý logic Backend
def generate_tts(text, voice_name):
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=voice_name 
                        )
                    )
                )
            )
        )

        audio_data = None
        mime_type = None

        for part in response.candidates[0].content.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                mime_type = part.inline_data.mime_type
                break

        # Xử lý đóng gói chuẩn WAV khi nhận được dữ liệu l16 thô
        if audio_data and "l16" in str(mime_type):
            output_file = "gradio_output.wav"
            
            with wave.open(output_file, "wb") as f:
                f.setnchannels(1)      
                f.setsampwidth(2)      
                f.setframerate(24000)  
                f.writeframes(audio_data)
            
            # Trả về đường dẫn file âm thanh và thông báo thành công
            return output_file, f"✅ Thành công! Dữ liệu gốc: {mime_type}"
        else:
            return None, "❌ Lỗi: AI không trả về định dạng âm thanh thô hợp lệ."

    except Exception as e:
        return None, f"❌ Lỗi hệ thống: {str(e)}"

# 3. Dựng giao diện người dùng (Frontend bằng Gradio)
with gr.Blocks(title="Gemini TTS Studio", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎙️ Trình Tạo Giọng Nói AI")
    gr.Markdown("Hệ thống chuyển đổi văn bản thành giọng nói giao tiếp trực tiếp với mô hình Gemini Core.")
    
    with gr.Row():
        with gr.Column(scale=2):
            # Ô nhập liệu
            text_input = gr.Textbox(
                label="Nội dung cần đọc", 
                lines=4, 
                value="こんにちは！今日のプログラミングの勉強はどうですか？" 
            )
            
            # Menu thả xuống để chọn giọng
            voice_dropdown = gr.Dropdown(
                choices=['Puck', 'Aoede', 'Charon', 'Kore', 'Fenrir'],
                value='Puck',
                label="Chọn diễn viên lồng tiếng"
            )
            
            # Nút thực thi
            generate_btn = gr.Button("🚀 Bắt đầu tạo âm thanh", variant="primary")
        
        with gr.Column(scale=1):
            # Trình phát âm thanh
            audio_output = gr.Audio(label="Kết quả phát âm", type="filepath")
            # Ô log trạng thái
            status_output = gr.Textbox(label="Trạng thái Backend", interactive=False)

    # Gắn sự kiện click nút bấm vào hàm Backend
    generate_btn.click(
        fn=generate_tts,
        inputs=[text_input, voice_dropdown],
        outputs=[audio_output, status_output]
    )

# 4. Kích hoạt Server
if __name__ == "__main__":
    print("Đang khởi động Server UI...")
    demo.launch()
