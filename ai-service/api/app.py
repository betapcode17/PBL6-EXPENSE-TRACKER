# import os
# import shutil
# import tempfile
# from fastapi import FastAPI, UploadFile, File, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from api.schemas import ReceiptResponseSchema, HealthCheckSchema
# from pipeline.receipt_pipeline import ReceiptAIPipeline

# app = FastAPI(
#     title="Receipt OCR & KIE AI Service",
#     description="API nhận diện hóa đơn, trích xuất thực thể KIE và phân loại danh mục chi tiêu",
#     version="1.0.0"
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Khởi tạo Pipeline singleton
# pipeline = None

# @app.on_event("startup")
# def load_pipeline():
#     global pipeline
#     config_paths = {
#         "segmentation": "weights/segmentation_unet.pth",
#         "orientation": "weights/orientation_mobilenetv3.pth",
#         "detector": "weights/paddleocr_dbnet/",
#         "recognizer": "weights/vietocr_transformer.pth",
#         "layoutlmv3": "weights/layoutlmv3_kie/",
#         "classifier": "weights/phobert_classifier.pth"
#     }
#     pipeline = ReceiptAIPipeline(config_paths=config_paths)
#     print("AI Pipeline loaded successfully.")

# @app.get("/health", response_model=HealthCheckSchema)
# def health_check():
#     return HealthCheckSchema()

# @app.post("/api/v1/scan-receipt", response_model=ReceiptResponseSchema)
# async def scan_receipt(file: UploadFile = File(...)):
#     if not file.content_type.startswith("image/"):
#         raise HTTPException(status_code=400, detail="File tải lên phải là định dạng hình ảnh (.jpg, .png, .jpeg)")
    
#     with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp:
#         shutil.copyfileobj(file.file, tmp)
#         tmp_path = tmp.name

#     try:
#         result = pipeline.process(tmp_path)
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Lỗi trong quá trình xử lý AI: {str(e)}")
#     finally:
#         if os.path.exists(tmp_path):
#             os.remove(tmp_path)
