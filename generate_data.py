import pandas as pd
import random

data = []

for _ in range(2000):
    temp = round(random.uniform(20, 70), 2)
    hum = round(random.uniform(30, 80), 2)
    ldr = random.randint(0, 4095)
    current = random.randint(0, 4000)

    # ---- Strong AI-based risk logic ----
    risk = 0

    # Temperature
    if temp > 65:
        risk += 0.7
    elif temp > 55:
        risk += 0.5
    elif temp > 48:
        risk += 0.3

    # Light
    if ldr < 600:
        risk += 0.5
    elif ldr < 1000:
        risk += 0.3

    # Current
    if current > 3500:
        risk += 0.5
    elif current > 3000:
        risk += 0.3

    # 🔥 Combination effects (AI strength)
    if temp > 50 and ldr < 1000:
        risk += 0.3

    if temp > 50 and current > 3000:
        risk += 0.3

    if ldr < 800 and current > 3000:
        risk += 0.3

    risk = min(1.0, risk)

    # ---- Labeling ----
    if risk >= 0.7:
        label = "fault"
    elif risk >= 0.3:
        label = "warning"
    else:
        label = "normal"

    data.append([temp, hum, ldr, current, label])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Temperature", "Humidity", "LDR", "Current", "Label"
])

df.to_csv("led_data.csv", index=False)

print("Dataset created!")
print("Total rows:", len(df))