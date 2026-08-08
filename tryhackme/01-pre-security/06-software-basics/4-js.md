```
=== JavaScript: Simple Demo - Resume Materi ===
[05 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VARIABEL & KONSTANTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
let      → Deklarasi VARIABEL, nilainya BISA berubah sepanjang program
           Contoh : let tries = 0;  /  let guess = 0;

const    → Deklarasi KONSTANTA, nilainya TIDAK BISA berubah
           Contoh : const secret = 12;

Perbedaan:
  let   = kotak yang bisa diganti isinya kapan saja
  const = kotak yang sudah disegel, tidak bisa diubah

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIPE DATA DASAR YANG DIPAKAI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Number  → Angka (bulat maupun desimal)
String  → Teks, diapit tanda kutip  "seperti ini"
Boolean → true atau false (hasil perbandingan/kondisi)
NaN     → Not a Number → hasil parseInt pada input non-angka

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FUNGSI/METHOD PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Math.random()     → Angka desimal acak antara 0 (inklusif) sampai 1 (eksklusif)
                    Contoh hasil : 0.372

Math.floor()      → Bulatkan ke bawah (hapus desimal)
                    Contoh : Math.floor(7.44) → 7

parseInt(teks,10) → Ubah teks jadi bilangan bulat basis 10
                    Contoh : parseInt("7", 10) → 7
                    Jika gagal → menghasilkan NaN

console.log()     → Tampilkan output ke layar/terminal

rl.question()     → Minta input dari pengguna (mengembalikan string)

rl.close()        → Tutup antarmuka readline setelah selesai dipakai

.test()           → Method regex untuk cek apakah teks cocok dengan pola
                    Mengembalikan true atau false

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FORMULA ANGKA ACAK DALAM RENTANG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const secret = Math.floor(Math.random() * (20)) + 1;

Breakdown :
  Math.random()     → 0 sampai 0.999...
  * 20              → 0 sampai 19.999...
  Math.floor()      → 0 sampai 19  (bulatkan bawah)
  + 1               → 1 sampai 20  (geser rentang)

Versi lebih fleksibel (v4) :
  Math.floor(Math.random() * (MAX - MIN + 1)) + MIN

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CONDITIONAL STATEMENT (if/else)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Struktur  :
  if (kondisi pertama) {
      // jalankan ini
  } else if (kondisi kedua) {
      // jalankan ini
  } else {
      // jalankan ini jika semua kondisi di atas false
  }

Sifat     : Mutually exclusive → begitu satu kondisi true,
            blok lainnya TIDAK dicek lagi

Operator perbandingan :
  <    = kurang dari
  >    = lebih dari
  ===  = sama dengan (strict)
  !==  = tidak sama dengan
  ||   = ATAU (or)
  &&   = DAN (and)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LOOP (while)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Struktur  :
  while (kondisi) {
      // terus diulang selama kondisi = true
  }

Contoh    : while (guess !== secret) { ... }
Artinya   : Terus minta tebakan selama guess belum sama dengan secret
Berhenti  : Begitu kondisi menjadi false (guess === secret)

Bahaya    : Kalau kondisi tidak pernah false → loop tak terhenti (infinite loop)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 INPUT DARI PENGGUNA (readline)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kenapa perlu library readline?
  → Node.js defaultnya tidak menunggu input user
  → Node.js dirancang untuk web server, bukan program command-line
  → Perlu library tambahan untuk memaksa Node.js menunggu

Tiga baris wajib :
  import * as readline from "node:readline/promises";
  import { stdin as input, stdout as output } from "node:process";
  const rl = readline.createInterface({ input, output });

Penjelasan :
  readline  = modul untuk tanya-jawab + tunggu jawaban
  /promises = bisa pause rapi tanpa freeze program
  stdin     = standard input (keyboard)
  stdout    = standard output (layar)
  rl        = antarmuka yang menggabungkan keduanya

await     → Hentikan eksekusi sementara sampai user merespons

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TRY / FINALLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
try {
    // kode utama dijalankan di sini
} finally {
    rl.close(); // SELALU dijalankan, apapun yang terjadi
}

try     → Jalankan kode dalam lingkungan aman (tidak crash jika error)
finally → Blok yang PASTI dijalankan di akhir, sukses maupun gagal
Fungsi  → Pastikan rl.close() selalu dipanggil agar program bersih

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VALIDASI INPUT (REGEX)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pola    : /^\d+$/
Arti per bagian :
  ^    = mulai dari awal teks
  \d   = satu karakter digit (0-9)
  +    = satu atau lebih
  $    = sampai akhir teks
  /  / = pembungkus regex di JavaScript

Penggunaan :
  if (!/^\d+$/.test(text)) {
      console.log("Please type a whole number.");
  }

Kenapa pakai ! (tanda seru)?
  .test() → true jika input ADALAH angka
  !       → balik jadi true jika input BUKAN angka
  Tujuan  → tampilkan error saat input bukan angka

Tanpa validasi (v3) → input "abc" bisa hasilkan NaN
                    → NaN !== secret → loop jalan
                    → tapi semua perbandingan false → masuk else
                    → tampilkan "You got it!" padahal salah → BUG

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 EVOLUSI VERSI PROGRAM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
v1  → Deklarasi variabel + input 1x + hitung tries
      Belum ada feedback, belum ada loop

v2  → Tambah conditional (if/else if/else)
      Ada feedback tapi hanya 1 kesempatan tebak

v3  → Tambah while loop
      Pengguna bisa tebak berkali-kali sampai benar
      Belum ada validasi input

v4  → Tambah validasi regex /^\d+$/
      Tambah konstanta MIN_NUMBER & MAX_NUMBER
      Program paling robust dan mudah dirawat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CARA MENJALANKAN DI NODE.JS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Perintah  : node namafile.js
Contoh    : node guess_v3.js
Lokasi    : /home/ubuntu/JavaScript-Demo
```