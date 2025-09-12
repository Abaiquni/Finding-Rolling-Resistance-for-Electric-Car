# Re-import necessary packages after reset
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Constants
g = 9.81
dt = 1.0

# Load the file again
file_path = "2.csv"
df = pd.read_csv(file_path, header=None)
df.columns = ["velocity_kmh"]

# Convert km/h to m/s
v = df["velocity_kmh"].values * 1000 / 3600

# Compute acceleration (numerical derivative)
a = np.gradient(v, dt)

# Regression: -a vs v^2
X = v**2
y = -a

X_reg = sm.add_constant(X)
model = sm.OLS(y, X_reg).fit()

intercept, slope = model.params
Crr = intercept / g
# Plot velocity vs time and print CRR only

time = np.arange(len(v)) * dt

# Plot velocity vs time and show CRR in legend
plt.figure(figsize=(8,6))
plt.plot(time, v, label=f"Velocity (CRR={Crr:.4f})")
plt.xlabel("Time [s]")
plt.ylabel("Velocity [m/s]")
plt.title("Coastdown Test - Velocity vs Time (Single Direction)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print (Crr)
