# from pydantic import BaseModel, Field
# from typing import Optional, Dict, Any, List

# class ExtractedDataSchema(BaseModel):
#     seller: Optional[str] = Field(default=None, description="Tên cửa hàng / người bán")
#     address: Optional[str] = Field(default=None, description="Địa chỉ cửa hàng")
#     timestamp: Optional[str] = Field(default=None, description="Thời gian xuất hóa đơn (ISO-8601)")
#     total_cost: Optional[int] = Field(default=None, description="Tổng số tiền thanh toán (VNĐ)")

# class MetadataSchema(BaseModel):
#     skew_angle: Optional[float] = Field(default=0.0, description="Góc xoay nắn thẳng (độ)")
#     is_flipped_180: Optional[bool] = Field(default=False, description="Hóa đơn có bị lật ngược không")
#     total_lines_detected: Optional[int] = Field(default=0, description="Số dòng chữ phát hiện được")

# class ReceiptResponseSchema(BaseModel):
#     status: str = Field(default="success", description="Trạng thái xử lý")
#     invoice_category: str = Field(default="Khác", description="Danh mục hóa đơn")
#     extracted_data: ExtractedDataSchema
#     metadata: MetadataSchema

# class HealthCheckSchema(BaseModel):
#     status: str = "ok"
#     version: str = "1.0.0"
