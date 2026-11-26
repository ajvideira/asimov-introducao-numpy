import numpy as np
from skimage.transform import rescale
import scipy.ndimage
import cv2
import os

FILENAME = 'teste_img.jpg'

PATH = os.path.join('assets', FILENAME)

img = cv2.imread(PATH)

cv2.imshow('Imagem original', img)

cv2.waitKey(0)