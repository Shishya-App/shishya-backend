import sewar.full_ref as sewa
import imgcompare
from PIL import Image
from skimage.metrics import structural_similarity
import cv2
import numpy
class aina:
    def isadhar(image):
        image= Image.open(image)
        newsize = (678, 381)
        image = image.resize(newsize)
      #   ms=sewa.mse(image,'testadha3.jpg')
        mssi=sewa.msssim(image,'testadha3.jpg')
        si=sewa.ssim(image,'testadha3.jpg')
        q=sewa.uqi(image,'testadha3.jpg')
        vif=sewa.vifp(image,'testadha3.jpg')
        if( mssi>0.9 and si>0.9 and q>0.9 and vif>0.9 ):
            return True
        else:
            return False
        
        diff= imgcompare.image_diff_percent(image,'testadha3.jpg')
        return diff<0.95
        
#     def structural_sim(img1, img2):

#         sim, diff = structural_similarity(img1, img2, full=True)
#         return sim

#     def orb_sim(img1, img2):
#   # SIFT is no longer available in cv2 so using ORB
        

#         orb = cv2.ORB_create()

#   # detect keypoints and descriptors
#         kp_a, desc_a = orb.detectAndCompute(img1, None)
#         kp_b, desc_b = orb.detectAndCompute(img2, None)

#   # define the bruteforce matcher object
#         bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
#   #perform matches. 
#         matches = bf.match(desc_a, desc_b)
#   #Look for similar regions with distance < 50. Goes from 0 to 100 so pick a number between.
#         similar_regions = [i for i in matches if i.distance < 50]  
#         if len(matches) == 0:
#           return 0
#         return len(similar_regions) / len(matches)

    
    