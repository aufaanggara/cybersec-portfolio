```
=== Linux Fundamentals Part 2 - Resume Materi ===
[23 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SSH (SECURE SHELL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : Protokol komunikasi terenkripsi antar dua perangkat
Fungsi   : Remote login & kontrol terminal mesin Linux jarak jauh
Cara     : Input dikirim dalam format terbaca → dienkripsi → perjalanan
           di jaringan → didekripsi saat sampai di mesin tujuan
Yang wajib ada :
  1. IP Address mesin remote
  2. Kredensial akun yang valid (username + password)

Sintaks  : ssh username@IPADDRESS
Contoh   : ssh tryhackme@10.10.10.10

CATATAN PENTING :
  → Saat ketik password di SSH, TIDAK ADA teks/simbol muncul di layar
  → Ini normal! Tetap ketik lalu tekan Enter

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FLAGS & SWITCHES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : Argumen tambahan untuk memperluas kemampuan perintah
Format   : tanda hyphen (-) diikuti huruf/kata kunci
Contoh   : ls -a  /  ls --all

Beberapa flag bisa digabung :
  ls -lh  →  -l (detail list) + -h (human-readable size)

Cara cari tahu flag sebuah perintah :
  --help  → ringkasan cepat semua opsi yang tersedia
  man     → manual lengkap (man pages) sebuah perintah

NAVIGASI MAN PAGE :
  j / ↓     = scroll satu baris ke bawah
  k / ↑     = scroll satu baris ke atas
  Space     = loncat satu halaman penuh ke bawah
  q         = keluar dari man page

Contoh penggunaan man :
  man ls    → buka manual lengkap perintah ls

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FLAG PENTING PERINTAH ls
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-a / --all        → tampilkan SEMUA file termasuk yang tersembunyi (.)
-l                → tampilkan dalam format list detail lengkap
-h                → ukuran file dalam format human-readable (K, M, G)
-lh               → gabungan -l dan -h (paling sering dipakai)

FORMAT OUTPUT ls -lh :
  -rw-r--r-- 1 cmnatic cmnatic 0 Feb 19 10:37 file1
   │          │ │       │       │ │             └─ nama file
   │          │ │       │       │ └─ tanggal modified
   │          │ │       └───────┴─ group
   │          │ └─ owner
   │          └─ jumlah hard link
   └─ permission (10 karakter)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FILE PERMISSIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Format   : rwxrwxrwx
Dibagi 3 kelompok :
  3 pertama → Owner (pemilik file)
  3 tengah  → Group
  3 terakhir→ Others (semua orang lain)

Huruf permission :
  r = read    (baca)
  w = write   (tulis/edit)
  x = execute (jalankan)
  - = tidak punya permission tersebut

KONVERSI KE ANGKA :
  r = 4
  w = 2
  x = 1
  Cara hitung : jumlahkan nilai tiap kelompok

Contoh rwxrwxrwx :
  Owner  : r+w+x = 4+2+1 = 7
  Group  : r+w+x = 4+2+1 = 7
  Others : r+w+x = 4+2+1 = 7
  Hasil  : 777

Tabel umum :
  rwxr-xr-x = 755 → Owner full, others hanya read+execute
  rw-r--r-- = 644 → Owner read/write, others hanya read
  rwx------ = 700 → Hanya owner yang punya akses

Perintah ubah permission :
  chmod 750 namafile

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERINTAH FILESYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
touch namafile        → buat file kosong baru
mkdir namafolder      → buat folder/direktori baru
cp file1 file2        → salin file1 → hasilkan file2 (asli tetap ada)
mv file1 file2        → pindah/rename (asli HILANG = seperti Cut)
mv file1 folder/      → pindahkan file1 ke dalam folder
rm namafile           → hapus file (PERMANEN, tidak ada recycle bin!)
rm -R namafolder      → hapus folder beserta seluruh isinya (recursive)
file namafile         → cek tipe/format sebuah file

PROTIP : Semua perintah di atas mendukung full path
  Contoh : cp directory1/directory2/note .

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SWITCH PENTING rm
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-R  → recursive, wajib dipakai saat hapus direktori/folder

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BERPINDAH USER (su)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sintaks  : su namauser
Yang perlu disiapkan :
  1. Nama user tujuan
  2. Password user tujuan

SWITCH PENTING su :
  -l / --login  → inherit semua properti user baru (env variables, dll)
                  sesi masuk ke home directory user TUJUAN
  (tanpa -l)    → sesi tetap di home directory user SEBELUMNYA

Contoh :
  su user2          → masuk sebagai user2, direktori tetap /home/tryhackme
  su -l user2       → masuk sebagai user2, direktori pindah ke /home/user2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DIREKTORI PENTING LINUX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/etc   → Kependekan : etcetera
         Isi       : file konfigurasi & sistem OS
         File kunci: sudoers (daftar user yg boleh sudo)
                     passwd  (daftar user sistem)
                     shadow  (password terenkripsi sha512)

/var   → Kependekan : variable data
         Isi       : data yang sering berubah/diakses aplikasi
         Subfolder : /var/log (semua log file disimpan di sini)
                     /var/opt, /var/tmp, /var/backups

/root  → Home directory khusus milik root user
         BUKAN /home/root, melainkan langsung /root
         Hanya bisa diakses oleh root

/tmp   → Kependekan : temporary
         Sifat     : VOLATILE — isi terhapus saat restart
         Akses     : semua user bisa menulis ke sini by default
         Kegunaan pentest : tempat simpan enumeration scripts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flags/Switches   = argumen tambahan pada perintah, diawali tanda -
Man Page         = manual lengkap dokumentasi sebuah perintah Linux
Hidden File      = file/folder diawali titik (.) → tersembunyi dari ls biasa
Permission       = hak akses read/write/execute pada file/folder
Owner            = user pemilik sebuah file/folder
Group            = kelompok user yang punya akses bersama ke file
Execute          = permission untuk menjalankan file sebagai program/script
Recursive (-R)   = operasi yang mencakup folder beserta seluruh isinya
Volatile         = data bersifat sementara, hilang saat sistem restart
Environment Var  = variabel konfigurasi yang aktif di sesi user tertentu
SHA512           = algoritma enkripsi yang dipakai Linux untuk simpan password
```