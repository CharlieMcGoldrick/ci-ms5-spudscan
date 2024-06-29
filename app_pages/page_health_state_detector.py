import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    resize_input_image,
    plot_predictions_probabilities
)

def load_tflite_model(model_path):
    # Load the TFLite model and allocate tensors
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    
    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    return interpreter, input_details, output_details

def predict_with_tflite(interpreter, input_details, output_details, image):
    # Preprocess the image
    input_shape = input_details[0]['shape']
    img = image.resize((input_shape[1], input_shape[2]))
    img = np.array(img, dtype=np.float32)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    
    # Set the tensor to the image
    interpreter.set_tensor(input_details[0]['index'], img)
    
    # Run the interpreter
    interpreter.invoke()
    
    # Get the predictions
    predictions = interpreter.get_tensor(output_details[0]['index'])
    
    return predictions

def page_health_state_detector_body():
    st.write("### Health State Detector")
    st.warning(
        "Upload pictures of potato leaves to discover whether they are healthy, affected by early blight, or late blight, and download a report of the examined leaves."
    )

    st.write(
        "You can download a set of infected and healthy leaves for live prediction from [here](https://www.kaggle.com/datasets/hafiznouman786/potato-plant-diseases-data)."
    )

    st.write("---")
    
    st.write("**Upload a clear picture of a potato leaf. You may select more than one.**")
    images_buffer = st.file_uploader(' ', type='jpeg', accept_multiple_files=True)
   
    if images_buffer:
        df_report = pd.DataFrame([])
        model_loaded = False
        interpreter = None
        input_details = None
        output_details = None
        version = 'v4'
        file_path = f'outputs/{version}'
        model_path = f"{file_path}/best_model_quantized.tflite"
        
        if not os.path.exists(model_path):
            st.error(f"Model file not found at {model_path}. Please ensure the model file is in the correct location.")
            return
        
        try:
            interpreter, input_details, output_details = load_tflite_model(model_path)
            model_loaded = True
        except OSError as e:
            st.error(f"Error loading the model file at {model_path}. Ensure the file is not corrupted and is a valid TFLite model. Error: {e}")
            return
        
        if model_loaded:
            for image in images_buffer:
                img_pil = Image.open(image)
                st.info(f"Potato leaf Sample: **{image.name}**")
                img_array = np.array(img_pil)
                st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

                # Resize the image
                resized_img = img_pil.resize((256, 256))
                
                # Predict with TFLite model
                pred_proba = predict_with_tflite(interpreter, input_details, output_details, resized_img)
                
                # Load class labels (assuming you have a function or a list)
                class_labels = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
                
                plot_predictions_probabilities(pred_proba[0], class_labels)

                pred_class = class_labels[np.argmax(pred_proba)]
                df_report = df_report.append({"Name": image.name, 'Result': pred_class}, ignore_index=True)
            
            if not df_report.empty:
                st.success("Analysis Report")
                st.table(df_report)