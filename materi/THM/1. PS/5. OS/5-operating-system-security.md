```
=== OS Security - Resume Materi ===
[13 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DEFINISI DASAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hardware  = Semua komponen fisik komputer yang bisa disentuh
            Contoh : CPU, RAM, HDD/SSD, keyboard, layar, printer
OS        = Lapisan antara hardware dan program/aplikasi
            Tanpa OS → hardware tidak bisa dijalankan program apapun
Software  = Dibagi 2 :
            - Programs : Firefox, Chrome, WhatsApp, MS Office
            - OS       : Windows, macOS, Android, iOS, Linux

Analogi   : Hardware = dapur restoran
            OS       = kepala chef yang atur siapa boleh masuk dapur
            Program  = pelayan yang pesan lewat chef, tidak masuk dapur langsung

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 JENIS OS BERDASARKAN FUNGSI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Desktop/Laptop  : Windows 11, macOS
Smartphone      : Android, iOS
Server          : Windows Server 2022, IBM AIX, Oracle Solaris
Universal       : Linux (bisa desktop & server)

Market Share    : Android 39.4% | Windows 32.1% | iOS 17.6%
                  OSX 6.7%      | Unknown 1.7%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CIA TRIAD (3 PILAR KEAMANAN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Confidentiality = Informasi hanya boleh diakses oleh orang yang berhak
Integrity       = Tidak ada yang bisa merusak/mengubah file tanpa izin
Availability    = Sistem harus bisa diakses kapanpun dibutuhkan pemiliknya

Analogi  : 3 kunci brankas mewah
           C = hanya orang tepat yang bisa buka
           I = isi tidak bisa diubah diam-diam
           A = brankas tidak bisa dikunci oleh orang lain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 3 KELEMAHAN UTAMA YANG DIINCAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Authentication & Weak Passwords
2. Weak File Permissions
3. Malicious Programs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 AUTHENTICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Proses verifikasi identitas di sistem lokal/remote

3 Cara Auth :
  Something you know → password, PIN
  Something you are  → sidik jari, wajah
  Something you have → nomor HP (OTP/SMS)

Password Lemah Yang Sering Dipakai (Top 20 NCSC) :
  1. 123456       6. 12345678    11. 1234567890  16. 1q2w3e4r5t
  2. 123456789    7. abc123      12. 123123      17. qwertyuiop
  3. qwerty       8. 1234567     13. 000000      18. 123
  4. password     9. password1   14. iloveyou    19. monkey
  5. 111111      10. 12345       15. 1234        20. dragon

Pola berbahaya yang sering dipakai :
  - Urutan angka     : 123, 1234, 12345, dst
  - Kata kamus       : password, iloveyou, monkey, dragon
  - Pola keyboard    : qwerty, qwertyuiop, 1q2w3e4r5t
    → Terlihat kompleks tapi SANGAT mudah ditebak!

WAJIB : Pakai password kompleks + password BERBEDA di setiap akun

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WEAK FILE PERMISSIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prinsip   : Least Privilege = "siapa boleh akses apa?"
            Setiap orang hanya boleh akses file yang mereka BUTUHKAN

Bahaya izin lemah :
  → Serang Confidentiality : akses file yang tidak seharusnya bisa dilihat
  → Serang Integrity       : modifikasi file yang tidak seharusnya bisa diedit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MALICIOUS PROGRAMS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Trojan Horse → Serang C & I
               Beri akses penyerang ke sistem
               Bisa baca & modifikasi file korban

Ransomware   → Serang Availability
               Enkripsi file korban → tidak bisa dibaca tanpa password
               Minta "ransom" (tebusan) untuk kembalikan akses
               Dekripsi = proses membalik enkripsi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERINTAH LINUX DASAR (LAB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
whoami                  → Tampilkan nama user yang sedang login
ssh USER@IP             → Remote login ke mesin lain via SSH
ls                      → List semua file di direktori saat ini
cat FILENAME            → Tampilkan isi file teks ke layar
history                 → Tampilkan semua perintah yang pernah diketik user
su - USERNAME           → Ganti ke akun user lain (Switch User)
su - root               → Ganti ke akun root (admin penuh)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 AKUN ADMINISTRATOR SISTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
root          = akun admin di Linux, Android, Apple
administrator = akun admin di Windows
Keduanya      = akses penuh TANPA BATAS ke seluruh sistem

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CELAH HISTORY COMMAND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bahaya    : Kalau user salah ketik password sebagai perintah biasa
            → password tersimpan permanen di history!
Contoh    : Johnny ketik happyHack!NG di baris perintah
            → password root bocor, bisa dilihat siapapun yang login ke akunnya
Pelajaran : Jangan pakai password lemah (abc123) + hati-hati saat ketik password

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CATATAN SSH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Koneksi pertama ke server → sistem minta konfirmasi (yes/no)
- Saat ketik password via SSH → TIDAK ada indikator di layar (bintang/titik)
  Tapi sistem tetap menerima input password yang diketik
- Setelah login akun orang lain → bisa jalankan history milik mereka

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Encryption    = proses acak file jadi tidak terbaca tanpa key
Decryption    = proses membalik enkripsi agar file bisa dibaca kembali
Least Privilege = prinsip akses minimum sesuai kebutuhan
Root / Admin  = akun dengan akses penuh tanpa batas di sistem
Authentication= proses verifikasi identitas pengguna
Malware       = program berbahaya (Trojan, Ransomware, Virus, dll)
SSH           = Secure Shell, protokol remote login ke sistem lain
```