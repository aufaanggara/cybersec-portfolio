```
=== Burp Suite Intruder - Resume Materi ===
[10 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU INTRUDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Modul fuzzing bawaan Burp Suite untuk otomasi
           request dengan variasi input secara berulang
Fungsi   : Brute-force login, fuzzing endpoint/subdomain,
           credential stuffing, IDOR enumeration
Setara   : Wfuzz / ffuf (tapi lebih lambat di Community Edition)
Limit    : Community Edition = RATE LIMITED → lambat
           → untuk pentest nyata lebih baik pakai ffuf/Hydra

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBEDAAN FUZZING VS BRUTE-FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fuzzing      → Kirim input aneh/acak untuk PANCING reaksi error
               Tujuan : temukan bug/celah/perilaku tak terduga
               Contoh : kirim karakter spesial ke form input

Brute-force  → Coba SEMUA kemungkinan nilai secara sistematis
               Tujuan : temukan nilai yang BENAR (password, token)
               Contoh : coba 0000 sampai 9999 di PIN

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 4 SUB-TAB / PANEL INTRUDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Positions    → Tandai bagian request yang akan diganti payload
               Tombol : Add § / Clear § / Auto §
               Penanda posisi : tanda § (section mark)

Payloads     → Isi daftar nilai yang akan dicobakan ke posisi
               Terdiri dari 4 bagian :
               1. Payload Sets    → pilih posisi & tipe payload
               2. Payload Settings → isi daftar (load/paste/add)
               3. Payload Processing → aturan pra-proses payload
               4. Payload Encoding → URL encode karakter tertentu

Resource Pool→ Alokasi resource (hanya berguna di Pro Edition)

Settings     → Atur perilaku serangan & handling hasil

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PAYLOAD PROCESSING - ATURAN PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Add prefix   → Tambah karakter di DEPAN setiap payload
Add suffix   → Tambah karakter di BELAKANG setiap payload
Match/Replace→ Ganti pola tertentu dalam payload
Skip if match→ Lewati payload yang cocok regex tertentu
Capitalize   → Ubah huruf pertama jadi kapital

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 4 TIPE SERANGAN INTRUDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. SNIPER ← DEFAULT & PALING UMUM
   Cara   : 1 payload set, dicoba ke setiap posisi BERGANTIAN
   Rumus  : requests = jumlahPayload × jumlahPosisi
   Cocok  : single-position attack, password brute-force,
             fuzzing 1 parameter
   Contoh : pos=2, payload=3 kata → 6 request total

2. BATTERING RAM
   Cara   : 1 payload set, payload SAMA dikirim ke SEMUA posisi
             SERENTAK dalam 1 request
   Rumus  : requests = jumlahPayload (tidak dikali posisi)
   Cocok  : race condition, test payload identik di banyak posisi
   Contoh : pos=2, payload=3 kata → 3 request total

3. PITCHFORK
   Cara   : Banyak payload set (maks 20), masing-masing untuk
             1 posisi, diiterasi BERSAMAAN (sejajar)
   Rumus  : requests = panjang wordlist TERPENDEK
   Cocok  : credential stuffing (username:password sudah dipasangkan)
   PENTING: Berhenti saat wordlist terpendek habis
   Contoh : usr[joel,harriet,alex] + pw[J03l,Emma1815,Sk1ll]
             → 3 request (joel:J03l, harriet:Emma1815, alex:Sk1ll)

4. CLUSTER BOMB
   Cara   : Banyak payload set (maks 20), uji SEMUA KOMBINASI
             dari setiap payload set
   Rumus  : requests = payload1 × payload2 × ... (perkalian semua)
   Cocok  : credential brute-force saat mapping user:pass TIDAK diketahui
   WARNING: Traffic sangat besar! Hati-hati dengan set besar
   Contoh : usr=3 kata, pw=3 kata → 9 request (semua kombinasi)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN 4 TIPE SERANGAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tipe           Payload Set   Cara Kerja        Request
Sniper         1             Bergantian        payload × posisi
Battering Ram  1             Serentak semua    = jumlah payload
Pitchfork      Banyak(≤20)   Sejajar bersama   = wordlist terpendek
Cluster Bomb   Banyak(≤20)   Semua kombinasi   = perkalian semua set

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MEMBACA HASIL SERANGAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status Code  → Sering SAMA semua (302), tidak bisa jadi patokan
Length       → KUNCI utama! Yang BERBEDA dari mayoritas = anomali

Brute-force login :
  Gagal  → halaman error/login panjang → Length BESAR
  Berhasil → redirect ke dashboard singkat → Length KECIL

IDOR enumeration :
  Tidak ada → halaman 404 singkat → Length KECIL
  Ada isinya → halaman tiket/data lengkap → Length BESAR

Kesimpulan : selalu klik header Length untuk sort, cari yang BEDA sendiri

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CREDENTIAL STUFFING VS BRUTE-FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Brute-force       → Coba semua kombinasi tanpa tahu mapping
                    Tool : Cluster Bomb / Hydra
Credential stuff. → Pakai pasangan user:pass dari data bocoran
                    Tool : Pitchfork (lebih cepat & efisien)
                    Alasan efisien : request = jumlah pasangan saja

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 IDOR (INSECURE DIRECT OBJECT REFERENCE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Kerentanan akses kontrol — user bisa akses resource
           milik user lain hanya dengan ganti angka/ID di URL
Contoh   : /support/ticket/6 → ganti jadi /ticket/1, /ticket/2 dst
Deteksi  : Gunakan Intruder Sniper + payload type Numbers
Tanda    : Status 200 + Length lebih besar dari yang 404
Bahaya   : Bisa baca semua data user lain tanpa izin

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BURP MACROS (BYPASS CSRF TOKEN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Masalah  : CSRF token + session cookie berubah setiap request
           → Intruder biasa GAGAL karena token kadaluarsa
Solusi   : Burp Macro → jalankan GET request otomatis sebelum
           setiap request Intruder untuk ambil token baru

Cara setup :
  Settings → Sessions → Macros → Add
  → Pilih GET request ke halaman login dari history
  → Beri nama macro → OK

  Sessions → Session Handling Rules → Add
  → Tab Scope : centang HANYA Intruder
  → URL Scope : Use suite scope / custom scope (masukkan IP target)
  → Tab Details → Rule Actions → Add → Run a Macro
  → Pilih macro tadi
  → Update only parameters : loginToken
  → Update only cookies    : session
  → OK

Tanda berhasil : semua response = 302 (bukan 403)
Tanda gagal    : muncul 403 = macro tidak bekerja

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TOOL TERMINAL ALTERNATIF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ffuf    → Fuzzing web (direktori, endpoint, parameter, subdomain)
          Cepat, fleksibel, paling populer untuk web fuzzing
Hydra   → Spesialis brute-force login (HTTP, SSH, FTP, RDP, dll)
          Pilihan utama untuk credential attack ke form login
Gobuster→ Directory & subdomain fuzzing, simpel & cepat
wget    → Download file dari URL lewat terminal
          Flag penting :
          -O  → tentukan nama file output
          -P  → tentukan folder tujuan
          -r  → download rekursif
          -q  → mode senyap (no output)
          -c  → lanjut unduhan yang terputus
          --no-check-certificate → abaikan SSL

unzip   → Ekstrak file zip
          unzip file.zip          → ekstrak di direktori saat ini
          unzip file.zip -d folder → ekstrak ke folder tertentu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Payload          = nilai/data yang disisipkan ke posisi target
Wordlist         = daftar kata/nilai yang dipakai sebagai payload
Section mark §   = penanda posisi di request Intruder
Rate limiting    = pembatasan kecepatan request (di Community Ed.)
CSRF token       = token anti-pemalsuan request yang berubah tiap sesi
Session cookie   = cookie penanda sesi login yang aktif
Credential stuff = serangan pakai pasangan user:pass dari data bocoran
IDOR             = bug akses kontrol via manipulasi ID di URL
Macro            = serangkaian aksi otomatis yang dijalankan berulang
302 Redirect     = response server yang redirect ke halaman lain
403 Forbidden    = akses ditolak (sering tanda macro gagal)
404 Not Found    = resource tidak ditemukan
```