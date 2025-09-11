# analyze_coastdown.py
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.interpolate import interp1d

# ==============================
# Parameter
# ==============================
g = 9.81   # gravitasi [m/s²]
dt = 1.0   # interval sampling data [s]

# ==============================
# Fungsi untuk proses satu dataset
# ==============================
def process_dataset(file_path):
    # Baca CSV (hanya satu kolom kecepatan km/h)
    df = pd.read_csv(file_path, header=None)
    df.columns = ["velocity_kmh"]

    # Konversi kecepatan km/h -> m/s
    v = df["velocity_kmh"].values * 1000 / 3600

    # Hitung percepatan dengan diferensiasi numerik
    a = np.gradient(v, dt)

    return v, a

# ==============================
# Fungsi utama analisis coastdown dua arah
# ==============================
def analyze_coastdown(file1, file2):
    # Proses dua dataset
    v1, a1 = process_dataset(file1)
    v2, a2 = process_dataset(file2)

    # Buat grid kecepatan bersama
    common_v = np.linspace(
        min(v1.min(), v2.min()),
        max(v1.max(), v2.max()),
        200
    )

    # Interpolasi percepatan terhadap kecepatan
    f1 = interp1d(v1, a1, bounds_error=False, fill_value="extrapolate")
    f2 = interp1d(v2, a2, bounds_error=False, fill_value="extrapolate")

    a1_interp = f1(common_v)
    a2_interp = f2(common_v)

    # Rata-rata percepatan dua arah
    a_avg = (a1_interp + a2_interp) / 2

    # Data regresi: -a vs v²
    X = common_v**2
    y = -a_avg

    X_reg = sm.add_constant(X)
    model = sm.OLS(y, X_reg).fit()

    intercept, slope = model.params
    Crr = intercept / g

    # ==============================
    # Output hasil
    # ==============================
    print("=== Hasil Coastdown Test Dua Arah ===")
    print(f"Intercept       : {intercept:.6f}")
    print(f"Slope           : {slope:.6e}")
    print(f"CRR             : {Crr:.6f}")

    # ==============================
    # Plot hasil regresi
    # ==============================
    plt.figure(figsize=(8,6))
    plt.scatter(X, y, s=10, alpha=0.6, label="Data -a(v) vs v²")
    plt.plot(X, model.predict(X_reg), "r-", label="Regresi Linear")
    plt.xlabel("v² [m²/s²]")
    plt.ylabel("-a [m/s²]")
    plt.title("Coastdown Test Dua Arah - Estimasi CRR")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ==============================
# Main program
# ==============================
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python analyze_coastdown.py file_forward.csv file_backward.csv")
        sys.exit(1)

    file_forward = sys.argv[1]
    file_backward = sys.argv[2]

    analyze_coastdown(file_forward, file_backward)


#ini cuman tambahan