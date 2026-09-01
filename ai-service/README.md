# AI Service - Vietnamese Receipt OCR & Key Information Extraction (KIE)

AI Service phục vụ đề tài nhận diện hóa đơn, bóc tách 4 trường thực thể (`SELLER`, `ADDRESS`, `TIMESTAMP`, `TOTAL_COST`) và phân loại danh mục chi tiêu tự động.

## 🚀 Cài đặt & Chạy ứng dụng

### 1. Cài đặt môi trường
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Chạy API Server (FastAPI)
```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload
```
Truy cập Swagger UI tài liệu API: `http://localhost:8000/docs`

### 3. Chạy bằng Docker
```bash
docker build -t receipt-ai-service .
docker run -p 8000:8000 receipt-ai-service
```
