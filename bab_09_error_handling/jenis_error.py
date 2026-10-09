# Mendemokan 7 jenis error umum (dibungkus try-except supaya semuanya tampil).
# SyntaxError & IndentationError tidak bisa ditangkap try-except biasa
# (terjadi sebelum program jalan), jadi ditulis sebagai komentar di bawah.

contoh = [
    ("NameError",         lambda: print(skor_x)),
    ("TypeError",         lambda: "5" + 3),
    ("ValueError",        lambda: int("abc")),
    ("ZeroDivisionError", lambda: 10 / 0),
    ("IndexError",        lambda: [1, 2][5]),
    ("KeyError",          lambda: {"a": 1}["b"]),
]

for nama, fungsi in contoh:
    try:
        fungsi()
    except Exception as e:
        print(f"{nama}: {e}")

# SyntaxError:       print("hai"
# IndentationError:  if x:
#                    print(x)
