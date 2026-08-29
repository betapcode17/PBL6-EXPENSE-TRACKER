# from src.segmentation.segmentor import ReceiptSegmentor
# from src.text_detector.detector import TextDetector
# from src.orientation.deskew_utils import deskew_by_long_boxes
# from src.orientation.orientation_corrector import OrientationCorrector

# class DataPreparationPipeline:
#     def __init__(self, config_paths):
#         self.segmentor = ReceiptSegmentor(config_paths.get("segmentation"))
#         self.detector = TextDetector(config_paths.get("detector"))
#         self.orient_corrector = OrientationCorrector(config_paths.get("orientation"))

#     def run(self, raw_image):
#         warped_img = self.segmentor.crop_and_dewarp(raw_image)
#         raw_boxes = self.detector.detect_boxes(warped_img)
#         horizontal_img, skew_angle = deskew_by_long_boxes(warped_img, raw_boxes)
#         aligned_img, is_flipped = self.orient_corrector.check_and_flip_180(horizontal_img)
#         final_boxes = self.detector.detect_boxes(aligned_img)
#         return aligned_img, final_boxes, skew_angle, is_flipped
