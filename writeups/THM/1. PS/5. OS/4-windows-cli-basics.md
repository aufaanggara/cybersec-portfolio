```
=== Windows CLI Basics - Resume Materi ===
[12 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU WINDOWS COMMAND PROMPT (CMD)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Antarmuka berbasis teks untuk berinteraksi dengan Windows OS
Cara     : Ketik perintah → komputer langsung eksekusi
Kenapa   : Lebih cepat, lebih kontrol, banyak security tools hanya jalan di CLI
Analogi  : Berbicara langsung ke otak komputer tanpa perantara klik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NAVIGASI FILESYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Struktur : Windows pakai drive letter → C:\Users\NamaUser\...
           Berbeda dengan Linux yang pakai /home/user/...

PERINTAH NAVIGASI :
  cd              → cek lokasi direktori saat ini (tanpa argumen)
  cd folder_name  → masuk ke folder tertentu
  cd ..           → kembali satu level ke atas
  dir             → tampilkan isi folder (file & folder yang terlihat)
  dir /a          → tampilkan SEMUA isi termasuk yang tersembunyi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SWITCH & FUNGSINYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
dir /a          → tampilkan semua file termasuk hidden
                  /a = all attributes
dir /s nama.txt → cari file di semua subfolder dari lokasi saat ini
                  /s = subdirectories (rekursif ke bawah)

Contoh kombinasi :
  dir /s task_brief.txt  → cari file task_brief.txt di seluruh subfolder

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MEMBACA FILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
type nama_file  → cetak isi file langsung di terminal
Contoh : type task_brief.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR MENEMUKAN FILE YANG TIDAK DIKETAHUI LOKASINYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. cd           → cek posisi sekarang (pastikan di user folder)
2. dir          → lihat isi folder saat ini
3. dir /a       → cek apakah ada file/folder tersembunyi
4. dir /s nama  → biarkan Windows cari file di semua subfolder
5. cd <path>    → navigasi ke folder tempat file ditemukan
6. dir          → konfirmasi file ada di folder ini
7. type nama    → baca isi file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 INFORMASI SISTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
whoami      → tampilkan username akun yang sedang login
              Kenapa penting : user berbeda = permission berbeda

hostname    → tampilkan nama komputer
              Kenapa penting : identifikasi mesin dalam jaringan

systeminfo  → tampilkan detail lengkap OS & hardware
              Fokus pada :
              - OS Name    = nama sistem operasi
              - OS Version = versi spesifik Windows
              - System Type = 32-bit atau 64-bit

ipconfig    → tampilkan konfigurasi jaringan
              Cari :
              - IPv4 Address   = alamat IP mesin ini
              - Default Gateway = pintu keluar ke jaringan luar
              - Subnet Mask    = batas jaringan lokal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HIDDEN FILES — PENTING!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hidden ≠ Rahasia → Windows sembunyikan secara default, bukan dikunci
Cara lihat : dir /a
Contoh     : folder AppData, .logs, .research tidak muncul di dir biasa
Fakta      : dari 16 folder di dir biasa → bisa jadi 28+ setelah dir /a

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TABEL RINGKAS SEMUA PERINTAH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERINTAH              FUNGSI
─────────────────────────────────────
cd                  → cek direktori saat ini
cd folder_name      → masuk ke folder
cd ..               → naik satu level ke atas
dir                 → lihat isi folder (visible)
dir /a              → lihat isi folder (semua + hidden)
dir /s nama_file    → cari file di semua subfolder
type nama_file      → baca isi file
whoami              → siapa user yang login
hostname            → nama komputer ini
systeminfo          → info lengkap OS & hardware
ipconfig            → info konfigurasi jaringan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Directory      = folder dalam struktur filesystem
Path           = alamat lengkap lokasi file/folder
               Contoh : C:\Users\Administrator\Documents\Notes
Hidden File    = file yang disembunyikan Windows secara default
Drive Letter   = penanda partisi di Windows (C:, D:, dll)
IPv4 Address   = alamat unik mesin dalam jaringan (format: 10.x.x.x)
Default Gateway= IP router / pintu keluar dari jaringan lokal
Switch/Flag    = tambahan pada perintah untuk ubah perilaku (contoh: /a /s)
Subfolder      = folder di dalam folder lain (nested)
Permissions    = hak akses yang dimiliki user tertentu di sistem
```