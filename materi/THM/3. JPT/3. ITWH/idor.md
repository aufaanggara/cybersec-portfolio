```
=== IDOR (Insecure Direct Object Reference) - Resume Materi ===
[08 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU IDOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Kerentanan access control saat server menerima input user
           untuk mengakses objek (file, data, dokumen) TANPA validasi
           apakah objek itu benar milik user yang memintanya
Penyebab : Server terlalu percaya pada input user & tidak validasi
           kepemilikan data di sisi server
Analogi  : Ganti angka di URL → bisa lihat data orang lain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CONTOH KASUS IDOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Normal   : http://online-service.thm/profile?user_id=1305 → data sendiri
Exploit  : http://online-service.thm/profile?user_id=1000 → data orang lain
Masalah  : Server tidak cek apakah user yang login = pemilik data
Solusi   : Server harus validasi kepemilikan sebelum tampilkan data

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 3 JENIS IDOR BERDASARKAN BENTUK ID
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ENCODED IDs
   → ID disembunyikan dalam bentuk encoding (paling umum = base64)
   → Karakter : a-z, A-Z, 0-9, dan = (untuk padding)
   → Cara eksploit :
     - Decode  → https://www.base64decode.org/
     - Tamper  → ubah nilai ID-nya
     - Encode  → https://www.base64encode.org/
     - Submit  → kirim ulang request
   → Contoh : eyJpZCI6MzB9 → decode → {"id":30} → ubah → {"id":10}
              → encode → eyJpZCI6MTB9 → submit → akses data orang lain

2. HASHED IDs
   → ID di-hash (contoh : md5)
   → Contoh : 123 → 202cb962ac59075b964b07152d234b70
   → Cara eksploit : masukkan hash ke https://crackstation.net/
     (database miliaran hash → value)
   → Bisa follow predictable pattern (hash dari integer)

3. UNPREDICTABLE IDs
   → ID tidak bisa ditebak/di-decode/di-crack
   → Cara eksploit : buat 2 akun → tukar ID antar akun
   → Jika akun A bisa lihat data akun B = IDOR valid

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DIMANA IDOR BISA DITEMUKAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tidak selalu di address bar! Bisa juga di :
→ AJAX request (dimuat browser di background)
→ JavaScript file (parameter direferensikan di sana)
→ Parameter tersembunyi (ada saat development, terbawa ke production)

Teknik : PARAMETER MINING
→ Endpoint /user/details terlihat normal
→ Tapi lewat parameter mining ditemukan parameter user_id
→ /user/details?user_id=123 → bisa akses data user lain
→ Cara mining : coba manual, pakai tools (Arjun/ffuf),
                baca JS file, cek request lain di Burp Suite

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR PRAKTIK LAB (ACME IT SUPPORT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Login    → buat akun di customer section
2. Your Account → lihat username & email ter-pre-filled
3. Dev Tools → tab Network → refresh → temukan request :
              /api/v1/customer?id=50
4. Response → {"id":50,"username":"aufa","email":"...@mail.ugm.ac.id"}
5. Exploit  → ganti id=50 → id=1 → id=3 di URL
6. Hasil    → dapat data username & email milik user lain = IDOR!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOLS YANG WAJIB DIKETAHUI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
base64decode.org  → decode encoded ID
base64encode.org  → encode ulang setelah dimanipulasi
crackstation.net  → crack hashed ID (database miliaran hash)
Burp Suite        → intercept & modifikasi request
Arjun / ffuf      → parameter mining otomatis
Browser Dev Tools → tab Network untuk lihat AJAX request

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IDOR             = Insecure Direct Object Reference
Access Control   = mekanisme kontrol siapa boleh akses apa
Encoding         = ubah data binary ke ASCII (BUKAN enkripsi, bisa di-decode)
Hashing          = ubah data jadi string fixed-length (satu arah)
Parameter Mining = teknik cari parameter tersembunyi di endpoint
Endpoint         = URL/path spesifik yang menerima request di server
AJAX Request     = request background yang tidak terlihat di address bar
Padding (=)      = karakter pengisi di akhir string base64
Query String     = bagian URL setelah ? (contoh: ?id=50)
Pre-filled       = kolom yang sudah terisi otomatis dari data server
```