
import shutil, os, argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
print(image.shape)
