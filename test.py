import tensorflow as tf
from tensorflow import keras
from imutils import paths
import numpy as np
import argparse
import cv2
import os
#print(tf.version.VERSION)


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="chemin de l'image pour prediction")

ap.add_argument("-m", "--model", 
    default="covid.model",
	help="chemin du model")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (224, 224))
images = []
images.append(image)
data = np.array(images) / 255.0
savedmodel=tf.keras.models.load_model(args["model"])
#savedmodel.summary()
q = savedmodel.predict(data)
q = list(q[0])

print("Probabilité que cette personne est malade :",q[0])
print("Probabilité que cette personne n'est pas malade :",q[1])
