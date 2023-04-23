import tensorflow as tf
import streamlit as st
from PIL import Image
import numpy as np
import pyttsx3
engine = pyttsx3.init()

model = tf.keras.models.load_model('cashRec.h5')

classes = ['fifty', 'five', 'fivehundred', 'hundred', 'ten', 'thousand', 'twenty']

def classify_image(img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)/255
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    index = np.argmax(predictions)
    y_pred = classes[index]
    return y_pred


uploaded_file = st.file_uploader('Choose an image file', type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    prediction = classify_image(uploaded_file)
    output = f"The Note is {prediction} rupees."
    st.write(output)
    engine.say(f"{prediction} Rupees")
    engine.setProperty('volume', 1)
    engine.runAndWait()


# In Terminal type: streamlit run main.py

