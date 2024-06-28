import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"My project focuses on developing an accurate machine learning model to identify and classify potato plant diseases, "
        f"specifically early blight and late blight, using leaf images. This model will help farmers detect diseases early and manage crop health more effectively. "
        f"The dataset used for this project contains 2152 images of potato plants, categorized based on their health and disease status.\n\n"
        f"**Visual Criteria for Detection**\n\n"
        f"The visual criteria used to detect the health state of potato leaves are as follows:\n"
        f"* **Healthy Potato Leaves:** Uniform green color, no spots or lesions.\n"
        f"* **Early Blight:** Presence of small, dark brown to black spots on older leaves, often with concentric rings forming a 'target' pattern.\n"
        f"* **Late Blight:** Large, irregularly shaped brown lesions on leaves, often with a greenish halo."
    )

    st.warning(
        f"**Project Dataset**\n\n"
        f"The dataset is sourced from Kaggle and contains high-resolution images of potato leaves. Each image is labeled as healthy, early blight, or late blight. "
        f"This dataset is essential for training and validating our machine learning model to ensure accurate disease classification.\n\n"
        f"Dataset breakdown:\n"
        f"* Healthy: 152 images\n"
        f"* Early Blight: 1000 images\n"
        f"* Late Blight: 1000 images\n\n"
        f"For additional details, refer to the [Potato Plant Diseases Dataset on Kaggle](https://www.kaggle.com/datasets/hafiznouman786/potato-plant-diseases-data)."
    )

    st.success(
        f"The project has three primary business requirements:\n\n"
        f"1. **Understanding Disease Symptoms:** Visualize correlations between disease symptoms and specific potato diseases (early blight, late blight) and healthy leaves. "
        f"Data visualizations will help in understanding these correlations.\n\n"
        f"2. **Accurate Classification:** Develop a Convolutional Neural Network (CNN) to accurately identify and classify potato plant health states using leaf images.\n\n"
        f"3. **Detailed Prediction Reports:** Generate detailed prediction reports for the examined leaves, including prediction results and associated probabilities."
    )

    st.write(
        f"You can find more information in the "
        f"[Project README file](https://github.com/CharlieMcGoldrick/ci-ms5-spudscan#readme)."
    )
