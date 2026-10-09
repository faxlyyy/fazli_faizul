import csv
from pathlib import Path

# --- baca data ---
data = []
with open(Path(__file__).parent / "nilai.csv") as f:
    for baris in csv.DictReader(f):
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

# --- rekap nilai per kelas ---
rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")
