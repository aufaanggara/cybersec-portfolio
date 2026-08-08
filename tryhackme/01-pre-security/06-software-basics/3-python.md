```
=== Python: Guess The Number - Resume Materi ===

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi    : Bahasa pemrograman high-level, general-purpose
High-level  : Menyembunyikan detail teknis komputer (memori, register, dll)
General-purpose : Bisa dipakai untuk banyak hal →
                  web apps, automation, data science, machine learning

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIGA KONSEP FUNDAMENTAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. VARIABEL    → tempat menyimpan data/nilai
2. CONDITIONAL → membuat keputusan (if/elif/else)
3. LOOP        → mengulang kode selama kondisi terpenuhi (while)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VARIABEL YANG DIPAKAI DI GAME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
secret  = angka rahasia yang dipilih komputer (1–20)
guess   = tebakan pengguna (awal = 0, di luar range valid)
tries   = jumlah percobaan pengguna (awal = 0)
text    = input mentah dari pengguna (bertipe string)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FUNGSI / METHOD PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import random          → memuat library untuk angka acak
random.randint(1, 20)  → hasilkan angka acak antara 1 dan 20 (inklusif)
print("...")           → tampilkan teks/nilai ke layar
input("...")           → minta input dari pengguna → hasilnya STRING
int(text)              → konversi string → integer (bilangan bulat)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CONDITIONAL (if / elif / else)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Struktur  :
  if KONDISI:          → cek kondisi pertama
      ...
  elif KONDISI:        → cek kondisi berikutnya jika if false
      ...
  else:                → jalankan jika semua kondisi di atas false
      ...

Operator perbandingan :
  <   → kurang dari
  >   → lebih dari
  ==  → sama dengan
  !=  → tidak sama dengan
  or  → salah satu kondisi harus true

Logika game :
  if guess < 1 or guess > 20  → "Out of range"
  elif guess < secret          → "Too low"
  elif guess > secret          → "Too high"
  else                         → "You got it!" (pasti sama)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LOOP (while)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Struktur  :
  while KONDISI:
      ...kode yang diulang...

Cara kerja :
  → Python cek kondisi
  → Kalau TRUE  : jalankan semua kode di dalam (indented)
  → Kalau FALSE : berhenti / keluar dari loop

Di game ini  : while guess != secret → ulangi selama tebakan salah
Berhenti saat: guess == secret (pengguna berhasil menebak)

Analogi nyata :
  Beli kaos    → cek toko satu per satu SAMPAI ketemu yang cocok
  Cari parkir  → cek baris satu per satu SAMPAI dapat tempat kosong

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 EVOLUSI PROGRAM (v1 → v2 → v3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
guess_v1.py → Bisa pilih angka & baca input, BELUM ada perbandingan
guess_v2.py → Sudah ada if/elif/else, TAPI hanya 1 kesempatan menebak
guess_v3.py → LENGKAP: ada while loop → bisa tebak berkali-kali

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KODE FINAL LENGKAP (guess_v3.py)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import random

secret = random.randint(1, 20)
tries  = 0
guess  = 0

print("I'm thinking of a number between 1 and 20")

while guess != secret:
    text  = input("Take a guess: ")
    guess = int(text)
    tries = tries + 1

    if guess < 1 or guess > 20:
        print("That number is out of range. Try again.")
    elif guess < secret:
        print("Too low, try again.")
    elif guess > secret:
        print("Too high, try again.")
    else:
        print("You got it in", tries, "tries!")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
String      = tipe data teks (hasil input() selalu string)
Integer     = tipe data bilangan bulat (dikonversi pakai int())
Library     = kumpulan fungsi siap pakai (contoh: random)
Indentation = penjorokan kode = tanda kode ada di dalam blok if/while
Iteration   = satu kali perulangan loop
Pseudo-code = penulisan logika pakai bahasa manusia sebelum jadi kode
Body loop   = semua kode yang ada di dalam while (yang diindent)
```