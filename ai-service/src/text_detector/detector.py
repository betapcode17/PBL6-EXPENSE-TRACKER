# import cv2
# import numpy as np

# class TextDetector:
#     def __init__(self, model_dir: str = None):
#         self.model_dir = model_dir

#     def detect_boxes(self, image: np.ndarray) -> list:
#         # Giả lập trả về danh sách box [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
#         # Trong thực tế gọi PaddleOCR(use_gpu=True).ocr(image, rec=False)
#         h, w = image.shape[:2]
#         return [
#             [[int(w*0.1), int(h*0.05)], [int(w*0.8), int(h*0.05)], [int(w*0.8), int(h*0.10)], [int(w*0.1), int(h*0.10)]],
#             [[int(w*0.1), int(h*0.12)], [int(w*0.9), int(h*0.12)], [int(w*0.9), int(h*0.17)], [int(w*0.1), int(h*0.17)]],
#             [[int(w*0.1), int(h*0.80)], [int(w*0.4), int(h*0.80)], [int(w*0.4), int(h*0.85)], [int(w*0.1), int(h*0.85)]],
#             [[int(w*0.6), int(h*0.80)], [int(w*0.9), int(h*0.80)], [int(w*0.9), int(h*0.85)], [int(w*0.6), int(h*0.85)]]
#         ]
