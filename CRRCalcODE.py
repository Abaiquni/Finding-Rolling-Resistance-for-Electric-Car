import numpy as np
import pandas as pd
from scipy.integrate import odeint
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Constants (assumed)
g = 9.81
rho = 1.225   # air density (kg/m³)
Af = 0.4294286      # frontal area (m²)
Cd = 0.1495849     # drag coefficient
m = 76     # vehicle mass (kg) 49+26

# Load experimental data
file_path = r"F:\OneDrive - UGM 365\UGM Akademik\Semester 7\Skripsi\Workplace\VehicleModel\CRRFinding\Data\rolling2.csv"
df = pd.read_csv(file_path, header=None)

# Extract columns and remove empty rows
df.columns = ["timestamp", "speed_kmh"]
df = df.dropna()  # Remove rows with NaN values

# Extract values
timestamp = df["timestamp"].values
v_measured_kmh = df["speed_kmh"].values

# Remove rows where timestamp is not strictly increasing
valid_idx = np.ones(len(timestamp), dtype=bool)
for i in range(1, len(timestamp)):
    if timestamp[i] <= timestamp[i-1]:
        valid_idx[i] = False

timestamp = timestamp[valid_idx]
v_measured_kmh = v_measured_kmh[valid_idx]

# Convert speed to m/s
v_measured = v_measured_kmh / 3.6

# Use the actual timestamp as time (already in seconds)
t = timestamp

print(f"Number of valid data points: {len(v_measured)}")
print(f"Time range: {t[0]:.4f} s to {t[-1]:.4f} s")
print(f"Initial velocity: {v_measured[0]:.2f} m/s ({v_measured_kmh[0]:.2f} km/h)")
print(f"Final velocity: {v_measured[-1]:.2f} m/s ({v_measured_kmh[-1]:.2f} km/h)")
print()

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
print("Starting optimization...")
res = minimize(cost, x0=[0.0015], bounds=[(0.001, 0.002)], method='L-BFGS-B')
Crr_opt = res.x[0]

print(f"Optimization successful!")
print(f"Optimal CRR: {Crr_opt:.6f}")
print(f"Cost (SSE): {res.fun:.4f}")
print()

# Simulate with optimal CRR
v_fit = simulate(Crr_opt)

# Plot measured vs simulated
# Plot measured vs simulated
plt.figure(figsize=(12, 10))
plt.plot(t, v_measured_kmh, "o", markersize=3, label="Experimental Measured", alpha=0.7)
plt.plot(t, v_fit * 3.6, "r-", linewidth=2, label=f"Fitted (CRR={Crr_opt:.6f})")

# Set label dengan ukuran font lebih besar
plt.xlabel("Time (s)", fontsize=20)  # Ukuran font 14
plt.ylabel("Velocity (km/h)", fontsize=20)  # Ukuran font 14

# Anda juga bisa memperbesar font untuk judul dan legend
plt.title("Coastdown Test - Experimental vs Simulated", fontsize=20)
plt.legend(fontsize=20)

# Perbesar font ticks (angka pada sumbu)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate residuals
residuals = v_measured_kmh - (v_fit * 3.6)
print(f"Mean residual: {np.mean(residuals):.4f} km/h")
print(f"Std residual: {np.std(residuals):.4f} km/h")
print(f"Max absolute residual: {np.max(np.abs(residuals)):.4f} km/h")
print(f"\nOptimal CRR: {Crr_opt:.6f}")