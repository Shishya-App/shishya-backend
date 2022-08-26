# import logging
# import sys
# import numpy as np
# import pandas as pd
# import mlops.ml_verify as mas
# for name in logging.Logger.manager.loggerDict.keys():
#     logging.getLogger(name).setLevel(logging.CRITICAL)

# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# from tkinter.tix import IMAGE
from ocr import ankocr


# image= 'subject2.jpeg'
# if(mas.check.check_similarity(image,'adhatest3.jpg')>0.70):
#     #   print("similar")
#     t=ankocr.get_text(image)
#     # print(t)
#     if('GOVERNMENT OF INDIA' in t):
#         print("all test passed")
#     else:
#         print('text not found')
# else:
#     t=ankocr.get_text(image)
#     # print(t)
#     if('GOVERNMENT OF INDIA' in t):
#         print('similarity test fail but text found')
#     else:
#         print('all test fail')


from test import tester



# print(tester.check_jee_allot('ALLOTMENT LETTER.pdf'))
# print(tester.check_jee_allot('200310484280_AdmitCard.pdf'))
# ankocr.delete('save.png')
# print(tester.check('testadha2.jpg'))
# print(tester.check_pan('riya_pan.jpeg'))
