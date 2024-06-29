# Deployed version at [SpudScan](https://ci-ms5-spudscan-c8cc6dcae5c7.herokuapp.com/)

# Table of Contents 
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypotheses and Validations](#hypotheses-and-validations)
4. [Rationale to Map Business Requirements to Data Visualizations and ML Tasks](#rationale-to-map-business-requirements-to-data-visualizations-and-ml-tasks)
5. [ML Business Case](#ml-business-case)
6. [Dashboard Design](#dashboard-design)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Technologies used](#technologies-used)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

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

# Bugs

## Known Bugs
No known bugs

## Fixed Bugs
- [Fix: adjust dataset ratios](https://github.com/CharlieMcGoldrick/ci-ms5-spudscan/commit/3d4a778b345e4ea9ecd9cd40d045c13a6c78cdce) - The validation and test ratio were both set to `0.15`. I set this to validation ratio of `0.1` and test ratio of `0.2`
- [Fix: add import to load model](https://github.com/CharlieMcGoldrick/ci-ms5-spudscan/commit/030beb3329c230b4e2873c441209783bfdf58a97) - Needed to add `from keras.models import load_model`
- [Fix: Correct DataFrame shape handling for prediction probabilities](https://github.com/CharlieMcGoldrick/ci-ms5-spudscan/commit/e0518b9bf54fbae7e40c8fd110156eecf718ddec) - Correct DataFrame shape handling for prediction probabilities by ensuring pred_proba and class_labels are in correct list format. Adjusted Streamlit app and functions to properly handle and display prediction results.

[Back to top ⇧](#table-of-contents)

# Deployment

## Creating the Heroku App
To deploy this project on Heroku, follow these steps:
1. **Create a `requirements.txt` File**: This file should list all the dependencies the program needs to run. Heroku uses this file to install the necessary packages.
2. **Set the Python Runtime**: Create a `runtime.txt` file specifying a Python version compatible with the Heroku-20 stack.
3. **Push Changes to GitHub**: Commit and push your recent changes to GitHub.
4. **Create a Heroku App**:
   - Log into your Heroku account.
   - Click "CREATE NEW APP," provide a unique name, and select a geographical region.
5. **Add Buildpacks**: From the Settings tab, add the `heroku/python` buildpack.
6. **Deploy the App**:
   - Go to the Deploy tab, choose GitHub as the deployment method.
   - Connect to GitHub and select your project's repository.
   - Choose the branch you want to deploy and click "Deploy Branch."
7. **Enable Deploys**:
   - You can either enable automatic deploys or manually deploy by selecting "Deploy Branch."
8. **Monitor the Logs**: Wait for the logs to show the dependencies being installed and the app being built.
9. **Access the App**: Once deployed, your app will be accessible via a link like `https://your-project-name.herokuapp.com/`.
10. **Manage Slug Size**: If the slug size is too large, add unnecessary large files to the `.slugignore` file.

## Clone a GitHub Repository

To make a clone of this repository, follow these steps:

1. **Login to your GitHub account**.
2. **Go to the repository** by visiting the link: [Charlie McGoldrick Github - SpudScan Repo](https://github.com/CharlieMcGoldrick/ci-ms5-spudscan).
3. **Click the "Code" button** and then use the copy button next to the link to copy the link.
4. **In your IDE of choice, open a new terminal** and use the following clone command:
   `git clone https://github.com/CharlieMcGoldrick/ci-ms5-spudscan`

## Forking the GitHub Repository

To fork this repository, follow these steps:

1. **Log in to your GitHub account**.
2. **Go to the repository you want to fork**, which is located at: [Charlie McGoldrick Github - SpudScan Repo](https://github.com/CharlieMcGoldrick/ci-ms5-spudscan).
3. **In the top-right corner of the repository page, click on the "Fork" button**.
4. **GitHub will prompt you to select where you want to fork the repository**. Choose your personal account or organization.
5. **Wait for the forking process to complete**. Once it's done, you will be redirected to your forked repository under your GitHub account.

**NOTE**: Any changes pushed to the main branch automatically show up on the website.

[Back to top ⇧](#table-of-contents)

# Technologies used
## Platforms
- GitHub: Repository for storing the project code.
- Kaggle: Source for downloading datasets.
- Gitpod: Development environment used for writing code, committing changes, and pushing to GitHub.
- Jupyter Notebook: Utilized for editing and running code.
- Heroku: Used to deploy the project.

## Languages
- Markdown
- Python

## Main Data Analysis and Machine Learning Libraries
- **matplotlib 3.3.1**: Plotted dataset distributions.
- **numpy 1.19.2**: Utilized for array conversions.
- **pandas 1.1.2**: Managed data creation and storage as dataframes.
- **tensorflow-cpu 2.6.0**: Used for creating the model.
- **keras 2.6.0**: Set model hyperparameters.
- **scikit-learn 0.24.2**: Applied for model evaluation.
- **plotly 5.12.0**: Visualized the model's learning curve.
- **seaborn 0.11.0**: Plotted the model's confusion matrix.
- **streamlit 0.85.0**: Developed the project dashboard.

[Back to top ⇧](#table-of-contents)

# Credits

## Dataset
- The Potato leaves dataset is from [Kaggle](https://www.kaggle.com/datasets/hafiznouman786/potato-plant-diseases-data/data)

## Code
- [Template used](https://github.com/Code-Institute-Solutions/milestone-project-bring-your-own-data) to start the project
- Model learning Curve - C is from [Stack Overflow](https://stackoverflow.com/questions/41908379/keras-plot-training-validation-and-test-set-accuracy) by [Tim Seed](https://stackoverflow.com/users/3257992/tim-seed)
- App pages for the Streamlit dashboard were largely from [ci-walkthrough-malaria-detector](https://github.com/CharlieMcGoldrick/ci-walkthrough-malaria-detector)

[Back to top ⇧](#table-of-contents)

# Acknowledgements
- Thanks to my mentor Mo Shami and Code Institue.
- Thank you to my friends and family for their patience and understanding whilst working on this project.

[Back to top ⇧](#table-of-contents)