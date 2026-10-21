def budget_impact(patients, cost_per_patient, uptake_rate):
    if not 0 <= uptake_rate <= 1:
        raise ValueError("uptake_rate must be between 0 and 1")
    return round(patients * uptake_rate * cost_per_patient, 2)
