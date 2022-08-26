from mlverify2 import cnn_verify
import os
img_dir = '../data'
img_path_list = ['adhar.jpg']
index = 0
img_path = os.path.join(img_dir, img_path_list[index])
model_name = 'vgg16'

print(cnn_verify.make_prediction(model_name, img_path))