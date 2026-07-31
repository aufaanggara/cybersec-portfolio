```
=== Cryptography Basics - Resume Materi ===
[03 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU KRIPTOGRAFI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Praktik & studi teknik komunikasi aman + perlindungan data
           di hadapan penyerang (adversaries)
Tujuan   : Secure communication in the presence of adversaries
Melindungi 3 hal →
  Confidentiality = kerahasiaan data
  Integrity       = data tidak diubah
  Authenticity    = memastikan identitas pihak yang berkomunikasi
Analogi  : Protokol jaringan = jalan raya, kriptografi = sistem keamanan
           di jalan raya itu (penjaga, rambu, brankas)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Plaintext   = data/pesan ASLI yang bisa dibaca (sebelum enkripsi)
              Bisa berupa: dokumen, gambar, file multimedia, data biner
Ciphertext  = versi ACAK & tidak terbaca setelah enkripsi
              Tidak bisa dapat info apapun dari plaintext kecuali ukurannya
Cipher      = algoritma/metode untuk ubah plaintext ↔ ciphertext
              Dibuat oleh matematikawan, bersifat pengetahuan publik
Key         = string bit yang dipakai cipher untuk enkripsi/dekripsi
              Harus RAHASIA (kecuali public key di asymmetric)
Encryption  = proses plaintext → ciphertext (pakai cipher + key)
              Pilihan cipher boleh diungkap, KEY tidak
Decryption  = proses ciphertext → plaintext (pakai cipher + key)
              Tanpa key = MUSTAHIL mendapatkan plaintext

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR ENKRIPSI & DEKRIPSI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENKRIPSI : Sender → Plaintext → [Encrypt + Key] → Ciphertext →
DEKRIPSI :        → Ciphertext → [Decrypt + Key] → Plaintext → Recipient

Analogi cipher vs key :
  Cipher = resep masakan (semua boleh tahu)
  Key    = bumbu rahasia (hanya pemilik yang tahu)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CONTOH PENGGUNAAN KRIPTOGRAFI SEHARI-HARI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Login website     : kredensial dienkripsi agar tidak bisa di-snoop
→ Koneksi SSH       : membangun tunnel terenkripsi, tidak bisa disadap
→ Online banking    : browser verifikasi sertifikat server bank
→ Download file     : hash function verifikasi file identik dengan aslinya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 REGULASI KRIPTOGRAFI DI DUNIA NYATA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PCI DSS  = Payment Card Industry Data Security Standard
           → Wajib untuk perusahaan yang menangani kartu kredit
           → Data harus dienkripsi at rest (disimpan) & in motion (dikirim)

HIPAA    = Health Insurance Portability & Accountability Act (USA)
HITECH   = Health Information Technology for Economic & Clinical Health (USA)
GDPR     = General Data Protection Regulation (EU)
DPA      = Data Protection Act (UK)
           → Semua untuk rekam medis, berbeda tiap negara

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CAESAR CIPHER (CIPHER HISTORIS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Asal     : Abad pertama SM, salah satu cipher paling sederhana
Cara     : Geser setiap huruf sejumlah N posisi ke kanan
           (saat mencapai Z, mulai dari A lagi)

Contoh   :
  Plaintext  : TRYHACKME
  Key        : 3 (geser kanan 3)
  Ciphertext : WUBKDFNPH
  T→W, R→U, Y→B, H→K, A→D, C→F, K→N, M→P, E→H

Dekripsi : Geser ke KIRI sebesar nilai key

Kelemahan :
  → Hanya ada 25 kemungkinan key (alfabet 26 huruf, geser 26 = tidak berubah)
  → Bisa dipecahkan dengan brute force semua 25 kemungkinan
  → Cipher publik + hanya 25 key = TIDAK AMAN di standar modern

Analogi  : Gembok dengan hanya 25 kombinasi — pencuri tinggal coba satu per satu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CIPHER HISTORIS LAINNYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Vigenère cipher → Abad ke-16
Enigma machine  → Perang Dunia II
One-time pad    → Era Perang Dingin

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DUA JENIS ENKRIPSI UTAMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SYMMETRIC ENCRYPTION
  Nama lain : Private key cryptography
  Cara      : Kunci SAMA untuk enkripsi & dekripsi
  Alur      : Alice & Bob pakai Shared Secret Key yang sama
  Masalah   : Bagaimana cara berbagi key secara aman?
              → Tidak bisa lewat jalur yang sama dengan ciphertext
              → Solusi terakhir: ketemu langsung
  Contoh    :
    DES   → Standar 1977, key 56-bit
            Dipecahkan < 24 jam pada 1999 → diganti 3DES
    3DES  → DES × 3, key 168-bit (efektif 112-bit)
            Solusi sementara, deprecated 2019, diganti AES
    AES   → Standar 2001, key 128/192/256-bit ← STANDAR SAAT INI

ASYMMETRIC ENCRYPTION
  Nama lain : Public key cryptography
  Cara      : Dua kunci BERBEDA — public key & private key
  Alur      :
    Enkripsi : Alice pakai BOB'S PUBLIC KEY → Ciphertext
    Dekripsi : Bob pakai BOB'S PRIVATE KEY → Plaintext
  Aturan    : Data dienkripsi public key → HANYA bisa dibuka private key
              Private key WAJIB dirahasiakan
  Kelemahan : Lebih LAMBAT, ukuran key lebih BESAR
  Contoh    :
    RSA              → Key 2048/3072/4096-bit (min. rekomendasi 2048-bit)
    Diffie-Hellman   → Min. rekomendasi 2048-bit, enhanced 3072/4096-bit
    ECC              → Key lebih PENDEK tapi sekuat RSA
                       256-bit ECC ≈ setara 3072-bit RSA
  Dasar    : Masalah matematika mudah dihitung satu arah
             tapi SANGAT SULIT dibalik (bisa butuh jutaan tahun)

  Analogi  : Public key = slot kotak surat (siapapun bisa masukkan surat)
             Private key = kunci kotak surat (hanya pemilik yang bisa buka)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN SYMMETRIC vs ASYMMETRIC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  SYMMETRIC        ASYMMETRIC
Jumlah key      : 1 (shared)       2 (public + private)
Kecepatan       : CEPAT            LAMBAT
Ukuran key      : Lebih kecil      Lebih besar
Masalah utama   : Distribusi key   Tidak ada (public key bebas dibagi)
Nama lain       : Private key      Public key cryptography
Contoh          : AES, 3DES, DES   RSA, ECC, Diffie-Hellman

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 XOR OPERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kepanjangan : Exclusive OR
Simbol      : ⊕ atau ^
Aturan      : Beda bit = 1, Sama bit = 0

Truth Table :
  0 ⊕ 0 = 0
  0 ⊕ 1 = 1
  1 ⊕ 0 = 1
  1 ⊕ 1 = 0

Sifat penting :
  A ⊕ A = 0          (nilai XOR dirinya sendiri = 0)
  A ⊕ 0 = A          (nilai XOR 0 = tidak berubah)
  A ⊕ B = B ⊕ A      (komutatif)
  (A⊕B)⊕C = A⊕(B⊕C) (asosiatif)

Contoh biner :
  1010 XOR 1100 →
  1⊕1=0, 0⊕1=1, 1⊕0=1, 0⊕0=0 → hasil: 0110

XOR sebagai enkripsi simetris dasar :
  P = plaintext, K = secret key
  Enkripsi : C = P ⊕ K
  Dekripsi : C ⊕ K = (P⊕K)⊕K = P⊕(K⊕K) = P⊕0 = P ✓
  Catatan  : Butuh key SEPANJANG plaintext (tidak praktis)

Analogi  : Sakelar lampu — dinyalakan 2x = kembali ke posisi awal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MODULO OPERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Simbol   : % atau mod
Definisi : X % Y = SISA pembagian X oleh Y
           (bukan hasil baginya, tapi SISANYA)

Contoh   :
  25 % 5 = 0   → 25 = 5×5 + 0
  23 % 6 = 5   → 23 = 3×6 + 5
  23 % 7 = 2   → 23 = 3×7 + 2

Sifat penting :
  → Hasil selalu NON-NEGATIF & kurang dari pembagi
  → Untuk integer a dan positif n : hasil a%n selalu di range 0 sampai n-1
  → TIDAK BISA DIBALIK
    Contoh : x%5 = 4 → tak terhingga nilai x yang memenuhi

Untuk angka besar :
  → Gunakan Python (tipe int bisa handle angka sembarang besar)
  → Atau pakai WolframAlpha → ketik: [angka] mod [pembagi]

Analogi  : Jam dinding — 14:00 = jam 2 siang karena 14 mod 12 = 2
           Kamu tahu jarumnya di angka 2 tapi tidak tahu sudah
           berputar berapa kali → itulah kenapa modulo tidak reversible

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 RINGKASAN AKHIR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Alice & Bob = karakter fiktif standar dalam contoh kriptografi
at rest     = data yang sedang DISIMPAN (diam)
in motion   = data yang sedang DIKIRIM (bergerak)
Deprecated  = sudah tidak direkomendasikan / ditinggalkan
Legacy      = sistem lama yang masih berjalan
Infeasible  = praktis mustahil (misal: butuh jutaan tahun)
```