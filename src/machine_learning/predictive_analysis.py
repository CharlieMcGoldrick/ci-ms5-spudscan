import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from src.data_management import load_pkl_file

def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """
    prob_per_class = pd.DataFrame(
        data=pred_proba,
        index=pred_class,
        columns=['Probability']
    )
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)

def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    img_array = img_to_array(img_resized)
    my_image = np.expand_dims(img_array, axis=0) / 255.0

    return my_image

def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """
    model = load_model(f"outputs/{version}/best_model.h5")

    pred_proba = model.predict(my_image)[0]

    # Load class indices
    class_indices = load_pkl_file(file_path=f"outputs/{version}/class_indices.pkl")
    target_map = {v: k for k, v in class_indices.items()}
    pred_class_index = np.argmax(pred_proba)
    pred_class = target_map[pred_class_index]
    pred_proba_value = pred_proba[pred_class_index]

    st.write(
        f"The predictive analysis indicates the sample leaf is "
        f"**{pred_class.lower()}** with a probability of {pred_proba_value:.2f}."
    )

    return pred_proba, pred_class