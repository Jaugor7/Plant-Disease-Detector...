from django.shortcuts import render, redirect
from django.contrib import messages
import numpy as np
import pickle
from PIL import Image
from django.http import JsonResponse
from django.contrib import messages

import os
import re
import sys

import tensorflow as tf


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from glob import glob

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model=load_model("model_inception.h5")

def index(request):
    return render(request, 'index.html')

def model_predict(img, model):
    img = img.resize((224,224), Image.ANTIALIAS)

    x = image.img_to_array(img)
    print(x.shape)

    x=x/255
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    print("Printing All Probs")
    print(preds)

    preds = np.argmax(preds, axis=1)

    print("Printing Max Probs")
    print(preds[0])

    preds = preds[0]

    if preds==0:
        preds="The Disease is Bacterial Spot."
    elif preds==1:
        preds="The Disease is Early Blight."
    elif preds==2:
        preds="The Disease is Late Blight."
    elif preds==3:
        preds="The Disease is Leaf Mold."
    elif preds==4:
        preds="The Disease is Septoria Leaf Spot."
    elif preds==5:
        preds="The Disease is Spider Mites."
    elif preds==6:
        preds="The Disease is Target Spot."
    elif preds==7:
        preds="The Disease is Yellow Leaf Curl Virus"
    elif preds==8:
        preds="The Disease is Mosaic Virus."
    elif preds==9:
        preds="No Disease. Healthy Leaf."
    
    return preds

def check(request):
    if request.method == 'POST':
        f = request.FILES['image']
        img = Image.open(f)

        preds = model_predict(img, model)
        messages.success(request, preds)
        return JsonResponse({1:'true'})

    messages.error(request, "Invalid Request To The URL.")
    return redirect('/')
