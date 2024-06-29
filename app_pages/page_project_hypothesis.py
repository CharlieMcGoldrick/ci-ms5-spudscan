import streamlit as st
import matplotlib.pyplot as plt

def page_project_hypothesis_body():
    st.write("### Hypothesis 1: Symptom Correlation")

    st.info(
        "We suspect potato leaves affected by early blight or late blight have distinct symptoms, such as leaf spots, discoloration, "
        "and lesions, differentiating them from healthy leaves."
    )
    st.info(
        "To validate this hypothesis, we conducted the following studies and analyses:\n\n"
        "- **Average Image Study:** Investigated common features in healthy, early blight, and late blight leaves by computing their average images.\n"
        "- **Data Annotation:** Annotated images with specific symptoms such as leaf spots, discoloration, and lesions.\n"
        "- **Symptom Feature Extraction:** Used image processing techniques to extract features related to these symptoms.\n"
        "- **Correlation Analysis:** Performed statistical analysis to determine the correlation between these symptoms and the health categories.\n"
        "- **Visualization:** Created visualizations like scatter plots, heatmaps, and annotated average images to illustrate the correlation."
    )
    st.success(
        "The model was able to detect such differences and learn how to differentiate and generalize in order to make accurate predictions. "
        "It exceeded well above the 75% accurarcy rate set out by the client and so has been a success"
        "A good model trains its ability to predict classes on a batch of data without adhering too closely to that set of data. "
        "In this way, the model is able to generalize and predict future observations reliably because it didn't 'memorize' the relationships "
        "between features and labels as seen in the training dataset but the general pattern from feature to labels."
    )
    
    st.write("To explore the validation of these processes, visit the pages using the navigation on the left:")
    st.markdown("""
    - **Leaves Visualizer**
    - **Health State Detector**
    - **ML Performance Metrics**
    """)