# from pipeline.data_preparation_pipeline import DataPreparationPipeline
# from pipeline.information_extraction_pipeline import InformationExtractionPipeline

# class ReceiptAIPipeline:
#     def __init__(self, config_paths: dict):
#         self.prep_stage = DataPreparationPipeline(config_paths)
#         self.extract_stage = InformationExtractionPipeline(config_paths)

#     def process(self, raw_image_path: str) -> dict:
#         aligned_img, final_boxes, skew_angle, is_flipped = self.prep_stage.run(raw_image_path)
#         clean_entities, category, total_lines = self.extract_stage.run(aligned_img, final_boxes)

#         return {
#             "status": "success",
#             "invoice_category": category,
#             "extracted_data": clean_entities,
#             "metadata": {
#                 "skew_angle": round(skew_angle, 2),
#                 "is_flipped_180": is_flipped,
#                 "total_lines_detected": total_lines
#             }
#         }
