import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import os

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)

def page_health_state_detector_body():
    st.info(
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
        model = None
        version = 'v4'
        file_path = f'outputs/{version}'
        model_path = f"{file_path}/best_model.h5"
        
        if not os.path.exists(model_path):
            st.error(f"Model file not found at {model_path}. Please ensure the model file is in the correct location.")
            return
        
        try:
            model = load_model(model_path, compile=False)
            model_loaded = True
        except OSError as e:
            st.error(f"Error loading the model file at {model_path}. Ensure the file is not corrupted and is a valid TensorFlow/Keras model. Error: {e}")
            return
        
        if model_loaded:
            for image in images_buffer:
                img_pil = Image.open(image)
                st.info(f"Potato leaf Sample: **{image.name}**")
                img_array = np.array(img_pil)
                st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

                resized_img = resize_input_image(img=img_pil, version=version)
                pred_proba, class_labels = load_model_and_predict(resized_img, model, version)
                plot_predictions_probabilities(pred_proba, class_labels)

                pred_class = class_labels[np.argmax(pred_proba)]
                df_report = df_report.append({"Name": image.name, 'Result': pred_class}, ignore_index=True)
            
            if not df_report.empty:
                st.success("Analysis Report")
                st.table(df_report)