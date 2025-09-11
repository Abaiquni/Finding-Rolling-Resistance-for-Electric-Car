#  Coastdown Test - Estimation of Rolling Resistance Coefficient (CRR)

##  Description
This project documents the **Coastdown Test** method to estimate:
- **CRR (Coefficient of Rolling Resistance)**
- **Aerodynamic parameter (Cd·Af)**

The procedure follows **SAE J1263 / J2263** standards, using coastdown runs in **two opposite directions** to eliminate the effect of road slope (grade).

---

## ⚙️ Physics Principle

When a vehicle is coasting freely:

$$
m \cdot a = - \left( F_{rr} + F_{aero} + F_{grade} \right)
$$

where:

- Rolling resistance:

$$
F_{rr} = C_{rr} \cdot m \cdot g
$$

- Aerodynamic drag:

$$
F_{aero} = \tfrac{1}{2} \rho A_f C_d v^2
$$

- Road grade force:

$$
F_{grade} = m \cdot g \cdot \sin(\theta)
$$

After performing coastdown in two opposite directions and averaging:

$$
-a(v) = C_{rr} \cdot g + \frac{\rho A_f C_d}{2m} v^2
$$

Thus:

- **Regression intercept** → $C_{rr} \cdot g$  
- **Regression slope** → $\tfrac{\rho A_f C_d}{2m}$  

---

##  Experimental Procedure

### 1. Preparation
- Measure **total vehicle mass** (including driver and payload).
- Set tire pressure to manufacturer specification.
- Keep transmission in neutral during the test.

### 2. Test Track
- Straight, flat road segment (≥ 1 km).
- Low wind (< 2 m/s is recommended).

### 3. Data Collection
- Accelerate vehicle to a target speed (e.g. 100 km/h).
- Release throttle, allow the vehicle to coast down to < 20 km/h.
- Record **speed vs. time** at fixed intervals (e.g. 1 Hz).
- Repeat test at least 3 times in **Direction A** and **Direction B**.

### 4. Sensor
If using a **wheel proximity sensor**:
- Count wheel RPM from pulses.
- Convert to linear speed:

$$
v = \frac{RPM \cdot \pi \cdot D}{60}
$$

---

##  Data Format
The input `.csv` file should contain one column of vehicle speed in km/h:

```csv
time velocity_kmh
1 32.2
2 31.9
3 31.7
...
