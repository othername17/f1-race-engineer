def process_telemetry(df):
    # Core logic for telemetry markers
    df['throttle'] = df['throttle'].clip(0, 1)
    df['brake'] = df['brake'].clip(0, 1)
    return df
