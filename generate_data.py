import pandas as pd
import random

data = []

for _ in range(800):  # increased data size
    # ---- Generate base values ----
    temp = round(random.uniform(20, 70), 2)
    hum = round(random.uniform(30, 80), 2)
    ldr = random.randint(0, 4095)
    current = random.randint(0, 4000)

    # ---- Add sensor noise ----
    temp += random.uniform(-2, 2)
    ldr += random.randint(-100, 100)
    current += random.randint(-200, 200)

    # keep values in valid range
    ldr = max(0, min(4095, ldr))
    current = max(0, min(4000, current))

    # ---- Fuzzy logic (IMPORTANT) ----
    if temp > 55:
        label = "overheat"

    elif 48 < temp <= 55:
        label = random.choice(["overheat", "normal"])  # borderline

    elif ldr < 800:
        label = "dim"

    elif 800 <= ldr < 1200:
        label = random.choice(["dim", "normal"])  # borderline

    elif current > 3200:
        label = "overcurrent"

    elif 2800 < current <= 3200:
        label = random.choice(["overcurrent", "normal"])  # borderline

    else:
        label = "normal"

    data.append([temp, hum, ldr, current, label])

# ---- Create DataFrame ----
df = pd.DataFrame(data, columns=[
    "Temperature", "Humidity", "LDR", "Current", "Label"
])

# ---- Save CSV ----
df.to_csv("led_data.csv", index=False)

print("Improved dataset created!")