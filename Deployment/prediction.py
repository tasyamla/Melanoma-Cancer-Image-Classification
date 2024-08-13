#import library
import pandas as pd
import numpy as np
import streamlit as st
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import tensorflow_hub as hub

#import pickle
import pickle

#load model
def app():
    file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    model = load_model('model_seq_imp.keras', custom_objects={'KerasLayer': hub.KerasLayer})
    target_size=(224, 224)

    def import_and_predict(image_data, model):
        image = tf.keras.utils.load_img(image_data, target_size=(224, 224))
        x = tf.keras.utils.img_to_array(image)
        x = np.expand_dims(x, axis=0)

        plt.imshow(image)
        plt.axis('off')
        plt.show()

        # Make prediction
        classes = model.predict(x)
        result_pred = np.where(classes >= 0.5, 1, 0)
        if result_pred == 1:
            result = 'Malignant'
        else:
            result = 'Benign'

        return f"Prediction: {result}"

    if file is None:
        st.text("Please upload an image file")
    else:
        result = import_and_predict(file, model)
        st.image(file)
        st.write(result)
        
if __name__ == "__main__":
    run()