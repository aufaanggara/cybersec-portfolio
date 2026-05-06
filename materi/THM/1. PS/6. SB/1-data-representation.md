```
=== Representing Colors & Numbers - Resume Materi ===
[26 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SISTEM BILANGAN — RINGKASAN UTAMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Desimal     → Basis 10  | Digit : 0–9        | Digunakan manusia sehari-hari
Biner       → Basis 2   | Digit : 0–1        | Bahasa dasar komputer
Heksadesimal→ Basis 16  | Digit : 0–9 & A–F  | Representasi ringkas biner
Oktal       → Basis 8   | Digit : 0–7        | Jarang dipakai, mengelompok 3 bit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KENAPA KOMPUTER PAKAI BINER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Transistor hanya punya 2 kondisi fisik :
  Low voltage (0–0.8V)   → 0
  High voltage (2–3.3V)  → 1
Contoh lain :
  Polaritas magnet  → North/South  (hard disk)
  Ada/tidaknya cahaya → on/off     (fiber optics)
Kesimpulan : semua data di komputer = kombinasi 0 dan 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP BIT & BYTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bit    = Binary digit → nilai 0 atau 1 (unit terkecil data)
Byte   = 8 bit → bisa disebut juga OCTET
1 bit  → 2 kondisi  (2¹)
8 bit  → 256 kondisi (2⁸) → inilah kenapa satu channel warna = 0–255

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA KONVERSI BINER → DESIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nilai posisi dari kanan ke kiri (dobel terus) :
  Posisi : 7    6    5    4    3    2    1    0
  Nilai  : 128  64   32   16   8    4    2    1

Rumus   : tiap bit dikali nilai posisinya, lalu dijumlah
Aturan  : bit = 1 → nilai IKUT dijumlah
          bit = 0 → nilai DIABAIKAN

Contoh 10111100 :
  128+0+32+16+8+4+0+0 = 188 ✅

Contoh soal hafalan :
  0000 = 0   |  1000 = 8
  0001 = 1   |  1001 = 9
  0010 = 2   |  1010 = 10
  0011 = 3   |  1011 = 11
  0100 = 4   |  1100 = 12
  0101 = 5   |  1101 = 13
  0110 = 6   |  1110 = 14
  0111 = 7   |  1111 = 15

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA KONVERSI DESIMAL → HEKSADESIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0–9   → sama persis dengan desimal
10=A  11=B  12=C  13=D  14=E  15=F

Hafalan cepat : "After 9 → A B C D E F = 10 11 12 13 14 15"

4 bit = 1 digit hex
8 bit (1 byte) = 2 digit hex

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA KONVERSI HEKSADESIMAL → DESIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sama seperti biner, tapi pangkat 16

Rumus : tiap digit × 16^posisi (dari kanan mulai 0)

Contoh 9BDF :
  9×16³ + 11×16² + 13×16¹ + 15×16⁰
= 9×4096 + 11×256 + 13×16 + 15×1
= 36864 + 2816 + 208 + 15
= 39.903 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA KONVERSI OKTAL → DESIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sama seperti biner/hex, tapi pangkat 8
3 bit = 1 digit oktal

Contoh 357 :
  3×8² + 5×8¹ + 7×8⁰
= 3×64 + 5×8 + 7×1
= 192 + 40 + 7
= 239 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REPRESENTASI WARNA DI KOMPUTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Model warna : RGB (Red, Green, Blue)
Setiap warna dikontrol intensitasnya → seperti 3 kenop/lampu

8 Warna (3 bit) — tiap lampu hanya ON/OFF :
  000 = Hitam  |  100 = Merah
  001 = Biru   |  011 = Cyan
  010 = Hijau  |  101 = Magenta
  110 = Kuning |  111 = Putih
  Rumus : 2×2×2 = 2³ = 8 warna

16 Juta Warna (24 bit) — tiap channel 256 level :
  256×256×256 = 16.777.216 warna
  Rumus       : 3 channel × 8 bit = 24 bit = 3 byte
  Tiap byte   : 2 digit hex → total 6 digit hex

Contoh warna hex BC002D :
  BC  = Red   = 188 (desimal) = 10111100 (biner)
  00  = Green = 0   (desimal) = 00000000 (biner)
  2D  = Blue  = 45  (desimal) = 00101101 (biner)
  Hasil = warna merah tua/gelap

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 POLA BINER YANG PERLU DIINGAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bit paling kanan  → selang-seling  0,1,0,1,0,1...
Bit kedua kanan   → dua-dua        0,0,1,1,0,0,1,1...
Bit ketiga kanan  → empat-empat    0,0,0,0,1,1,1,1...
Bit paling kiri   → delapan-delapan 0×8 lalu 1×8...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bit          = Binary digit, nilai 0 atau 1
Byte / Octet = 8 bit
Basis        = jumlah digit yang digunakan sistem bilangan
RGB          = Red Green Blue, model warna komputer
Hex Color    = kode warna 6 digit hex (contoh: #FF5733)
True Color   = 24 bit color = 16 juta warna
Channel      = satu komponen warna (R atau G atau B)
Intensity    = tingkat kecerahan/kekuatan warna (0–255)
```