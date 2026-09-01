# import cv2
# from PIL import Image

# class TextRecognizer:
#     def __init__(self, model_path: str = None):
#         self.model_path = model_path

#     def recognize_boxes(self, image, boxes: list) -> list:
#         # Trong thực tế crop từng box và đưa qua VietOCR Predictor
#         results = []
#         dummy_texts = ["THE COFFEE HOUSE", "403 Phan Huy Ích, P.14, Q.Gò Vấp", "Tổng cộng", "38.000"]
#         for idx, box in enumerate(boxes):
#             text = dummy_texts[idx % len(dummy_texts)]
#             pts = [box[0][0], box[0][1], box[2][0], box[2][1]] # [xmin, ymin, xmax, ymax]
#             results.append({
#                 "box": pts,
#                 "text": text
#             })
#         return results
