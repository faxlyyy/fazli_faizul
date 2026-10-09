# Python Dasar

Kumpulan kode latihan dari materi **Python Dasar** (11 bab, teori + praktik).

## Struktur

| Folder | Isi |
|---|---|
| `bab_01_pengenalan` | print, komentar, indentasi |
| `bab_02_variabel_tipe_data` | variabel, int/float/str/bool, casting, string |
| `bab_03_input_output` | print() lanjutan, input() |
| `bab_04_operator` | aritmatika, perbandingan, logika, penugasan |
| `bab_05_percabangan` | if/elif/else, nested, ternary, match-case |
| `bab_06_perulangan` | for, while, break/continue/pass |
| `bab_07_koleksi_data` | list, tuple, set, dictionary |
| `bab_08_function` | def, parameter, lambda, scope |
| `bab_09_error_handling` | try/except, raise |
| `bab_10_module_package` | import, module sendiri, pip |
| `bab_11_pengolahan_data` | CSV, filter, rekap, pandas |

## Cara menjalankan

```bash
python bab_01_pengenalan/hello.py
```

Untuk bab 10 (module sendiri), jalankan dari dalam folder `proyek`:

```bash
cd bab_10_module_package/proyek
python main.py
```

Untuk `pakai_pandas.py`: `pip install -r requirements.txt` dulu.

## Catatan

- Butuh Python 3.10+ (karena `match-case`).
- `tuple.py` sengaja berakhir dengan `TypeError` (itu bagian dari contoh).
- `string.py` dan `operator.py` di slide diganti nama jadi `string_demo.py` dan
  `operator_demo.py` agar tidak bentrok dengan module bawaan Python.
