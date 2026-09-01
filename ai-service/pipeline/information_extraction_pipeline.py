# from src.text_recognition.recognizer import TextRecognizer
# from src.kie.extractor import LayoutLMv3Extractor
# from src.correction.text_corrector import TextCorrector
# from src.classification.classifier import InvoiceClassifier

# class InformationExtractionPipeline:
#     def __init__(self, config_paths):
#         self.recognizer = TextRecognizer(config_paths.get("recognizer"))
#         self.kie_extractor = LayoutLMv3Extractor(config_paths.get("layoutlmv3"))
#         self.corrector = TextCorrector()
#         self.classifier = InvoiceClassifier(config_paths.get("classifier"))

#     def run(self, aligned_img, final_boxes):
#         ocr_results = self.recognizer.recognize_boxes(aligned_img, final_boxes)
#         kie_entities = self.kie_extractor.extract(aligned_img, ocr_results)
#         clean_entities = self.corrector.clean_and_format(kie_entities)
#         full_text = " ".join([item['text'] for item in ocr_results])
#         category = self.classifier.predict_category(seller=clean_entities.get("seller", ""), full_text=full_text)
#         return clean_entities, category, len(ocr_results)
