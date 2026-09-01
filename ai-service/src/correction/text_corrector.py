# import re

# class TextCorrector:
#     def clean_and_format(self, kie_data: dict) -> dict:
#         cleaned = {}
#         cleaned["seller"] = str(kie_data.get("seller", "")).strip()
#         cleaned["address"] = str(kie_data.get("address", "")).strip()

#         # Chuẩn hóa số tiền
#         raw_cost = str(kie_data.get("total_cost", ""))
#         digits_only = re.sub(r"[^\d]", "", raw_cost)
#         cleaned["total_cost"] = int(digits_only) if digits_only else None

#         # Chuẩn hóa ngày giờ
#         raw_time = str(kie_data.get("timestamp", ""))
#         cleaned["timestamp"] = raw_time.strip()
#         return cleaned
