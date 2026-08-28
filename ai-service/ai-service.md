# AI Module Documentation - MC_OCR 2021 Dataset & Pipeline

## 1. Cấu trúc Dataset (MC_OCR 2021)

| Thư mục | Định dạng | Số lượng | Nội dung & Mục đích |
| :--- | :--- | :--- | :--- |
| `preprocessor/` | `.jpg`, `.txt` | 1.155 ảnh + txt | Tọa độ 4 góc hóa đơn -> Train Corner Detection / Bỏ background |
| `data0.7/` | `.jpg` | 1.044 ảnh | Ảnh hóa đơn chuẩn đã lọc sạch (Confidence >= 0.7) |
| `data0_or_180/` | `.jpg` | 35.987 ảnh | Ảnh crop từng dòng chữ -> Train phân loại xoay 0° vs 180° |
| `rotation_corrector/` | `.jpg`, `.txt` | 1.155 bộ | Ảnh + tọa độ 4 góc từng box chữ sau khi nắn xoay |
| `rotation_corrector_kie/`| `.jpg`, `.txt` | 1.155 bộ | Tọa độ 8 điểm gán nhãn KIE |
| `text_detector/` & `dataset/` | `.jpg`, `.txt` | 1.155 bộ | Nhãn Ground Truth đa giác -> Train DBNet / CRAFT |
| `text_recognition_mcocr_data/` | `.jpg` | 6.585 ảnh | Ảnh crop dòng chữ tiếng Việt -> Đầu vào VietOCR |
| `kie_data/` | `.tsv`, `.jpg` | 1.155 tsv + ảnh | Dữ liệu đa phương thức (Ảnh + Box + Text + Nhãn KIE) |
| `train_images/` | `.jpg` | 1.155 ảnh | Ảnh hóa đơn gốc tập Train |
| `val_images/` | `.jpg` | 391 ảnh | Ảnh hóa đơn gốc tập Validation |

---

## 2. Pipeline Xử lý AI (7 Bước)

### Bước 1: Receipt Segmentation (Cắt bỏ Background)
* **Mục đích:** Loại bỏ mặt bàn, viền thừa, bóng đổ để tránh nhiễu OCR.
* **Mô hình:** `U-Net (Backbone MobileNetV2)` hoặc `YOLOv8-seg`.
* **Dataset:** `preprocessor/`.
* **Output:** Ảnh hóa đơn đã được crop sát 4 góc.

### Bước 2: Text Detection & Deskew (Phát hiện chữ & Nắn thẳng)
* **Mục đích:** Xác định Bounding Box của từng dòng chữ và nắn thẳng góc nghiêng ngang.
* **Mô hình:** `PaddleOCR (DBNet)`.
* **Thuật toán Deskew:** Lọc box dài (Aspect Ratio >= 2.5) -> Tính `cv2.minAreaRect()` -> Xoay theo góc trung vị (Median Angle).
* **Dataset:** `text_detector/`.

### Bước 3: Receipt Classification (Phân loại xoay 0° vs 180°)
* **Mục đích:** Kiểm tra và đảo chiều hóa đơn nếu bị lộn ngược 180°.
* **Mô hình:** `MobileNetV3-Small` (Binary Classification, độ trễ < 5ms).
* **Dataset:** `data0_or_180/`, `data0.7/`.
* **Output:** Hóa đơn đúng chiều đọc (0°).

### Bước 4: Image Alignment
* **Mục đích:** Đồng bộ lại toàn bộ hệ tọa độ Bounding Box sau khi nắn góc và xoay 180°.

### Bước 5: Text Recognition (Nhận diện chữ tiếng Việt)
* **Mục đích:** Chuyển ảnh dòng chữ thành chuỗi text tiếng Việt có dấu.
* **Mô hình:** `VietOCR` (`vgg_transformer` / `resnet_transformer`).
* **Dataset:** `text_recognition_mcocr_data/`.
* **Output:** Chuỗi ký tự UTF-8 chính xác dấu thanh và số.

### Bước 6: Key Information Extraction - KIE (Trích xuất thực thể)
* **Mục đích:** Gán nhãn cho 4 trường: `SELLER`, `ADDRESS`, `TIMESTAMP`, `TOTAL_COST`.
* **Mô hình:** `LayoutLMv3` (Multimodal: Visual + Spatial 2D Box + Text Token).
* **Dataset:** `kie_data/`.

### Bước 7: Text Correction & Formatting (Hậu xử lý)
* **Mục đích:** Sửa lỗi chính tả OCR và ép kiểu dữ liệu.
* **Phương pháp:** Regex + Rule-based.
  * **TOTAL_COST:** Loại bỏ ký tự thừa, sửa `O->0`, `l->1`, xóa dấu phân cách -> Ép kiểu `Integer`.
  * **TIMESTAMP:** Nhận diện định dạng ngày giờ -> Chuẩn hóa về ISO-8601 (`YYYY-MM-DD HH:MM:SS`).