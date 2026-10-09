# Install dulu:  pip install pandas
import pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "nilai.csv")
print(df.groupby("kelas")["nilai"].mean())
print(df[df["nilai"] >= 75]["nama"].tolist())
print(df.sort_values("nilai").tail(1))
