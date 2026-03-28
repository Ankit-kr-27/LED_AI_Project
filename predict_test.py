import joblib
import pandas as pd

model = joblib.load("model.pkl")

def get_output(probs, classes):
    prob_dict = dict(zip(classes, probs))

    # 🔥 Improved risk score
    risk = (
        1.0 * prob_dict.get("fault", 0) +
        0.6 * prob_dict.get("warning", 0) +
        0.1 * prob_dict.get("normal", 0)
    )

    if risk > 0.7:
        status = "🔥 High Risk"
    elif risk > 0.3:
        status = "⚠️ Warning"
    else:
        status = "✅ Normal"

    return risk, status, prob_dict


def explain(sample):
    temp, hum, ldr, current = sample
    reasons = []

    if temp > 50:
        reasons.append("High temperature")
    if ldr < 1000:
        reasons.append("Low light output")
    if current > 3000:
        reasons.append("High current draw")

    return reasons


samples = [
    [30, 50, 2000, 500],
    [60, 40, 2000, 500],
    [30, 50, 500, 500],
    [30, 50, 2000, 3500],
    [52, 45, 1100, 2900],
    [68, 40, 400, 3600]
]

for s in samples:
    df = pd.DataFrame([s], columns=[
        "Temperature", "Humidity", "LDR", "Current"
    ])

    probs = model.predict_proba(df)[0]
    classes = model.classes_

    # ✅ Proper function call
    risk, status, prob_dict = get_output(probs, classes)
    reasons = explain(s)

    print("\nInput:", s)
    print("Risk Score:", round(risk, 2))
    print("Status:", status)
    print("Confidence:", prob_dict)
    print("Reason:", ", ".join(reasons) if reasons else "Stable")