# import unittest
# import numpy as np
# from src.text_recognition.recognizer import TextRecognizer

# class TestOCR(unittest.TestCase):
#     def test_recognizer_runs(self):
#         dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
#         rec = TextRecognizer()
#         res = rec.recognize_boxes(dummy_img, [[[0, 0], [50, 0], [50, 20], [0, 20]]])
#         self.assertTrue(len(res) > 0)

# if __name__ == "__main__":
#     unittest.main()
