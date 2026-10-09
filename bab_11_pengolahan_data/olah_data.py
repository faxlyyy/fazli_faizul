import csv
from pathlib import Path

# --- baca data (sama seperti baca_data.py) ---
data = []
with open(Path(__file__).parent / "nilai.csv") as f:
    for baris in csv.DictReader(f):
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

# --- olah data ---
nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [d["nama"] for d in data
         if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])
