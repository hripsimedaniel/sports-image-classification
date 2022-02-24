#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#downlading and preparing raw data


# In[28]:


import os
from PIL import Image


# In[40]:


data_images = []
for file in os.listdir("C:/Users/manve/Documents/SaskPolytech/FINAL PROJECT/Downloaded_images"):
    
  try:
    image = Image.open("C:/Users/manve/Documents/SaskPolytech/FINAL PROJECT/Downloaded_images/"+file)
    # image = image.thumbnail((128,128), Image.ANTIALIAS)
    # print(image)
    image.resize((64,64), Image.ANTIALIAS)
    # print(image.format)
    if(image.format == "JPEG"):
        data_images.append(image)
  except: 
    pass

len(data_images)


# In[ ]:





# In[41]:


#printing images


# In[42]:


from matplotlib import pyplot
from matplotlib.image import imread


# In[43]:


i = 0
images = []


# In[44]:


folder_images = "C:/Users/manve/Documents/SaskPolytech/FINAL PROJECT/Downloaded_images/"


# In[45]:


#load in data

for image in os.listdir(folder_images):
  img = Image.open(folder_images+image)
  img = img.resize((64,64))
  images.append(img)


# In[46]:


#Plot images, then save as save.png

row = 3
col = 5


# In[47]:


import matplotlib.pyplot as plt

fig, axs = plt.subplots(row,col)
cnt = 0
for i in range(row):
  for j in range(col):
    axs[i,j].imshow(images[cnt])
    
    axs[i,j].axis('off')
    cnt += 1
fig.savefig("save.png")


# In[ ]:




