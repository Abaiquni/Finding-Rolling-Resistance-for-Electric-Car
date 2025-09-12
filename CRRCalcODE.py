import numpy as np
import pandas as pd
from scipy.integrate import odeint
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Constants (assumed)
g = 9.81
rho = 1.225   # air density (kg/m³)
Af = 0.4294      # frontal area (m²)
Cd = 0.1495     # drag coefficient
m = 78      # vehicle mass (kg)

# Load experimental data (from uploaded 2.csv)
file_path = "1.csv"
df = pd.read_csv(file_path, header=None)
df.columns = ["velocity_kmh"]

# Convert to m/s
v_measured = df["velocity_kmh"].values * 1000 / 3600
t = np.arange(len(v_measured))  # assume 1s sampling

# ODE model
def dvdt(v, t, Crr):
    return -(Crr * g) - (0.5 * rho * Af * Cd / m) * v**2

def simulate(Crr):
    v0 = v_measured[0]
    v_pred = odeint(dvdt, v0, t, args=(Crr,))
    return v_pred.flatten()

# Cost function (SSE)
def cost(Crr):
    v_pred = simulate(Crr[0])
    return np.sum((v_measured - v_pred)**2)

# Optimization
res = minimize(cost, x0=[0.0025], bounds=[(0.001, 0.02)])
Crr_opt = res.x[0]

# Simulate with optimal CRR
v_fit = simulate(Crr_opt)
# Convert to km/h for plotting
v_kmh = v_measured * 3.6
v_fit_kmh = v_fit * 3.6

# Plot measured vs simulated in km/h
plt.figure(figsize=(8,6))
plt.plot(t, v_kmh, "o", markersize=3, label="Measured (km/h)")
plt.plot(t, v_fit_kmh, "r-", label=f"Fitted (CRR={Crr_opt:.4f})")
plt.xlabel("Time [s]")
plt.ylabel("Velocity [km/h]")
plt.title("Coastdown Test - Measured vs Simulated (km/h vs time)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

Crr_opt
