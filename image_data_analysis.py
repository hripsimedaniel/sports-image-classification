# -*- coding: utf-8 -*-
"""FROM_COLAB_Image_data_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t6L0fowKl_6NPPQ-KDcRHgjxwlEYF4RK
"""

from google.colab import drive
drive.mount('/content/drive')

base_dir = "/content/drive/MyDrive/Final_Project/images"

import tensorflow as tf
import os

#Count how many images we have in each folder, folders are sorted by sports disciplines

image_dict = {}

for folder in os.listdir("/content/drive/MyDrive/Final_Project/images"):
  #print(folder)
  temp = []
  
  for file in os.listdir("/content/drive/MyDrive/Final_Project/images/" + folder):
    #print(file)
    temp.append(file)
  print(folder+" has "+ str(len(temp)))
  x = {folder: str(len(temp))}
  image_dict.update(x)


print(image_dict)

#Plot pie chart showing list of sports and ratio of each sports images in data

import matplotlib.pyplot as plt

# Get the Keys and store them in a list
labels = list(image_dict.keys())

# Get the Values and store them in a list
values = list(image_dict.values())

plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, radius = 2)

plt.show()