```
=== Encoding Karakter - Resume Materi ===
[26 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP DASAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Representasi : Data hidup sebagai bits & angka di memori komputer
Encoding     : Kesepakatan (mapping) antara angka dan maknanya
               Contoh : angka 65 → karakter "A"
Gibberish    : Terjadi saat file disimpan & dibuka dengan encoding BERBEDA
Analogi      : Encoding = kamus dwibahasa antara teks & kode numerik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ASCII
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kepanjangan : American Standard Code for Information Interchange
Tahun       : 1963
Bit         : 7 bit
Range       : 0 - 127 (128 karakter total)
Isi         : Huruf Inggris, digit, tanda baca, control characters
Sifat       : "A" = American → hanya cover bahasa Inggris

ANGKA PENTING YANG WAJIB HAPAL :
  48  = '0'  (digit nol)
  57  = '9'  (digit sembilan)
  65  = 'A'  (uppercase A)
  90  = 'Z'  (uppercase Z)
  97  = 'a'  (lowercase a)
  122 = 'z'  (lowercase z)
  127 = DEL  (delete)
  7   = BEL  (bell / bunyi ting di terminal)
  10  = LF   (\n / new line)
  13  = CR   (carriage return)

POLA PENTING :
  Huruf berurutan → tahu 'A'=65, maka 'B'=66, 'C'=67, dst
  Uppercase A-Z   → hex 41 sampai 5A
  Lowercase a-z   → hex 61 sampai 7A
  Selisih A vs a  → beda 32 (decimal) / 20 (hex)
  Karakter '[' = hex 5B

CONTOH "TryHackMe" dalam ASCII :
  Hex     : 54 72 79 48 61 63 6b 4d 65 0a
  Decimal : 124 162 171 110 141 143 153 115 145 012
  Binary  : 01010100 01110010 01111001 01001000
            01100001 01000011 01101011 01001101
            01100101 00001010
  → 0a / 00001010 = \n (new line / Enter)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 EXTENDED ASCII & MASALAHNYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Solusi awal : Tambah bit ke-8 → 128 karakter ekstra
Standar yg ada :
  ISO-8859-1 (Latin-1) → Eropa Barat
                          German(ß,ü) French(é,ç) Spanish(ñ,¿)
                          Italian, Portuguese, Nordic (ð/Ð)
  ISO-8859-2 (Latin-2) → Eropa Tengah/Timur
                          Polish(ł,ń) Czech(č,ř) Hungarian(ő,ű)
                          Croatian(đ) Romanian(ș,ț) Slovak
  Windows-1252         → Standar Microsoft (regional)

MASALAH : File disimpan ISO-8859-1, dibuka ISO-8859-2
          → karakter 'ø' tampil sebagai 'ř' (gibberish!)
AKAR MASALAH : 128 karakter ekstra TIDAK CUKUP untuk semua bahasa

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SKALA KEBUTUHAN KARAKTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Inggris  →    52 karakter (A-Z + a-z)
Arab     →   250+ karakter (ligatur & diakritik)
Jepang   → 2.136 Kanji (sehari-hari, ditetapkan Kemendikbud Jepang)
             6.879 karakter (standar JIS X 0208)
Cina     → ~8.000 karakter (dikenal orang terpelajar)
            87.887 Hanzi (standar GB 18030-2022)
+ Emoji  → belum dihitung!
→ Kesimpulan : butuh standar UNIVERSAL = Unicode

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 UNICODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Standar encoding karakter universal
            Menetapkan code point unik untuk SETIAP karakter
            dari semua sistem penulisan modern & historis dunia
Versi     : Unicode 17.0 (terbaru)
Jumlah    : ~157.000 karakter, ~4.000 di antaranya emoji sequences
Format    : U+[KODE HEX]

CODE POINT PENTING HAPAL :
  U+0041 = Latin "A"
  U+03A9 = Greek "Ω"
  U+3042 = Japanese Hiragana "あ"
  U+9F8D = Chinese "龍" (dragon) → UTF-16
  U+1F60A= Emoji 😊 (smiley face)
  U+30C4 = Japanese "ツ" (tsu) → UTF-16
  U+062A = Arabic "ت" (taa)
  U+265E = ♞ (black knight catur)
  U+1F525= Emoji 🔥 → 4 bytes di UTF-8

KEUNGGULAN UNICODE :
  ✓ Tidak perlu pilih encoding spesifik per bahasa
  ✓ Bisa pakai banyak bahasa dalam 1 file/pesan
  ✓ Semua orang pakai standar yang sama
  ✓ Tidak khawatir encoding penulis asli

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 UTF-8, UTF-16, UTF-32
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Catatan : Ketiganya merepresentasikan Unicode yang SAMA
          Perbedaan hanya cara penyimpanan bytes-nya

UTF-8  : Dinamis 1-4 bytes per karakter
         Paling UMUM di web modern
         U+0000 - U+007F  → 1 byte (identik ASCII) ← backward compatible!
         Non-ASCII (Ω)    → 2 bytes
         Emoji/kompleks   → 4 bytes
         Keunggulan : EFISIEN, tidak buang bytes

UTF-16 : 2 atau 4 bytes per karakter
         Karakter umum (Latin, Cyrillic, Hanzi) → 2 bytes
         Karakter langka (emoji, ancient scripts) → 4 bytes
                         (sepasang 16-bit unit)
         Contoh : 'A' = U+0041
                  🔥  = U+D83D U+DD25 (surrogate pair)

UTF-32 : Selalu tepat 4 bytes per karakter
         Paling SIMPEL tapi paling BOROS memori
         Contoh : 'A' = U+00000041
                  🔥  = U+0001F525

PERBANDINGAN CEPAT :
  ┌─────────┬──────────┬────────────┬──────────────┐
  │         │  Bytes   │  Efisiensi │  Penggunaan  │
  ├─────────┼──────────┼────────────┼──────────────┤
  │ UTF-8   │  1-4 (D) │  Terbaik   │  Web/Internet│
  │ UTF-16  │  2 atau 4│  Seimbang  │  OS/Windows  │
  │ UTF-32  │  Selalu 4│  Terburuk  │  Internal    │
  └─────────┴──────────┴────────────┴──────────────┘
  D = Dinamis

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CONTOH UNIK & MENARIK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
龍 U+9F8D   → "Dragon" → muncul di distro Kali Linux
😊 U+1F60A  → binary: 0000 0000 0000 0001 1111 0110 0000 1010
ツ U+30C4   → huruf Jepang "tsu", dipakai sebagai smiley
ت U+062A   → huruf Arab "taa", dipakai sebagai smiley
♞ U+265E   → black knight catur
             binary: 0010 0110 0101 1110

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Encoding        = Kesepakatan mapping angka ↔ karakter
Code Point      = Angka unik yang ditetapkan Unicode untuk 1 karakter
Character Set   = Kumpulan karakter dengan nomor uniknya
Gibberish       = Karakter acak akibat encoding berbeda
Backward Compat = UTF-8 kompatibel penuh dengan ASCII lama
Control Char    = Karakter tak terlihat (BEL, LF, CR, DEL, dll)
Ligature        = Gabungan dua huruf jadi satu simbol (banyak di Arab)
Diacritic       = Tanda tambahan pada huruf (é, ñ, ü, dll)
Surrogate Pair  = Dua unit 16-bit yang dipasangkan di UTF-16
                  untuk karakter di luar BMP (emoji, dll)
BMP             = Basic Multilingual Plane (U+0000 - U+FFFF)
```