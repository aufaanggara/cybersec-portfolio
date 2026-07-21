```
=== Hashing Basics - Resume Materi ===
[13 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU HASH FUNCTION & HASH VALUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hash Value   : String berukuran TETAP hasil perhitungan fungsi hash
               Juga disebut : digest
Hash Function: Mengambil input SEMBARANG ukuran → output TETAP
Sifat        : - Satu arah (tidak bisa dibalik)
               - Input sama → output SELALU sama
               - 1 bit berubah → output BERUBAH TOTAL
               - Cepat dihitung, sangat lambat dibalik
Kegunaan     : 1. Penyimpanan kata sandi (autentikasi)
               2. Integrity checking (verifikasi file)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALGORITMA HASH & OUTPUT SIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MD5      : 128 bit = 16 byte = 32 karakter hex  ← TIDAK AMAN
SHA-1    : 160 bit = 20 byte = 40 karakter hex  ← TIDAK AMAN
SHA-256  : 256 bit = 32 byte = 64 karakter hex  ← AMAN
SHA-512  : 512 bit = 64 byte = 128 karakter hex ← AMAN
yescrypt : 256 bit ← DEFAULT & DIREKOMENDASIKAN sistem baru

Rumus jumlah kemungkinan hash : 2^(jumlah_bit)
Contoh   : 8-bit  → 2^8  = 256 kemungkinan
           4-bit  → 2^4  = 16 kemungkinan

Output format : raw bytes → dikodekan ke HEX atau Base64
Cara hitung byte dari hex : jumlah karakter hex ÷ 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HASH COLLISION & PIGEONHOLE EFFECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Collision      : 2 input berbeda → output SAMA
Pigeonhole     : Input tak terbatas, output terbatas
                 → collision TIDAK BISA dihindari secara matematis
                 → hash bagus membuatnya sangat TIDAK MUNGKIN terjadi
MD5 & SHA-1    : Sudah berhasil di-engineer collision → TIDAK DIPERCAYA
                 Cek : MD5 Collision Demo & Shattered (SHA-1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERINTAH HASHING DI LINUX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
md5sum [file]      → hitung hash MD5
sha1sum [file]     → hitung hash SHA1
sha256sum [file]   → hitung hash SHA256
sha512sum [file]   → hitung hash SHA512
md5sum *.txt       → hash SEMUA file .txt sekaligus (* = wildcard)
wc -l [file]       → hitung jumlah baris dalam file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PENYIMPANAN KATA SANDI YANG AMAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BURUK  : Plaintext      → bocor = langsung kebaca (kasus RockYou 14 juta pass)
BURUK  : Enkripsi usang → kunci tersimpan = bisa didekripsi (kasus Adobe)
BURUK  : Hash tanpa salt→ rentan rainbow table (kasus LinkedIn SHA-1)
BENAR  : Hash + salt unik per user pakai algoritma aman

Algoritma aman untuk password : Argon2, Scrypt, Bcrypt, PBKDF2

Alur penyimpanan yang benar :
1. Pilih algoritma aman (misal Bcrypt)
2. Buat salt unik → misal Y4UV*^(=go_!
3. Gabung password + salt → AL4RMc10kY4UV*^(=go_!
4. Hash gabungan tersebut
5. Simpan HASH + SALT (salt tidak perlu dirahasiakan)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 RAINBOW TABLE vs DICTIONARY ATTACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Rainbow Table  : Tabel hash↔plaintext yang sudah dihitung duluan
                 → Tinggal cocokkan → SANGAT CEPAT
                 → TIDAK mempan jika ada salt
                 → Butuh storage besar
                 → Contoh tools online : CrackStation, Hashes.com

Dictionary Attack (Hashcat) :
                 → Hash dihitung ON THE SPOT satu per satu
                 → Bisa handle salt (otomatis baca dari format hash)
                 → Butuh waktu lebih lama
                 → Wordlist populer : rockyou.txt (14 juta+ password)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FORMAT HASH LINUX (/etc/shadow)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lokasi    : /etc/shadow (hanya root yang bisa baca)
            Dulu di /etc/passwd (bisa dibaca semua orang = TIDAK AMAN)
Format    : $prefix$options$salt$hash
9 field dipisah titik dua ( : ) :
  Field 1 : username
  Field 2 : hash ($prefix$options$salt$hash)
  Field 3 : tanggal terakhir password diubah (hari sejak 1 Jan 1970)
  Field 4 : minimum hari sebelum boleh ganti password
  Field 5 : maksimum hari sebelum harus ganti password
  Field 6 : hari peringatan sebelum expired
  Field 7 : hari setelah expired akun dikunci
  Field 8 : tanggal akun kadaluarsa total
  Field 9 : reserved (selalu kosong)

Prefix Linux (urutan kekuatan menurun) :
  $y$   → yescrypt     ← DEFAULT & DIREKOMENDASIKAN
  $gy$  → gost-yescrypt
  $7$   → scrypt
  $2b$/$2y$/$2a$/$2x$ → bcrypt
  $6$   → sha512crypt
  $md5  → SunMD5
  $1$   → md5crypt

Info detail : man 5 shadow  /  man 5 crypt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WINDOWS PASSWORD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Algoritma : NTLM (varian MD4)
Lokasi    : SAM (Security Accounts Manager)
Jenis hash: NT hash & LM hash
Visual    : IDENTIK dengan MD4 & MD5 → wajib pakai konteks
Tools dump: mimikatz (bypass Windows security)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HASHCAT — SINTAKS & MODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sintaks dasar :
hashcat -m <hash_type> -a <attack_mode> hashfile wordlist

Switch utama :
  -m  → tipe hash (angka dari Hashcat Example Hashes)
  -a  → mode serangan
  -O  → optimized kernel (lebih cepat, max 32 char password)
  -w 3→ workload tinggi (layar bisa lag)
  -S  → slow candidates (lambat tapi lebih akurat)

Attack Mode (-a) :
  0 → Straight/Dictionary : coba kata dari wordlist satu per satu ← PALING UMUM
  1 → Combination         : gabung 2 wordlist
  3 → Brute Force/Mask    : coba semua kombinasi sesuai pola
  6 → Hybrid Wordlist+Mask: kata dari wordlist + karakter acak di belakang
  7 → Hybrid Mask+Wordlist: karakter acak di depan + kata dari wordlist

Hash Mode (-m) yang sering dipakai :
  0    → MD5
  1000 → NTLM
  1400 → SHA2-256
  1800 → sha512crypt $6$
  3200 → bcrypt $2*$
  1710 → HMAC-SHA512 (key = $pass)

Contoh perintah :
hashcat -m 3200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt

Status saat running :
  s → tampilkan status/progress
  p → pause
  r → resume
  b → bypass (skip ke hash berikutnya)
  q → quit (berhenti total)

Catatan GPU vs CPU :
  Hashcat → pakai GPU → jalankan di OS HOST untuk performa maksimal
  John    → pakai CPU → bisa jalan di VM, tapi host tetap lebih cepat
  Bcrypt  → sengaja lambat di GPU = lebih aman dari brute force

Referensi hash type : hashcat.net/wiki/doku.php?id=example_hashes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MENGENALI JENIS HASH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Langkah identifikasi :
1. Lihat PREFIX → $y$, $6$, $2a$ dll → langsung ketahuan
2. Lihat PANJANG karakter hex :
   32 char  → MD5 atau NTLM
   40 char  → SHA-1
   64 char  → SHA-256
   128 char → SHA-512
3. Pakai tools : hashid [hash]  /  hash-identifier
4. Lihat KONTEKS :
   - Dari web app database → kemungkinan MD5
   - Dari /etc/shadow Linux → lihat prefix
   - Dari Windows SAM      → kemungkinan NTLM
5. Konfirmasi di Hashcat Example Hashes

Catatan : MD5 dan NTLM IDENTIK secara visual → bedakan dari konteks!
          Tools otomatis sering salah → tetap konfirmasi manual

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 INTEGRITY CHECKING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kegunaan  : Verifikasi file tidak dimodifikasi
Cara      : Hitung hash file → bandingkan dengan hash resmi dari developer
            Hash sama   → file ASLI & tidak diubah
            Hash beda   → file DIMODIFIKASI atau corrupt
Contoh    : File CHECKSUM Fedora ISO → berisi SHA256 resmi dari tiap file ISO
Bonus     : Hash juga bisa dipakai cari file DUPLIKAT
            2 file hash sama → isi file IDENTIK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HMAC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kepanjangan : Keyed-Hash Message Authentication Code
Fungsi      : Verifikasi KEASLIAN (authenticity) + INTEGRITAS data
Komponen    : Hash function + Secret key
Membuktikan : 1. Pengirim adalah siapa yang mereka klaim (kunci rahasia)
              2. Pesan tidak dimodifikasi (hash)
Alur kerja  :
  1. Secret key dipadding ke ukuran blok hash function
  2. Padded key di-XOR dengan konstanta (ipad)
  3. Pesan di-hash dengan (key XOR ipad)
  4. Hasil step 3 di-hash lagi dengan (key XOR opad)
  5. Output akhir = nilai HMAC

Formula : HMAC(K,M) = H((K⊕opad)||H((K⊕ipad)||M))
          K = kunci, M = pesan, H = hash function

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 HASHING vs ENCODING vs ENCRYPTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                HASHING    ENCODING    ENCRYPTION
Reversible?   : TIDAK       YA          YA (dengan kunci)
Butuh kunci?  : TIDAK       TIDAK       YA
Tujuan        : Integritas  Kompatibel  Kerahasiaan
Contoh        : SHA256,MD5  Base64,UTF8 AES,RSA

Encoding Base64 di Linux :
  base64           → encode (ketik teks → Ctrl+D → keluar hasil)
  base64 -d        → decode dari keyboard
  base64 -d [file] → decode langsung dari file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hash Value/Digest  : Output tetap dari fungsi hash
Salt               : Nilai acak unik yang ditambahkan ke password sebelum di-hash
Rainbow Table      : Tabel lookup hash↔plaintext yang sudah disiapkan
Collision          : 2 input berbeda menghasilkan hash yang sama
Pigeonhole Effect  : Input tak terbatas vs output terbatas → collision pasti ada
Plaintext          : Data/password asli sebelum di-hash
Wordlist           : Daftar kata sandi untuk digunakan dalam cracking
Dictionary Attack  : Serangan dengan mencoba kata dari wordlist satu per satu
Brute Force        : Mencoba semua kemungkinan kombinasi karakter
Integrity          : Jaminan data tidak dimodifikasi
HMAC               : Hash + kunci rahasia untuk verifikasi keaslian & integritas
Stdin Mode         : Hashcat menunggu input dari keyboard (bukan dari file)
Exhausted          : Seluruh wordlist sudah dicoba tapi tidak ada yang cocok
Cracked            : Hash berhasil dipecahkan, plaintext ditemukan
```