# import unittest
# import numpy as np
# import tempfile
# import cv2
# import os
# from pipeline.receipt_pipeline import ReceiptAIPipeline

# class TestPipeline(unittest.TestCase):
#     def test_pipeline_runs(self):
#         pipeline = ReceiptAIPipeline({})
#         dummy_img = np.zeros((200, 200, 3), dtype=np.uint8)
#         with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
#             cv2.imwrite(f.name, dummy_img)
#             tmp_name = f.name
#         try:
#             res = pipeline.process(tmp_name)
#             self.assertEqual(res["status"], "success")
#         finally:
#             if os.path.exists(tmp_name):
#                 os.remove(tmp_name)

# if __name__ == "__main__":
#     unittest.main()
