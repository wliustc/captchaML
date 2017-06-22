# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:31:30 2017

@author: marsggbo
"""

import PIL.Image as image
import numpy as np
from sklearn.cluster import KMeans

def loadImage(filePath):
    with open(filePath,'rb') as f:
        data = []
        img = image.open(f)
        w,h = img.size
        for i in range(w):
            for j in range(h):
                x,y,z = img.getpixel((i,j))
                data.append([x/256.0,y/256.0,z/256.0])
    return np.mat(data),w,h

imgData,w,h = loadImage("check.jpg")
label = KMeans(n_clusters=2).fit_predict(imgData)

label = label.reshape([w,h])
new_img = image.new("L",(w,h))
for i in range(w):
    for j in range(h):
        new_img.putpixel((i,j),int(256/(label[i][j]+1)))
new_img.save("kmeansImg.jpg","jpeg")

        
