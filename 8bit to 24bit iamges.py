#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  08 16:42:56 2020

@author: xumy
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

import sys
import shutil

path=r'./train/JpegImages/'
newpath=r'./train/output'
def turnto24(path):
   files = os.listdir(path)
   files = np.sort(files)
   i=0
   for f in files:
        imgpath = path + f
        img=Image.open(imgpath).convert('RGB')
        dirpath = newpath
        file_name, file_extend = os.path.splitext(f)
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.jpg')
        img.save(dst)

turnto24(path)



