import logging
import sys
import numpy as np
import pandas as pd
import mlops.ml_verify as mas
for name in logging.Logger.manager.loggerDict.keys():
    logging.getLogger(name).setLevel(logging.CRITICAL)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from ocr import ankocr

class tester:
    def check_adhar(file):
        image = ankocr.api_p2i(file)
        bar=mas.check.check_similarity(image,'adhatest3.jpg')
        t=ankocr.get_text(image)
        ankocr.delete('save.png')
        if(bar>0.40):
    #   print("similar")
        
            
    # print(t)
            if('GOVERNMENT OF INDIA' in t):
                return True
            else:
                return  False
        else:
            
    # print(t)
            if('GOVERNMENT OF INDIA' in t):
                return True
            else:
                return  False
        
    # test jee_admit card 
    def check_jee_allot(file):
        image = ankocr.api_p2i(file)
        bar=mas.check.check_similarity(image,'jee allot.jpg')
        t=ankocr.get_text(image)
        ankocr.delete('save.png')
        if(bar>0.40):
    #   print("similar")
            
    # print(t)
            if(('Provisional Admission Letter' in t) or ('Partial Admission Fee' in t)):
                return True
            else:
                return False
        else:
            
    # print(t)
            if(('Provisional Admission Letter' in t) or ('Partial Admission Fee' in t) ): # error
                return True
            else:
                return False
        
        
    def check_pan(file):
        image = ankocr.api_p2i(file)
        bar=mas.check.check_similarity(image,'test.jpeg')
        t=ankocr.get_text(image)
        ankocr.delete('save.png')
        if(bar>0.40):
    #   print("similar")
            
    # print(t)
            if(('INCOME TAX DEPARTMENT' in t) or ('Permanent Account Number Card' in t)):
                return True
            else:
                return  False
        else:
            
    # print(t)
            if(('INCOME TAX DEPARTMENT' in t) or ('Permanent Account Number Card' in t)):
                return True
            else:
                return  False
        
        
    # def pdf_to_image(pdf_file):
    #     from pdf2image import convert_from_path
    #     pages = convert_from_path(pdf_file, 500)
    #     for page in pages:
    #         page.save('out.jpg', 'JPEG')
        
    #     return 'out.jpg'
        
    # def delete__image(image):
    #     os.remove(image)
    #     return True  
        
    # def pdf_to_analysis(file):
    #     ifile= tester.pdf_to_image(file)
    #     pass
    
    # # PDF TO IMAGE WITHOUT PLOPPER 
    # def pdf_to_image_without_ploper(pdf_file):
    #     # pdf to image without ploper
    #     pass