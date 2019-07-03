import matplotlib.pyplot as plt
import numpy as np
import shutil, os, argparse
from keras.models import load_model
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to image")
ap.add_argument("-m", "--model", required=True, help="path to model")
args = vars(ap.parse_args())

model = load_model(args["model"])
image = cv2.imread(args["image"])


print("dimensiones de la imagen a anotar: {}".format(image.shape))
width, heigh, chanels = image.shape
w = 32
print("generando la nueva imagen")

new_image = np.zeros((width-w,heigh-w))
patches = np.zeros(((width-w)*(heigh-w),w,w,chanels))
for i in range(width-w):
    for j in range(heigh-w):
        patch = image[i:i+w,j:j+w]
        #patch = np.expand_dims(patch, 0)
        new_image[i][j] = model.predict(np.expand_dims(patch, 0))[0][0]


print("forma de la nueva imagen: {}".format(new_image.shape))
print("la nueva imágen representa la probabilidad de que cada pixel sea un núcleo")

import cv2
from matplotlib import pyplot as plt

plt.imshow(new_image, cmap = 'gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
