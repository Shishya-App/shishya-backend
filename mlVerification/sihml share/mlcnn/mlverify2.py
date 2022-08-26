import os
import numpy as np
import matplotlib.pyplot as plt

from keras.applications.vgg16 import VGG16
from keras.applications.resnet import ResNet50
from keras.applications.vgg16 import VGG16  
import tensorflow as tf
from keras.models import Model
from keras.models import model_from_json
from keras.utils import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.imagenet_utils import preprocess_input, decode_predictions

import cv2
from IPython.display import HTML, display
from glob import glob
from PIL import Image
import time

class cnn_verify:
    def create_folder(folder_name):
    # """ Create folder if there is not
    # Args:
    #     folder_name: String, folder name
    # Returns:
    #     None
    # """
        if not os.path.isdir(f"../models/{folder_name}"):
            os.makedirs(f"../models/{folder_name}")
            print(f"Folder '../models/{folder_name}' created")

    def load_model(model_name, include_top=True):
    # """ Load pre-trained Keras model
    # Args:
    #     model_name: String, name of model to load
    #     include_top: String, the model is buildt with 'feature learning block' + 'classification block'
    # Returns:
    #     model: Keras model instance
    # """
        available_models = ['vgg16', 'resnet50']
        selected_model = 'vgg16'
        
        if selected_model in available_models:
            # Load a Keras instance
            try:
                if model_name == 'vgg16':
                    model = VGG16(weights='imagenet', include_top=include_top)
                elif model_name == 'resnet50':
                    model = ResNet50(weights='imagenet', include_top=include_top)
                print(f">> '{model.name}' model successfully loaded!")
            except:
                print(f">> Error while loading model '{selected_model}'")
        
        # Wrong selected model
        else:
            print(f">> Error: there is no '{selected_model}' in {available_models}")
    
        return model

    def get_img_size_model(model = load_model('vgg16', include_top=True)):
    # """Returns image size for image processing to be used in the model
    # Args:
    #     model: Keras model instance 
    # Returns:
    #     img_size_model: Tuple of integers, image size
    # """
        model_name = model
        if model_name == "vgg16":
            img_size_model = (224, 224)
        elif model_name == "resnet50":
            img_size_model = (224, 224)
        else:
            img_size_model = (224, 224)
            print("Warning: model name unknown. Default image size: {}".format(img_size_model))
            
        return img_size_model


    def get_layername_feature_extraction(model = load_model('vgg16', include_top=True)):
        # """ Return the name of last layer for feature extraction   
        # Args:
        #     model: Keras model instance
        # Returns:
        #     layername_feature_extraction: String, name of the layer for feature extraction
        # """
        model_name = model.name
        if model_name == "vgg16":
            layername_feature_extraction = 'fc2'
        elif model_name == "resnet50":
            layername_feature_extraction = 'predictions'
        else:
            layername_feature_extraction = ''
            print("Warning: model name unknown. Default layername: '{}'".format(layername_feature_extraction))
        
        return layername_feature_extraction    


    def get_layers_list(model):
    # """Get a list of layers from a model
    # Args:
    #     model: Keras model instance
    # Returns:
    #     layers_list: List of string of layername
    # """
        layers_list = []
        for i in range(len(model.layers)):
            layer = model.layers[i]        
            layers_list.append(layer.name)
            
        return layers_list

    def image_processing(img_array):
    # """ Preprocess image to be used in a keras model instance
    # Args:
    #     img_array: Numpy array of an image which will be predicte
    # Returns:
    #     processed_img = Numpy array which represents the processed image
    # """    
    # Expand the shape
        img = np.expand_dims(img_array, axis=0)

    # Convert image from RGB to BGR (each color channel is zero-centered with respect to the ImageNet dataset, without scaling)
        processed_img = preprocess_input(img)
    
        return processed_img



    def make_prediction(model, img_path, display_img=False):
        """Make a prediction of an image by passing in the model
        
        Args:
            model: Keras model instance used to do the classification.
            img_path: String to the image path which will be predicted
            display_img: Boolean to decid to show image. Defaults to True
            
        Returns:
            predicted_class: String which represents the class of the predicted image from ImageNet
        """
        img_type = os.path.basename(img_path).split(".")[0]
        
        # Image processing
        img_size_model = cnn_verify.get_img_size_model(model)
        img = image.load_img(img_path, target_size=img_size_model)
        img_arr = np.array(img)
        img_ = cnn_verify.image_processing(img_arr)
    
        preds = model.predict(img_)
        top_preds = decode_predictions(preds)
        predicted_class = top_preds[0][0][1]
        predicted_class_percentage = top_preds[0][0][2]*100
        
        # print('Top 5 predictions:')
        for i in range(len(top_preds[0])):
            print("  {} >>>>> {}".format(i+1, top_preds[0][i]))
        
        if display_img:
            print()
            plt.axis('off')
            plt.title("({}) Original image: {}\nPrediction: {} ({:.2f}%)".format(model.name, img_type, predicted_class, predicted_class_percentage))
            plt.imshow(img_arr)
            
        return predicted_class