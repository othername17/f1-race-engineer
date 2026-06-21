import streamlit as st
import pandas as pd
from engine import process_telemetry

st.title("F1 Setup Advisor")
file = st.file_uploader("Upload CSV", type="csv")

if file:
    df = pd.read_csv(file)
    
    # Show us the columns so we can fix the mapping if 'lapNum' is wrong
    st.write("Column names found:", df.columns.tolist())
    
    # Try to find the lap column. If 'lapNum' doesn't exist, this will show an error
    # we can fix immediately.
    try:
        laps = sorted(df['lapNum'].unique())
        ref = st.selectbox("Reference Lap", laps)
        target = st.selectbox("Your Lap", laps)
        
        if st.button("Get Setup Advice"):
            advice = process_telemetry(df, ref, target)
            st.write(f"### Engineer's Advice: {advice}")
    except KeyError:
        st.error("Error: Could not find 'lapNum' column. Look at the list above and tell me which one is the lap identifier.")
