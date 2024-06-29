import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from src.machine_learning.evaluation_results import load_test_evaluation

def page_ml_performance_metrics_body():
    version = 'v4'
    st.info(
        "On this page, you will find a user-friendly overview of how the dataset was divided, the performance of the model on this data, and a brief explanation of each result."
    )
    
    st.write("### Image Distribution per Set and Label")

    labels_distribution = plt.imread(f"outputs/{version}/image_counts.png")
    st.image(labels_distribution, caption='Labels Distribution across Train, Validation, and Test Sets')

    st.warning(
        "The dataset of leaves is divided into three subsets:\n\n"
        "The training set (70% of the entire dataset) is used to 'fit' the model. It learns how to generalize and make predictions on new, unseen data from this set.\n\n"
        "The validation set (10% of the dataset) helps in enhancing model performance by fine-tuning the model after each epoch (one complete pass of the training set through the model).\n\n"
        "The test set (20% of the dataset) provides the final accuracy of the model after the training phase is complete. It consists of data the model has never encountered before."
    )
    
    st.write("---")
    st.write("### Model Performance")

    model_clf = plt.imread(f"outputs/{version}/classification_report_heatmap.png")
    st.image(model_clf, caption='Classification Report')  

    st.warning(
        "**Classification Report**\n\n"
        "Precision: This is the percentage of correct predictions. It is the ratio of true positives to the sum of true positives and false positives.\n\n"
        "Recall: This measures the percentage of actual positives that were correctly identified. It is the ratio of true positives to the sum of true positives and false negatives.\n\n"
        "F1 Score: This is the percentage of correct positive predictions. It is the weighted harmonic mean of precision and recall, where the best score is 1.0 and the worst is 0.0.\n\n"
        "Support: This represents the number of actual occurrences of each class in the specified dataset."
    )

    model_roc = plt.imread(f"outputs/{version}/roc_curve.png")
    st.image(model_roc, caption='ROC Curve')

    st.warning(
        "**ROC Curve**\n\n"
        "The ROC curve is a performance measurement tool."
        " It illustrates the model's ability to distinguish between classes by making accurate predictions."
        " An ROC curve is created by plotting the true positive rate (TPR) against the false positive rate (FPR).\n\n"
        "The true positive rate is the proportion of correctly predicted observations (e.g., the leaf was predicted healthy and it is indeed healthy).\n\n"
        "The false positive rate is the proportion of incorrectly predicted observations (e.g., the leaf was predicted healthy but is actually infected)."
    )

    model_cm = plt.imread(f"outputs/{version}/confusion_matrix.png")
    st.image(model_cm, caption='Confusion Matrix')

    st.warning(
        "**Confusion Matrix**\n\n"
        "A Confusion Matrix is a performance measurement tool for classifiers."
        " It is a table with 4 different combinations of predicted and actual values.\n\n"
        "True Positive / True Negative: The prediction matches the reality.\n\n"
        "False Positive / False Negative: The prediction is the opposite of reality (e.g., the leaf was predicted infected but is actually healthy).\n\n"
        "An effective model has high TP and TN rates, and low FP and FN rates."
    )

    model_perf = plt.imread(f"outputs/{version}/curve_c_model_loss_acc.png")
    st.image(model_perf, caption='Model Performance')  

    st.warning(
        "**Model Performance**\n\n"
        "Loss represents the sum of errors made for each example in the training (loss) or validation (val_loss) sets.\n\n"
        "The loss value indicates how poorly or well a model behaves after each iteration of optimization.\n\n"
        "Accuracy measures how accurate the model's predictions (accuracy) are compared to the true data (val_acc).\n\n"
        "A good model performs well on unseen data, indicating it is able to generalize and hasn't overfitted to the training dataset."
    )