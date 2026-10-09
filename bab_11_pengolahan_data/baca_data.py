import csv
from pathlib import Path

FILE = Path(__file__).parent / "nilai.csv"   # supaya jalan dari folder mana pun

data = []
with open(FILE) as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

print(len(data), "baris")
print(data[0])
