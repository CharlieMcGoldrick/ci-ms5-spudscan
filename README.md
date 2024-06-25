# Table of Contents 
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and Validation](#hypothesis-and-validation)

# Dataset Content
The dataset is the Potato Plant Diseases Dataset from [Kaggle](https://www.kaggle.com/datasets/hafiznouman786/potato-plant-diseases-data/versions/1).

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
1. BR1: The client is interested in understanding how different disease symptoms correlate with specific potato diseases (early blight, late blight) and healthy leaves. Therefore, they expect data visualizations showing these correlations against the leaf categories.
2. BR2: The client wants to accurately identify and classify potato plant health states using a machine learning model, specifically a Convolutional Neural Network (CNN).
3. BR3: The client is interested in obtaining detailed prediction reports for the examined leaves.

## Epics & User Stories
To address these business requirements, we have outlined the following epics and user stories. Each user story is broken down into manageable tasks, following an agile development process.

- Epic: Information Gathering and Data Collection
    1. US1: As a client, I want to know which symptoms are most correlated with each potato disease (early blight, late blight) and healthy leaves so that I can focus on key diagnostic features. _(Business Requirement Covered: BR1)_
    2. US2: As a user, I want to know the source and content of the data used in training the model to be confident in the quality of the trained model. _(Business Requirements Covered: BR2, BR3)_
- Epic: Data Visualization, Cleaning, and Preparation
    1. US1: As a client, I want to see visualizations of symptom correlations with leaf health categories to better understand the disease patterns. _(Business Requirement Covered: BR1)_
    2. US2: As a user, I want access to the data cleaning and preparation pipeline to quickly process new data for health state classification. _(Business Requirement Covered: BR2)_
    3. US3: As a user, I want to understand the project hypotheses and how they were validated to understand the mechanisms behind health state detection. _(Business Requirement Covered: BR2)_
- Epic: Model Training, Optimization, and Validation
    1. US1: As a client, I want a reliable model to classify the health states of potato plants so that I can provide timely advice to farmers. _(Business Requirement Covered: BR2)_
    2. US2: As a technical user, I want to understand the machine learning steps used to develop the health state classification model to ensure transparency and reproducibility. _(Business Requirement Covered: BR2)_
    3. US3: As a technical user, I want to know the model performance metrics to ensure that the predictions are reliable. _(Business Requirement Covered: BR2)_
- Epic: Dashboard Planning, Designing, and Development
    1. US1: As a client, I want an interactive dashboard to display the classification results and visualize the relationships between symptoms and leaf health states. _(Business Requirements Covered: BR1, BR2)_
    2. US2: As a user, I want interactive input widgets to provide real-time data and get health state classification results instantly. _(Business Requirement Covered: BR2)_
- Epic: Dashboard Deployment and Release
    1. US1: As a client, I want a detailed prediction report for each examined leaf to make informed decisions about disease management. _(Business Requirement Covered: BR3)_

[Back to top ⇧](#table-of-contents)