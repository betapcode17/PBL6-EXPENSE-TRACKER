# import cv2
# import numpy as np

# def deskew_by_long_boxes(image: np.ndarray, text_boxes: list, min_aspect_ratio: float = 2.5):
#     valid_angles = []
#     for box in text_boxes:
#         pts = np.array(box, dtype=np.float32)
#         rect = cv2.minAreaRect(pts)
#         (center), (width, height), angle = rect
#         if width < height:
#             width, height = height, width
#             angle += 90.0
#         aspect_ratio = width / (height + 1e-5)
#         if aspect_ratio >= min_aspect_ratio:
#             if angle > 45:
#                 angle -= 90
#             elif angle < -45:
#                 angle += 90
#             valid_angles.append(angle)

#     if len(valid_angles) == 0:
#         return image, 0.0

#     skew_angle = float(np.median(valid_angles))
#     (h, w) = image.shape[:2]
#     M = cv2.getRotationMatrix2D((w // 2, h // 2), skew_angle, 1.0)
#     straight_image = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
#     return straight_image, skew_angle
