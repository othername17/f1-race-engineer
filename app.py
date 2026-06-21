import streamlit as st
import pandas as pd
from engine import process_telemetry

st.title("F1 Telemetry Analyzer")

uploaded_file = st.file_uploader("Upload telemetry CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    processed_df = process_telemetry(df)
    st.write("Processed Data", processed_df)
    st.line_chart(processed_df[['throttle', 'brake']])
