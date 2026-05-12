```
=== Linux CLI Basics - Resume Materi ===
[12 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU LINUX CLI & TERMINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLI      : Command-Line Interface → kontrol komputer pakai TEKS
Terminal : Jendela tempat mengetik perintah CLI
Kenapa   : Lebih cepat, kontrol lebih besar, banyak security tools
           hanya bisa jalan di terminal
Linux    : OS open source, ringan, fleksibel → standar industri siber
Analogi  : Terminal = walkie-talkie langsung ke otak komputer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NAVIGASI FILESYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Perintah  Fungsi
────────  ──────────────────────────────────────
pwd       Print Working Directory → "aku sekarang di mana?"
          Output contoh : /home/ubuntu

ls        List → tampilkan isi folder saat ini
ls -l     List detail → tampilkan ukuran, izin, tanggal
ls -al    List all → tampilkan TERMASUK file tersembunyi

cd <dir>  Change Directory → masuk ke folder
          Contoh : cd Documents
cd ..     Naik satu level ke folder sebelumnya
          Contoh : dari /home/ubuntu/Documents → ke /home/ubuntu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MENCARI & MEMBACA FILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
find ~ -name <file>   Cari file berdasarkan nama mulai dari home (~)
                      Contoh : find ~ -name mission_brief.txt
                      Output : path lengkap ke file tsb
                      Catatan : ~ = simbol home directory

cat <file>            Baca & tampilkan isi file ke layar
                      Contoh : cat mission_brief.txt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 INFORMASI SISTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
whoami        Tampilkan username yang sedang login

uname         Tampilkan nama OS saja → output: Linux
uname -a      Tampilkan info LENGKAP sistem, breakdown:
              Linux      = kernel yang berjalan
              tryhackme  = hostname (nama komputer)
              x86_64     = arsitektur hardware (64-bit)
              GNU/Linux  = tipe OS (kernel + GNU tools)

df -h         Disk Filesystem human-readable → cek ruang disk
  -h          = human readable (tampil 2G bukan 2048000000)
              Breakdown output :
              /dev/root = disk utama fisik sistem
              tmpfs     = filesystem sementara di RAM
              /dev/shm  = shared memory area

cat /etc/os-release   Baca file identitas distro Linux
                      Isi : nama distro, versi, codename, URL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TENTANG FILE TERSEMBUNYI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ciri     : Nama file/folder DIAWALI dengan titik → .namafile
Tampil   : Hanya muncul saat pakai ls -al
Default  : Linux SEMBUNYIKAN otomatis, bukan berarti dikunci
Contoh   : .Xauthority  .apport-ignore.xml  .Xresources
Analogi  : Seperti laci rahasia — tidak dikunci, cuma tidak terlihat
           kalau tidak tahu harus mencari di mana

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DIREKTORI PENTING LINUX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
~           = Home directory user saat ini (/home/ubuntu)
/etc        = Folder konfigurasi & informasi sistem
              Isi : os-release, fstab, hosts, resolv.conf, dll
/dev/root   = Disk utama (root) sistem
/home       = Berisi folder home semua user

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR MISI (URUTAN LOGIS DI LAPANGAN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. pwd              → cek posisi awal
2. ls / ls -al      → lihat apa yang ada di sekitar
3. find ~ -name X   → cari file yang tidak diketahui lokasinya
4. cd <path>        → navigasi ke lokasi file
5. cat <file>       → baca isi file
6. whoami           → cek identitas user
7. uname -a         → cek info sistem & kernel
8. df -h            → cek ruang disk
9. cat /etc/os-release → cek nama & versi distro Linux

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Directory    = Folder dalam sistem Linux
Path         = Alamat lengkap lokasi file/folder di sistem
               Contoh : /home/ubuntu/Documents/file.txt
Root (/)     = Puncak dari semua filesystem Linux, titik awal
Kernel       = Inti sistem operasi, jembatan hardware & software
Hostname     = Nama komputer dalam jaringan
Distro       = Distribusi Linux (Ubuntu, Debian, Kali, dll)
Switch/Flag  = Tambahan perintah pakai - untuk ubah perilaku
               Contoh : -h di df -h, -a di ls -a, -l di ls -l
Filesystem   = Cara OS mengorganisir & menyimpan file di disk
tmpfs        = Temporary filesystem → disimpan di RAM, bukan disk
Human-readable = Format angka mudah dibaca manusia (2G vs 2048000)
```