# tts_using_gemini
Bạn có thể dùng một README kiểu nhẹ nhàng, sạch sẽ như này:

---

# 🎙️ Gemini TTS Studio

Một ứng dụng nhỏ dùng Google Gemini TTS API để chuyển văn bản thành giọng nói tự nhiên, kết hợp với Gradio để tạo giao diện web đơn giản và dễ sử dụng.

Ứng dụng cho phép:

* Nhập văn bản trực tiếp
* Chọn nhiều giọng đọc khác nhau
* Tạo và nghe lại file âm thanh ngay trên giao diện
* Xuất âm thanh dưới định dạng WAV

## ✨ Tính năng

* Text-to-Speech realtime từ Gemini
* Nhiều voice preset có sẵn
* Xử lý audio thô và đóng gói thành WAV chuẩn
* Giao diện đơn giản, chạy local nhanh

## 🛠 Công nghệ sử dụng

* Python
* Gradio
* Google GenAI SDK
* dotenv

## 🚀 Cài đặt

Cài dependencies:

```bash
pip install gradio google-genai python-dotenv
```

Tạo file `.env`:

```env
GOOGLE_API_KEY=your_api_key_here
```

Chạy project:

```bash
python app.py
```

## 📌 Demo

1. Nhập nội dung cần đọc
2. Chọn giọng nói
3. Nhấn **Generate**
4. Nghe kết quả ngay trên trình duyệt

## Mục tiêu project

Project này được tạo để thử nghiệm khả năng Text-to-Speech của Gemini, đồng thời làm một giao diện demo đơn giản phục vụ học tập và nghiên cứu.

---

Nếu đăng lên GitHub thì kiểu README này khá gọn, nhìn cá nhân nhưng vẫn chuyên nghiệp.

