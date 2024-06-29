import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random

def page_leaves_visualizer_body():
    st.write("### Leaves Visualizer")
    st.info(
        f"A study that visually differentiates healthy potato leaves from those affected by early blight and late blight.")

    st.warning(
        f"We suspect potato leaves affected by early blight and late blight have distinct visual symptoms. "
        f"Early blight typically presents as small, dark brown to black spots with concentric rings on older leaves, "
        f"while late blight manifests as large, irregularly shaped brown lesions, often with a greenish halo and white fungal growth under moist conditions.\n\n" 
        f"These properties must be translated into machine learning terms. "
        f"Images need to be 'prepared' before being fed to the model for optimal feature extraction and training.\n\n"
        f"When dealing with an image dataset, it's important to normalize the images in the dataset before training a Neural Network on it. "
        f"To normalize an image, one needs the mean and standard deviation of the entire dataset, calculated with a mathematical formula "
        f"that considers the properties of an image."
    )
    
    version = 'v4'
    if st.checkbox("Difference between average and variability image"):
        avg_healthy = plt.imread(f"outputs/{version}/stats_Potato___healthy.png")
        avg_early_blight = plt.imread(f"outputs/{version}/stats_Potato___Early_blight.png")
        avg_late_blight = plt.imread(f"outputs/{version}/stats_Potato___Late_blight.png")

        st.success(
            f"### Summary of Differences:\n\n"
            f"**Early Blight:**\n"
            f"* **Brighter Leaves:** The average intensity of the images shows that early blight leaves are generally brighter than the other categories.\n"
            f"* **High Variation:** There is a significant difference between individual images, which means that early blight can appear quite differently from one leaf to another. This is likely due to different stages or severity of the disease.\n\n"
            f"**Late Blight:**\n"
            f"* **Darker Leaves:** The average intensity is lower, indicating these leaves are generally darker than early blight leaves but still distinct from healthy leaves.\n"
            f"* **Moderate Variation:** The variation between images is less than early blight but more than healthy leaves, suggesting some consistency in appearance but still noticeable differences among individual leaves.\n\n"
            f"**Healthy Leaves:**\n"
            f"* **Balanced Brightness:** The intensity is between early and late blight, indicating a balanced level of brightness.\n"
            f"* **Natural Variation:** Healthy leaves show a lot of natural variation, which can be due to different lighting conditions, angles, and inherent differences in the leaves themselves.\n\n"
            f"These differences help us understand how each category looks on average and how much they vary, which is crucial for training an accurate machine learning model."
        )

        st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
        st.image(avg_early_blight, caption='Early Blight - Average and Variability')
        st.image(avg_late_blight, caption='Late Blight - Average and Variability')
        st.write("---")

    if st.checkbox("Differences between average diseased and average healthy leaves"):
        avg_diff_healthy_early = plt.imread(f"outputs/{version}/avg_diff_Potato___healthy_Potato___Early_blight.png")
        avg_diff_healthy_late = plt.imread(f"outputs/{version}/avg_diff_Potato___healthy_Potato___Late_blight.png")
        avg_diff_early_late = plt.imread(f"outputs/{version}/avg_diff_Potato___Early_blight_Potato___Late_blight.png")

        st.success(
            f"The differences between these average images show how the appearance of leaves changes from healthy to diseased states:\n\n"
            f"* **Healthy vs Early Blight:** The difference highlights how early blight leaves are generally brighter and have distinct spots.\n"
            f"* **Healthy vs Late Blight:** This shows that late blight leaves are darker with large, irregular lesions.\n"
            f"* **Early Blight vs Late Blight:** Comparing these two diseases shows that early blight has brighter and more uniform spots, while late blight has larger and darker lesions.\n\n"
            f"These comparisons help us identify specific visual features that our machine learning model can use to distinguish between healthy and diseased leaves."
        )
        st.image(avg_diff_healthy_early, caption='Difference between Healthy and Early Blight')
        st.image(avg_diff_healthy_late, caption='Difference between Healthy and Late Blight')
        st.image(avg_diff_early_late, caption='Difference between Early Blight and Late Blight')

    if st.checkbox("Image Montage"):
        st.write("To refresh the montage, click on the 'Create Montage' button")
        my_data_dir = 'inputs/potato_disease_dataset'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:

        # checks if your montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path + '/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows * ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")