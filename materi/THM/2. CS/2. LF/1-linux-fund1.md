```
=== Linux Fundamentals Part 1 - Resume Materi ===
[23 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU LINUX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Sistem operasi open-source berbasis UNIX
Sifat    : Ringan, efisien, fleksibel
Digunakan: Website, server perusahaan, mobil pintar, Android,
           superkomputer, IoT, infrastruktur kritis
Fakta    : Ubuntu Server bisa jalan dengan RAM hanya 512MB

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DISTRIBUSI LINUX (FLAVOURS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Konsep   : "Linux" = istilah payung untuk banyak OS berbasis UNIX
Ubuntu   : Distribusi paling populer, cocok untuk server & desktop
Debian   : Base dari Ubuntu, sangat stabil
Analogi  : Seperti Windows punya versi 7/8/10, Linux punya banyak distro
Sifat    : Open-source → siapa pun bisa modifikasi sesuai kebutuhan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TERMINAL & SHELL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Terminal : Antarmuka berbasis teks untuk berinteraksi dengan Linux
Tampilan : tryhackme@linux1:~$ ← ini namanya "prompt"
Kenapa   : Karena Linux sangat ringan, sering tidak ada GUI
           (Graphical User Interface)
Mindset  : Awalnya intimidating, tapi cepat terbiasa setelah praktik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERINTAH DASAR - OUTPUT & INFO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo        → Menampilkan teks ke layar
              Contoh : echo Hello
              Catatan: Pakai quotes jika ada spasi → echo "Hello Friend!"

whoami      → Cek username yang sedang login saat ini
              Contoh : whoami
              Output : tryhackme

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NAVIGASI FILESYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ls          → Listing - lihat isi folder saat ini
              Contoh : ls
              Output : Desktop Documents Pictures
              Trick  : ls Pictures → langsung lihat isi folder Pictures

cd          → Change Directory - pindah ke folder lain
              Contoh : cd Pictures
              Efek   : Sekarang berada di dalam folder Pictures

pwd         → Print Working Directory - cek posisi folder saat ini
              Contoh : pwd
              Output : /home/ubuntu/Documents
              Fungsi : Agar tidak tersesat di filesystem

cat         → Concatenate - baca isi file teks
              Contoh : cat todo.txt
              Output : Isi dari file todo.txt
              Trick  : cat /home/ubuntu/Documents/todo.txt
                       → baca file tanpa pindah folder

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PENCARIAN FILE & KONTEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
find        → Cari FILE berdasarkan nama
              Syntax : find -name namafile
              Contoh : find -name passwords.txt
              Output : ./folder1/passwords.txt

              Wildcard (*) untuk cari semua file dengan ekstensi tertentu
              Contoh : find -name *.txt
              Output : Semua file .txt di seluruh sistem

grep        → Cari KONTEN di dalam file
              Syntax : grep "keyword" namafile
              Contoh : grep "81.143.211.90" access.log
              Fungsi : Langsung tampilkan baris yang mengandung keyword

grep -R     → Cari konten di SEMUA file & subfolder (recursive)
              Syntax : grep -R "keyword" /path/
              Contoh : grep -R "PRETTY_NAME" /etc/
              Output : /etc/os-release:PRETTY_NAME="Ubuntu"
              Fungsi : Cari di banyak file sekaligus tanpa manual satu-satu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SHELL OPERATORS - POWER UP COMMAND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
&           → Background - jalankan perintah di latar belakang
              Contoh : cp largefile.zip backup/ &
              Fungsi : Terminal tidak terkunci, bisa jalankan perintah lain

&&          → Combine - gabung beberapa perintah dalam satu baris
              Syntax : command1 && command2
              Aturan : command2 HANYA jalan kalau command1 BERHASIL
              Contoh : apt update && apt upgrade

>           → Redirect (Replace) - arahkan output ke file (GANTI isi)
              Syntax : command > namafile
              Contoh : echo hey > welcome
              Efek   : File welcome berisi "hey" (isi lama HILANG)

>>          → Redirect (Append) - arahkan output ke file (TAMBAH di bawah)
              Syntax : command >> namafile
              Contoh : echo hello >> welcome
              Efek   : File welcome sekarang berisi:
                       hey
                       hello

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBEDAAN > vs >>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
>  (Single) → MENGGANTI seluruh isi file dengan output baru
               File lama = HILANG

>> (Double)  → MENAMBAHKAN output di BAWAH isi yang sudah ada
               File lama = TETAP ADA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Terminal        = Antarmuka teks untuk berinteraksi dengan sistem
Shell           = Program yang memproses perintah di terminal
Prompt          = Tanda terminal siap menerima perintah (tryhackme@linux1:~$)
Filesystem      = Struktur organisasi file & folder di sistem
Path            = Alamat lengkap lokasi file/folder (misal: /home/ubuntu/Documents)
Working Dir     = Folder tempat kamu berada saat ini
Redirect        = Mengalihkan output perintah ke file atau tempat lain
Wildcard (*)    = Simbol untuk merepresentasikan "apa saja" dalam pencarian
Recursive       = Proses yang mencari/memproses termasuk semua subfolder
Background      = Proses berjalan tanpa mengunci terminal
Concatenate     = Menggabungkan/menampilkan isi file
Command         = Perintah yang diketik di terminal
Flag/Switch     = Opsi tambahan pada perintah (misal: -R pada grep)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 QUICK REFERENCE - CHEAT SHEET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFORMASI:
  whoami              → Siapa user yang login
  pwd                 → Di folder mana sekarang

NAVIGASI:
  ls                  → Lihat isi folder
  ls namaFolder       → Lihat isi folder tertentu tanpa masuk
  cd namaFolder       → Masuk ke folder
  cd ..               → Keluar ke folder parent

BACA FILE:
  cat namafile        → Tampilkan isi file

CARI FILE:
  find -name file     → Cari file spesifik
  find -name *.txt    → Cari semua file .txt

CARI KONTEN:
  grep "kata" file    → Cari kata dalam file
  grep -R "kata" /dir → Cari kata di semua file dalam direktori

OUTPUT:
  echo teks           → Tampilkan teks
  echo "teks" > file  → Simpan teks ke file (ganti)
  echo "teks" >> file → Tambah teks ke file

OPERATORS:
  cmd &               → Jalankan di background
  cmd1 && cmd2        → Jalankan cmd2 jika cmd1 sukses
  cmd > file          → Redirect output (replace)
  cmd >> file         → Redirect output (append)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIPS & BEST PRACTICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Gunakan TAB untuk auto-complete nama file/folder
✓ Panah atas/bawah untuk akses command history
✓ Selalu pwd kalau merasa tersesat
✓ Hati-hati dengan > (bisa hapus file penting kalau salah)
✓ Latihan rutin agar command jadi muscle memory
✓ Case-sensitive → "File.txt" ≠ "file.txt"
✓ Kombinasikan perintah dengan operator untuk efisiensi maksimal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NEXT STEP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Praktik semua command sampai lancar
→ Lanjut ke Linux Fundamentals Part 2
→ Eksplorasi lebih dalam tentang permission, user management, scripting
```