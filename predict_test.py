import joblib
import pandas as pd

model = joblib.load("model.pkl")
le = joblib.load("encoder.pkl")

# 🔥 Human-friendly mapping
severity_map = {
    "normal": "Good condition ✅",
    "dim": "Needs maintenance (low light) ⚠️",
    "overheat": "Fault detected (overheating) 🔥",
    "overcurrent": "Fault detected (electrical issue) ⚡"
}

samples = [
    [30, 50, 2000, 500],
    [60, 40, 2000, 500],
    [30, 50, 500, 500],
    [30, 50, 2000, 3500]
]

for s in samples:
    sample = pd.DataFrame([s],
        columns=["Temperature", "Humidity", "LDR", "Current"]
    )

    pred = model.predict(sample)
    label = le.inverse_transform(pred)[0]

    # 🔥 Convert to human output
    final_output = severity_map[label]

    print(f"Input: {s} → {final_output}")