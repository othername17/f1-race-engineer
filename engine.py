def get_setup_advice(s_delta, t_delta):
    if s_delta < -5 and t_delta < -0.1:
        return "Mid-Corner Understeer: Stiffen rear ARB or increase rake."
    elif s_delta > 5 and t_delta < -0.2:
        return "Exit Oversteer: Soften rear spring or increase rear wing."
    return "Balanced performance."

def process_telemetry(df, ref_lap, target_lap):
    ref = df[df['lapNum'] == ref_lap]
    target = df[df['lapNum'] == target_lap]
    s_delta = target['speed_kmh'].mean() - ref['speed_kmh'].mean()
    t_delta = target['throttle'].mean() - ref['throttle'].mean()
    return get_setup_advice(s_delta, t_delta)
