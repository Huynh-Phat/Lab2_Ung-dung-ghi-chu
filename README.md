# App Ghi Chú - Lab 2 Tư Duy Tính Toán

## Mô tả
Ứng dụng ghi chú cá nhân đơn giản, sử dụng FastAPI (Backend) và Streamlit (Frontend). Tích hợp đăng nhập bằng Firebase Authentication và lưu trữ bằng SQLite.

## Hướng dẫn cài đặt
1. Clone repository này về máy.
2. Cài đặt các thư viện yêu cầu: `pip install -r requirements.txt`
3. Thêm Web API Key của Firebase vào biến `FIREBASE_API_KEY` trong file `frontend/app.py`.

## Hướng dẫn chạy
**Bước 1: Chạy Backend**
Mở terminal và gõ:
`uvicorn backend.main:app --reload`
Backend sẽ chạy ở `http://127.0.0.1:8000`

**Bước 2: Chạy Frontend**
Mở một terminal MỚI (giữ terminal backend chạy ngầm) và gõ:
`streamlit run frontend/app.py`
Frontend sẽ tự mở trên trình duyệt.

## Link Video Demo
https://drive.google.com/file/d/1a7yLNnavPvfEMpHK8ZsIR8f2-w2tcqvM/view?usp=sharing
