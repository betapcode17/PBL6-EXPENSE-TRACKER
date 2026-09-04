# src/segmentation/segmentor.py
import os
import cv2
import numpy as np
import tensorflow as tf

class ReceiptSegmentor:
    def __init__(self, model_path: str = "models/1_segmentation/receipt_unet_mobilenetv2.keras", img_size=(256, 256)):
        self.img_size = img_size
        self.model = None
        
        if model_path and os.path.exists(model_path):
            print(f"Dang tai Segmentation Model tu: {model_path}")
            self.model = tf.keras.models.load_model(model_path, compile=False)
            print("Tai Segmentation Model thanh cong!")
        else:
            print(f"Canh bao: Khong tim thay model tai {model_path}. Se tra ve anh goc khi xu ly.")

    def _order_points(self, pts: np.ndarray) -> np.ndarray:
        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]
        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]
        return rect

    def _four_point_transform(self, image: np.ndarray, pts: np.ndarray) -> np.ndarray:
        rect = self._order_points(pts)
        (tl, tr, br, bl) = rect
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))

        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))

        if maxWidth <= 0 or maxHeight <= 0:
            return image

        dst = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]
        ], dtype="float32")

        M = cv2.getPerspectiveTransform(rect, dst)
        return cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    def _clean_mask(self, raw_mask: np.ndarray):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        mask_clean = cv2.morphologyEx(raw_mask, cv2.MORPH_OPEN, kernel, iterations=2)
        mask_clean = cv2.morphologyEx(mask_clean, cv2.MORPH_CLOSE, kernel, iterations=2)

        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(mask_clean)
        if num_labels > 1:
            largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
            refined_mask = np.zeros_like(mask_clean)
            refined_mask[labels == largest_label] = 255
        else:
            refined_mask = mask_clean

        contours, _ = cv2.findContours(refined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            c = max(contours, key=cv2.contourArea)
            hull = cv2.convexHull(c)
            return hull
        return None

    def crop_and_dewarp(self, image_input) -> np.ndarray:
        """
        Nhận ảnh đầu vào (str path hoặc numpy ndarray)
        Trả về ảnh numpy ndarray đã nắn thẳng (Perspective Warp)
        """
        if isinstance(image_input, str):
            image = cv2.imread(image_input)
        else:
            image = image_input

        if image is None:
            raise ValueError("Khong the doc anh dau vao.")

        if self.model is None:
            return image

        h_orig, w_orig = image.shape[:2]

        # 1. Tiền xử lý đưa vào model
        img_resized = cv2.resize(image, self.img_size)
        img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        img_tensor = tf.cast(img_rgb, tf.float32) / 255.0

        # 2. Predict mask
        pred = self.model.predict(tf.expand_dims(img_tensor, 0), verbose=0)
        raw_mask = ((pred[0, :, :, 0] > 0.5) * 255).astype(np.uint8)
        raw_mask_full = cv2.resize(raw_mask, (w_orig, h_orig), interpolation=cv2.INTER_NEAREST)

        # 3. Lọc nhiễu & tìm 4 góc
        hull = self._clean_mask(raw_mask_full)
        if hull is not None:
            peri = cv2.arcLength(hull, True)
            approx = cv2.approxPolyDP(hull, 0.02 * peri, True)
            if len(approx) == 4:
                pts = approx.reshape(4, 2).astype("float32")
                return self._four_point_transform(image, pts)
            else:
                rect = cv2.minAreaRect(hull)
                box = cv2.boxPoints(rect)
                return self._four_point_transform(image, box.astype("float32"))

        return image