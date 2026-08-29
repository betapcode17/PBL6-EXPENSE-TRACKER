# class InvoiceClassifier:
#     def __init__(self, model_path: str = None):
#         self.model_path = model_path

#     def predict_category(self, seller: str, full_text: str) -> str:
#         text = (seller + " " + full_text).lower()
#         if any(k in text for k in ["coffee", "cafe", "trà sữa", "cơm", "phở", "nhà hàng", "bún"]):
#             return "Ăn uống (F&B)"
#         elif any(k in text for k in ["mart", "co.op", "vinmart", "bách hóa", "siêu thị"]):
#             return "Đi chợ / Siêu thị"
#         elif any(k in text for k in ["fashion", "clothing", "boutique", "giày", "quần áo"]):
#             return "Thời trang / Mua sắm"
#         elif any(k in text for k in ["xăng", "petrol", "dầu", "grab", "be"]):
#             return "Xăng dầu / Đi lại"
#         return "Khác"
