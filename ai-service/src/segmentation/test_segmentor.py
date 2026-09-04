import cv2
from src.segmentation.segmentor import ReceiptSegmentor

segmentor = ReceiptSegmentor(model_path="models/1_segmentation/receipt_unet_mobilenetv2.keras")

# Dua 1 anh bat ky vao test
warped = segmentor.crop_and_dewarp("data/1_segmentation/imgs/test_image.jpg")

cv2.imwrite("test_output_warped.jpg", warped)
print("Da nan thang va luu tai test_output_warped.jpg")
