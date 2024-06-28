import streamlit as st
from app_pages.multipage import MultiPage

# Load pages scripts
from app_pages.page_summary import page_summary_body
# from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
# from app_pages.page_health_state_detector import page_health_state_detector_body
# from app_pages.page_project_hypothesis import page_project_hypothesis_body
# from app_pages.page_ml_performance import page_ml_performance_metrics_body

app = MultiPage(app_name="Potato Plant Disease Detector")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
# app.add_page("Leaves Visualiser", page_leaves_visualizer_body)
# app.add_page("Health State Detector", page_health_state_detector_body)
# app.add_page("Project Hypothesis", page_project_hypothesis_body)
# app.add_page("ML Performance Metrics", page_ml_performance_metrics_body)

app.run()