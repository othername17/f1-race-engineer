import streamlit as st
import pandas as pd
from engine import process_telemetry

st.title("F1 Setup Advisor")
file = st.file_uploader("Upload CSV", type="csv")

if file:
    df = pd.read_csv(file)
processed_df = process_telemetry(df, ref, target)    ref = st.selectbox("Reference Lap", laps)
    target = st.selectbox("Your Lap", laps)
    
    if st.button("Get Setup Advice"):
        advice = process_telemetry(df, ref, target)
        st.write(f"### Engineer's Advice: {advice}")
