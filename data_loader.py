import os
import pandas as pd
import matplotlib.pyplot as plt
import cv2

def LoadData(frameObj, imgPath, maskPath, shape=256):
    imgNames = os.listdir(imgPath)
    names = []
    maskNames = []
    unames = [imgName.split(')')[0] for imgName in imgNames]
    unames = list(set(unames))

    for uname in unames:
        names.append(uname + ').png')
        maskNames.append(uname + ')_mask.png')

    imgAddr = imgPath + '/'
    maskAddr = maskPath + '/'

    for name, maskName in zip(names, maskNames):
        img = plt.imread(imgAddr + name)
        mask = plt.imread(maskAddr + maskName)

        img = cv2.resize(img, (shape, shape))
        mask = cv2.resize(mask, (shape, shape))

        frameObj['img'].append(img)
        frameObj['mask'].append(mask)

    return frameObj
