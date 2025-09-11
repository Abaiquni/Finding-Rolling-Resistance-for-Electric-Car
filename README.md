#  Coastdown Test - Estimation of Rolling Resistance Coefficient (CRR)

##  Description
This project documents the **Coastdown Test** method to estimate: **CRR (Coefficient of Rolling Resistance)**


The procedure follows **SAE J1263 / J2263** standards, using coastdown runs in **two opposite directions** to eliminate the effect of road slope (grade).

---

## Physics Principle

When a vehicle is coasting freely in straight track:

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
- Measure **total vehicle mass** (including driver).
- Set tire pressure according to the conditions to be tested.
- keep the transmission system consistent during testing.

### 2. Test Track
- Straight, flat track segment (+-3km).
- Low wind.
- No outside distraction

### 3. Data Collection
- Accelerate vehicle to a target speed (e.g. 30 km/h).
- Release throttle, allow the vehicle to coast down to < 0 km/h.
- Record **speed vs. time** at fixed intervals (e.g. 1s, or 500ms).
- Repeat test at least 3 times in **Direction A** and **Direction B** (Direction B is reversed of Direction A), this reversed direction need to be tested to eliminate the effect of grade $$(\theta)$$.

### 4. Sensor
Sensor that being used in this test is **wheel proximity sensor**:
- Count wheel RPM from pulses (RPM).
- Convert to linear speed (Km/h):

---

##  Data Format
The input `.csv` file should contain one column of vehicle speed in km/h:

```csv
time velocity_kmh
1 32.2
2 31.9
3 31.7
...
