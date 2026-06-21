import streamlit as st
import pandas as pd
from engine import process_telemetry

st.title("F1 Setup Advisor")
file = st.file_uploader("Upload CSV", type="csv")

if file:
    # Use sep='\t' to split the combined string into proper columns
    df = pd.read_csv(file, sep='\t')
    
    # Check for the actual lap column name
    lap_col = [col for col in df.columns if 'lap' in col.lower()][0]
    
    laps = sorted(df[lap_col].unique())
    ref = st.selectbox("Reference Lap", laps)
    target = st.selectbox("Your Lap", laps)
    
    if st.button("Get Setup Advice"):
        # Pass the identified lap column to the engine
        advice = process_telemetry(df, ref, target, lap_col)
        st.write(f"### Engineer's Advice: {advice}")
