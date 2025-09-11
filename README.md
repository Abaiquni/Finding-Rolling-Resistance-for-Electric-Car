# 🚗 Coastdown Test - Perhitungan Coefficient of Rolling Resistance (CRR)

## 📖 Deskripsi
Proyek ini mendokumentasikan metode **Coastdown Test** untuk menghitung:
- **CRR (Coefficient of Rolling Resistance)**
- **Parameter aerodinamika (Cd·Af)**

Metode mengikuti standar **SAE J1263 / J2263**, dengan coastdown dalam **dua arah berlawanan** untuk menghilangkan efek elevasi (slope).

---

## ⚙️ Prinsip Fisika
Saat kendaraan meluncur bebas:

$$
m \cdot a = - \big( F_{rr} + F_{aero} + F_{grade} \big)
$$

dengan:

- Rolling resistance:
  $$
  F_{rr} = C_{rr} \cdot m \cdot g
  $$

- Aerodynamic drag:
  $$
  F_{aero} = \tfrac{1}{2} \rho A_f C_d v^2
  $$

- Gaya akibat elevasi jalan:
  $$
  F_{grade} = m \cdot g \cdot \sin(\theta)
  $$

Jika coastdown dilakukan dua arah dan dirata-rata:

$$
-a(v) = C_{rr} \cdot g + \frac{\rho A_f C_d}{2m} v^2
$$

- **Intercept regresi** → $C_{rr} \cdot g$  
- **Slope regresi** → $\tfrac{\rho A_f C_d}{2m}$  

---

## 🧪 Prosedur Eksperimen

### 1. Persiapan
- Ukur **massa kendaraan total** (termasuk sopir & beban uji).
- Tekanan ban sesuai spesifikasi.
- Transmisi netral saat uji.

### 2. Lintasan
- Jalan lurus & datar, minimal 1 km.
- Angin < 2 m/s (disarankan pagi/sore).

### 3. Pengambilan Data
- Akselerasi kendaraan ke **100 km/h** (atau sesuai kebutuhan).
- Lepas akselerator, biarkan meluncur sampai **< 20 km/h**.
- Rekam **kecepatan vs waktu** tiap 1 detik.
- Ulangi tes minimal 3 kali di **arah A** dan **arah B**.

### 4. Sensor
Jika menggunakan **proximity sensor ban**:
- Hitung RPM roda dari jumlah pulsa.
- Konversi ke kecepatan linear:

$$
v = \frac{RPM \cdot \pi \cdot D}{60}
$$

---

## 📂 Struktur Data
Format file `.csv` yang dipakai:

```csv
velocity_kmh
32.2
31.9
31.7
...
