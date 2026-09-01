# import cv2
# import numpy as np

# class ReceiptSegmentor:
#     def __init__(self, model_path: str = None):
#         self.model_path = model_path

#     def crop_and_dewarp(self, image_input) -> np.ndarray:
#         if isinstance(image_input, str):
#             image = cv2.imread(image_input)
#         else:
#             image = image_input

#         if image is None:
#             raise ValueError("Không thể đọc ảnh đầu vào.")

#         orig = image.copy()
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#         edged = cv2.Canny(blurred, 75, 200)

#         contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#         contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

#         screen_cnt = None
#         for c in contours:
#             peri = cv2.arcLength(c, True)
#             approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#             if len(approx) == 4:
#                 screen_cnt = approx
#                 break

#         if screen_cnt is None:
#             return orig

#         pts = screen_cnt.reshape(4, 2)
#         rect = self._order_points(pts)
#         (tl, tr, br, bl) = rect

#         widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
#         widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
#         maxWidth = max(int(widthA), int(widthB))

#         heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
#         heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
#         maxHeight = max(int(heightA), int(heightB))

#         dst = np.array([
#             [0, 0],
#             [maxWidth - 1, 0],
#             [maxWidth - 1, maxHeight - 1],
#             [0, maxHeight - 1]
#         ], dtype="float32")

#         M = cv2.getPerspectiveTransform(rect, dst)
#         warped = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))
#         return warped

#     def _order_points(self, pts):
#         rect = np.zeros((4, 2), dtype="float32")
#         s = pts.sum(axis=1)
#         rect[0] = pts[np.argmin(s)]
#         rect[2] = pts[np.argmax(s)]
#         diff = np.diff(pts, axis=1)
#         rect[1] = pts[np.argmin(diff)]
#         rect[3] = pts[np.argmax(diff)]
#         return rect
