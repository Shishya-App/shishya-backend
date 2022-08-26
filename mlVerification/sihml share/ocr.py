# ocr module from easy ocr library

'''    

How to use code 
#from ocr import ankocr
#t=ankocr.get_text('test.jpeg')


t is the list of text detected in the document image 
'''


# +from nis import cat
import convertapi
import requests
from PyPDF2 import PdfReader
import easyocr as eocr
import cv2
import numpy as np
import os
import sys
import pickle as pkl
import PyPDF2
import pdfplumber
from pdf2image import convert_from_path
class ankocr:
    
    def __init__(self):
        print("kr raha hu ruk ja..")
        
    def get_text(image):
        reader = eocr.Reader(['en'])
        text = reader.readtext(image,detail=0)
        return text
        
    def get_adharid(image):
        t = ankocr.get_text(image)
        try:
           return t[t.index('MALE')+1]
        except:
           return [t.index('FEMALE')+1]
    def get_adharname(image):
        t=ankocr.get_text(image)
        try:
            return t[t.index('Government of India')+2]   
        except:
            return t[t.index('GOVERNMENT OF INDIA')+2] 
    #  pan 
    def get_panid(image):
        t=ankocr.get_text(image)
        try:
            return t[t.index('Permanent Account Number Card')+1]
        except:
            prompt= "not found or wrong data! manual action required"
            return prompt
    
    def get_panname(image):
        t=ankocr.get_text(image)
        try:
            return t[t.index('NAME')+1]
        except:
            prompt= "not found or wrong data! manual action required"
            return prompt
     
    # pdf extract
    
    
  
        
 
            
    # jee allotment 
    def get_appno(image):
        t=ankocr.get_text(image)
        # print(t)
        try:
            return t[t.index('Application Number:')+1]
        except:
            prompt= "not found or wrong data! manual action required"
            return prompt
    # 12th marks 
    def get_12_roll(image):
        t=ankocr.get_text(image)
        # print(t)
        try:
            return t[t.index('12th Roll Number:')+1]
        except:
            prompt= "not found or wrong data! manual action required"
            return prompt
        
    
        
        
        
# print(ankocr.pdf_to_text('allotletter.pdf'))  
    #  pdf to image by api 
    def api_p2i(file):
        
        convertapi.api_secret = 'cGujnI0KQ05odKHs'
        convertapi.convert('png', {
            'File': 'allotletter.pdf'
        }, from_format = 'pdf').save_files('save.png')
        
        return 'save.png'

    # delete image file
    def delete(file):
        os.remove(file)
        return True

# ankocr.delete('save.png')