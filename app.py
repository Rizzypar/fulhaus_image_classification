import gradio as gr
import cv2
from PIL import Image as im
from numpy import asarray
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import tensorflow as tf
import json
def classify_image(inp):
    loaded_model = keras.models.load_model('my_model.h5')
    train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    train_generator = train_datagen.flow_from_directory(
        'train2',
        target_size=(128, 128),
        batch_size=32,
        class_mode='categorical',
        subset='training')
    class_Predictor = train_generator.class_indices
    new_width = 128
    new_height = 128
    img = im.fromarray(inp)
    new_img = img.resize((new_width,new_height))
    new_arr = asarray(new_img)
    img_array = tf.expand_dims(new_arr, 0)
    predictions = loaded_model.predict(img_array, steps=1)
    print(predictions)
    pred=np.argmax(predictions)
    result = ""
    for keys in class_Predictor:
        if class_Predictor[keys] == pred:
            result = keys
    return result

def run():
    app = gr.Interface(fn=classify_image,
                 inputs=gr.Image(shape=(224, 224)),
                 outputs=gr.Label(num_top_classes=3))
    app.launch(server_name="0.0.0.0", server_port=7000, share=True)

if __name__ == "__main__":
    run()