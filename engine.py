def process_telemetry(df):
    # This looks for common column names used in F1 telemetry
    # It converts them to lowercase so the code can find them
    df.columns = df.columns.str.lower()
    
    # Check if 'throttle' or 'brake' exist in your file
    # If it finds them, it processes them
    if 'throttle' in df.columns:
        df['throttle'] = df['throttle'].clip(0, 1)
    
    if 'brake' in df.columns:
        df['brake'] = df['brake'].clip(0, 1)
        
    return df
