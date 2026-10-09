# pip & Virtual Environment

Jalankan di terminal (di folder proyek):

```bash
# buat & aktifkan virtual environment
python -m venv .venv
source .venv/bin/activate        # Mac / Linux
.venv\Scripts\activate           # Windows

# install paket dari PyPI
pip install pandas requests

# simpan & pasang ulang dependensi
pip freeze > requirements.txt
pip install -r requirements.txt
```
