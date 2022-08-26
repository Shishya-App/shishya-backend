import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt 
import base64
from PIL import Image
import io
import math 
from math import sqrt




global embed
embed = hub.KerasLayer(os.getcwd())


class TensorVector(object):

    def __init__(self, FileName=None):
        self.FileName = FileName

    def process(self):

        img = tf.io.read_file(self.FileName)
        img = tf.io.decode_jpeg(img, channels=3)
        img = tf.image.resize_with_pad(img, 224, 224)
        img = tf.image.convert_image_dtype(img,tf.float32)[tf.newaxis, ...]
        features = embed(img)
        feature_set = np.squeeze(features)
        return list(feature_set)

class check:    
    def convertBase64(FileName):
        """
        Return the Numpy array for a image 
        """
        with open(FileName, "rb") as f:
            data = f.read()
            
        res = base64.b64encode(data)
        
        base64data = res.decode("UTF-8")
        
        imgdata = base64.b64decode(base64data)
        
        image = Image.open(io.BytesIO(imgdata))
        
        return np.array(image)

    def cosineSim(a1,a2):
        sum = 0
        suma1 = 0
        sumb1 = 0
        for i,j in zip(a1, a2):
            suma1 += i * i
            sumb1 += j*j
            sum += i*j
        cosine_sim = sum / ((sqrt(suma1))*(sqrt(sumb1)))
        return cosine_sim


    def jaccard_similarity(list1, list2):
        intersection = len(list(set(list1).intersection(list2)))
        union = (len(list1) + len(list2)) - intersection
        return float(intersection) / union

    def average(x):
        assert len(x) > 0
        return float(sum(x)) / len(x)
    
    def pearson_def(x, y):
        assert len(x) == len(y)
        n = len(x)
        assert n > 0
        avg_x = check.average(x)
        avg_y = check.average(y)
        diffprod = 0
        xdiff2 = 0
        ydiff2 = 0
        for idx in range(n):
            xdiff = x[idx] - avg_x
            ydiff = y[idx] - avg_y
            diffprod += xdiff * ydiff
            xdiff2 += xdiff * xdiff
            ydiff2 += ydiff * ydiff

        return diffprod / math.sqrt(xdiff2 * ydiff2)




    def check_similarity(img1, img2):
        # img1 = convertBase64(img1)
        # img2 = convertBase64(img2)
        helper1=TensorVector(img1)
        helper2=TensorVector(img2)
        vector = helper1.process()
        vector2 = helper2.process()
        
        similarity = (check.jaccard_similarity(vector, vector2) + check.cosineSim(vector, vector2) + check.pearson_def(vector, vector2)) / 3
        # print(check.jaccard_similarity(vector, vector2))
        # print(check.cosineSim(vector, vector2))
        # print(check.pearson_def(vector, vector2))
        # img1 = TensorVector(img1).process()
        # img2 = TensorVector(img2).process()
        
        return similarity