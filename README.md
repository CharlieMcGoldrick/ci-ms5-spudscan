# Table of Contents 
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypotheses and Validations](#hypotheses-and-validations)
4. [Rationale to Map Business Requirements to Data Visualizations and ML Tasks](#rationale-to-map-business-requirements-to-data-visualizations-and-ml-tasks)
5. [ML Business Case](#ml-business-case)
6. [Dashboard Design](#dashboard-design)

# Dataset Content
The dataset is the Potato Plant Diseases Dataset from [Kaggle](https://www.kaggle.com/datasets/hafiznouman786/potato-plant-diseases-data).

This dataset contains 2152 images of potato plants, categorized based on their health and disease status. The dataset is designed for use in developing and testing models for accurate identification and classification of potato plant diseases.

## Categories Included
- Healthy (152 images)
- Early Blight (1000 images)
- Late Blight (1000 images)

[Back to top ⇧](#table-of-contents)


# Business Requirements
Our client, an agricultural technology firm, seeks assistance in developing an accurate machine learning model to identify and classify potato plant diseases, specifically early blight and late blight, using leaf images. This model will help farmers detect diseases early and manage crop health more effectively.

Although the client has extensive knowledge in traditional farming methods, they lack expertise in machine learning and image recognition, which are essential for this project. They have provided us with a comprehensive dataset of potato leaf images showing various disease states.

For more details, refer to the [interview with the Operations Manager of Green Fields Potato Farm](https://github.com/CharlieMcGoldrick/ci-ms5-spudscan/wiki/Business-Requirements-Interview).

We have agreed on the following business requirements with our client:
1. Business Requirement 1 (BR1): Data Visualization
    - We will display the "mean" and "standard deviation" images for healthy, early blight and late blight leaves.
    - We will display the difference between average leaves.
    - We will display an image montage for healthy, early blight and late blight leaves.
2. Business Requirement 2 (BR2): CNN Model for Health State Classification
    - We want to predict if a given leaf is healthy or has early/late blight.
    - We want to build a binary classifier and generate reports.

## Epics & User Stories
To address these business requirements, we have outlined the following epics and user stories. Each user story is broken down into manageable tasks, following an agile development process.

- Epic: Information Gathering and Data Collection
    1. US1: As a user, I want to know the source and content of the data used in training the model to be confident in the quality of the trained model. (Business Requirements Covered: BR2)
- Epic: Data Visualization, Cleaning, and Preparation
    1. US1: As a client, I want to see visualizations that differentiate healthy potato leaves from those affected by early blight and late blight to better understand the distinguishing features. (Business Requirement Covered: BR1)
    2. US2: As a user, I want access to the data cleaning and preparation pipeline to quickly process new data for health state classification. (Business Requirement Covered: BR2)
    3. US3: As a user, I want to understand the project hypotheses and how they were validated to understand the mechanisms behind health state detection. (Business Requirement Covered: BR2)
- Epic: Model Training, Optimization, and Validation
    1. US1: As a client, I want a reliable model to classify the health states of potato leaves so that I can provide timely advice to farmers. (Business Requirement Covered: BR2)
    2. US2: As a technical user, I want to understand the machine learning steps used to develop the health state classification model to ensure transparency and reproducibility. (Business Requirement Covered: BR2)
    3. US3: As a technical user, I want to know the model performance metrics to ensure that the predictions are reliable. (Business Requirement Covered: BR2)
- Epic: Dashboard Planning, Designing, and Development
    1. US1: As a client, I want an interactive dashboard to display the classification results and visualize the differences between healthy leaves and those affected by early blight and late blight. (Business Requirements Covered: BR1, BR2)
    2. US2: As a user, I want interactive input widgets to provide real-time data and get health state classification results instantly. (Business Requirement Covered: BR2)
- Epic: Dashboard Deployment and Release
    1. US1: As a client, I want a detailed prediction report for each examined leaf to make informed decisions about disease management. (Business Requirement Covered: BR2)

[Back to top ⇧](#table-of-contents)

# Hypotheses and Validations
1. Hypothesis 1: Symptom Correlation
    - **Hypothesis:** We suspect potato leaves affected by early blight or late blight have distinct symptoms, such as leaf spots, discoloration, and lesions, differentiating them from healthy leaves.
    - **Validation:**
        - **Average Image Study:** Conduct an average image study to investigate the common features in healthy, early blight, and late blight leaves.
        - **Data Annotation:** Annotate the images with specific symptoms such as leaf spots, discoloration, and lesions.
        - **Symptom Feature Extraction:** Use image processing techniques to extract features related to these symptoms.
        - **Visualization:** Create visualizations such as heatmaps, and annotated average images to illustrate the correlation.

[Back to top ⇧](#table-of-contents)

# Rationale to Map Business Requirements to Data Visualizations and ML Tasks
1. Business Requirement 1 (BR1): Data Visualization
    - We will display the "mean" and "standard deviation" images for healthy, early blight and late blight leaves.
    - We will display the difference between average leaves.
    - We will display an image montage for healthy, early blight and late blight leaves.
2. Business Requirement 2 (BR2): CNN Model for Health State Classification
    - We want to predict if a given leaf is healthy or has early/late blight.
    - We want to build a classifier and generate reports.

[Back to top ⇧](#table-of-contents)

# ML Business Case

## Predict Potato Plant Health States
**Model:** Convolutional Neural Network (CNN)

To meet the second business requirement (BR2), we will train a CNN model.
- Objective: Enable accurate identification and classification of potato plant health states.
- Approach: Supervised learning using a CNN to process high-resolution images.
- Success Metrics:
    - Achieve at least 75% accuracy on the validation set.
    - The model is considered a failure if it misclassifies more than 25% of the images.
- Output: A health state classification for each input image.

[Back to top ⇧](#table-of-contents)

# Dashboard Design
The dataset provided contains 2152 images of potato leaves, categorized as healthy, early blight, or late blight. This data will be used to train and validate the model. The model will be integrated into an interactive dashboard to allow real-time health state classification and visualization of the results.

Page 1: Quick Project Summary
- Overview of the project, dataset, and business requirements.

Page 2: Leaf Visualizer
- Interactive visualizations to differentiate between healthy and diseased leaves.
- Display mean and standard deviation images for each health category.

Page 3: Health State Detector
- Upload leaf images to get real-time classification results.
- Display prediction statements and associated probabilities.
- Provide a downloadable report of the examined leaves.

Page 4: Project Hypotheses and Validation
- Present hypothesis, explanation, validation process, and conclusion.

Page 5: ML Evaluation Metrics
- Label Distribution for Training, Validation, and Test Sets:
    - Frequency counts for each label across the training, validation, and test datasets to ensure balanced representation.
- Dataset Allocation:
    - Percentage breakdown of the entire dataset across training, validation, and test sets to understand the data split.
- Performance Metrics:
    - ROC Curve: A graphical representation of the model's diagnostic ability, illustrating the true positive rate against the false positive rate at various threshold settings.
    - Confusion Matrix: A table that shows the number of true positives, true negatives, false positives, and false negatives to evaluate the model's accuracy.
- Training Progress:
    - Model History: Tracking accuracy and loss metrics over epochs to observe the model's learning process, specifically using a CNN model.
- Final Model Assessment:
    - Test Set Evaluation: Final performance results on the test set to validate the model's generalization ability and real-world applicability.

[Back to top ⇧](#table-of-contents)