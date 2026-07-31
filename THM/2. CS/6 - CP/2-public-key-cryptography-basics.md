```
=== Public Key Cryptography Basics - Resume Materi ===
[09 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 4 PILAR KEAMANAN KOMUNIKASI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Authentication  = Konfirmasi IDENTITAS siapa yang kamu ajak bicara
Authenticity    = Verifikasi pesan BENAR dari pengirim yang diklaim
Integrity       = Pastikan data TIDAK DIUBAH selama perjalanan
Confidentiality = Cegah pihak tidak berwenang MEMBACA komunikasi

Symmetric  → Melindungi CONFIDENTIALITY (kunci sama untuk enkripsi & dekripsi)
Asymmetric → Melindungi AUTHENTICATION, AUTHENTICITY, INTEGRITY

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP KUNCI ASIMETRIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Public Key  = Boleh dibagikan ke siapapun → untuk ENKRIPSI & VERIFIKASI
Private Key = RAHASIA, hanya pemilik → untuk DEKRIPSI & TANDA TANGAN

Enkripsi pesan    : pakai PUBLIC KEY penerima → hanya penerima bisa buka
Tanda tangan      : pakai PRIVATE KEY pengirim → siapapun bisa verifikasi
Analogi public key: nomor rekening → siapapun boleh kirim uang
Analogi priv key  : PIN ATM → hanya pemilik yang boleh tahu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PENGGUNAAN UMUM ENKRIPSI ASIMETRIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Masalah   : Asimetris LAMBAT → tidak cocok untuk komunikasi sehari-hari
Solusi    : Asimetris dipakai SEKALI untuk tukar kunci simetris
           → Selanjutnya komunikasi pakai simetris yang lebih CEPAT

Alur      : Asimetris (sepakat kunci) → Simetris (komunikasi)
Analogi   : Asimetris = negosiasi kode rahasia di tempat umum
            Simetris  = ngobrol pakai kode itu setelahnya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 RSA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu   : Algoritma enkripsi kunci publik untuk transmisi aman
Dasar math: Susahnya FAKTORISASI bilangan besar
            → Kalikan 2 prima besar = MUDAH
            → Cari faktor dari hasil perkaliannya = SUSAH BANGET

Variabel CTF yang wajib hapal :
  p, q  = dua bilangan prima besar (rahasia)
  n     = p × q (hasil perkalian, publik)
  e     = bagian kunci publik
  d     = bagian kunci privat
  m     = plaintext (pesan asli)
  c     = ciphertext (pesan terenkripsi)

Kunci publik  = (n, e)
Kunci privat  = (n, d)
Enkripsi      : c = m^e mod n
Dekripsi      : m = c^d mod n

Keamanan   : Komputer tidak bisa faktorkan bilangan 600+ digit
Tools CTF  : RsaCtfTool, rsatool

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DIFFIE-HELLMAN KEY EXCHANGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tujuan    : Sepakat kunci bersama tanpa pernah kirim kunci itu sendiri
Keunggulan: Pengintip tidak bisa rekonstruksi kunci meski lihat semua traffic

Variabel  :
  p = bilangan prima besar (publik)
  g = generator, 0 < g < p (publik)
  a = private key Alice (RAHASIA)
  b = private key Bob (RAHASIA)
  A = kunci publik Alice = g^a mod p
  B = kunci publik Bob   = g^b mod p

5 Langkah DH :
  1. Sepakat p dan g (publik, semua orang boleh tahu)
  2. Masing-masing pilih private key (a dan b, RAHASIA)
  3. Hitung kunci publik masing-masing (A dan B)
  4. Tukar kunci publik (KEY EXCHANGE)
  5. Hitung shared secret :
     Alice : B^a mod p = g^ab mod p
     Bob   : A^b mod p = g^ab mod p
     → Hasilnya SAMA! Itulah shared secret

Kenapa bisa sama? : (g^b)^a = (g^a)^b = g^ab → hukum pangkat
Keamanan          : Discrete Logarithm Problem → susah balik hitung

DH vs RSA :
  DH  = key agreement (sepakat kunci bersama)
  RSA = digital signatures, key transport, authentication
  → Sering dipakai BERSAMAAN dalam protokol keamanan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SSH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2 Cara autentikasi SSH :
  Password  → Ketik username + password, mudah tapi TIDAK AMAN
  Key Auth  → Pakai pasangan public + private key, LEBIH AMAN

Perintah penting :
  ssh-keygen -t ed25519        → generate key pair Ed25519
  ssh-keygen -t rsa            → generate key pair RSA (kunci lebih panjang)
  ssh -i privateKeyFile user@host → SSH pakai key tertentu
  ssh-copy-id user@host        → copy public key ke server

Algoritma SSH yang tersedia (-t) :
  dsa        = Digital Signature Algorithm
  ecdsa      = Elliptic Curve DSA
  ecdsa-sk   = ECDSA + hardware security key
  ed25519    = EdDSA dengan Curve25519 (DIREKOMENDASIKAN)
  ed25519-sk = Ed25519 + hardware security key
  rsa        = RSA (kunci lebih panjang)

File penting :
  ~/.ssh/id_ed25519      → private key (JANGAN DIBAGIKAN)
  ~/.ssh/id_ed25519.pub  → public key (boleh dibagikan)
  ~/.ssh/authorized_keys → daftar public key yang boleh akses server

Aturan permission : private key harus 600 atau lebih ketat
Identifikasi algo : nama file → id_rsa = RSA, id_ed25519 = Ed25519
                    isi file  → BEGIN RSA PRIVATE KEY = RSA
                                BEGIN OPENSSH PRIVATE KEY = Ed25519/modern

CTF tip : SSH key di authorized_keys bisa jadi BACKDOOR yang berguna

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DIGITAL SIGNATURES & CERTIFICATES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Digital Signature  : Memverifikasi AUTENTISITAS + INTEGRITAS dokumen digital
Cara kerja         :
  Pengirim  → enkripsi HASH dokumen pakai PRIVATE KEY → tanda tangan
  Penerima  → dekripsi pakai PUBLIC KEY pengirim → bandingkan hash
  Cocok     → dokumen ASLI dan tidak diubah
  Tidak cocok → dokumen PALSU atau sudah diubah

Kenapa hash, bukan dokumen langsung?
  → Dokumen bisa sangat besar, hash kecil → lebih efisien

PENTING : Electronic signature (gambar TTD) ≠ Digital signature
  Electronic = tempel gambar TTD → bisa dipalsukan siapapun
  Digital    = pakai private key → tidak bisa dipalsukan

Yang dikirim ada 2 :
  1. File asli (plaintext, bisa dibaca)
  2. Hash terenkripsi (tanda tangan digital)

Certificates (Sertifikat) :
  Fungsi   : Membuktikan identitas server (contoh: HTTPS)
  Chain of Trust :
    Root CA → dipercaya browser otomatis sejak install
    CA      → dipercaya Root CA
    Website → dipercaya CA
    Browser → otomatis percaya website
  TLS cert : bisa beli dari CA berbayar, atau gratis via Let's Encrypt
  Wajib    : semua website modern harus pakai HTTPS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PGP / GPG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PGP = Pretty Good Privacy → software enkripsi file + digital signing
GPG = GnuPG → implementasi open-source dari OpenPGP

Fungsi GPG :
  → Enkripsi file/email (confidentiality)
  → Tanda tangan digital (authenticity + integrity)

Perintah penting :
  gpg --full-gen-key          → generate key pair baru (interactive)
  gpg --import namafile.key   → import key dari file
  gpg --decrypt namafile.gpg  → decrypt file
  gpg --export --armor email > file.asc → export public key

Opsi generate key :
  Algoritma : RSA, DSA, ECC (default & direkomendasikan)
  Kurva ECC : Curve25519 (default), NIST P-384, Brainpool P-256
  Expiry    : 0 = tidak expired, n = n hari, nw = n minggu, dst
  Identity  : nama + email dikaitkan ke key

CTF tip :
  → GPG sering dipakai untuk decrypt file di CTF
  → Kalau key berpassphrase → crack pakai John the Ripper + gpg2john
  → Kalau key sudah disediakan → import dulu, baru decrypt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cryptography       = Ilmu mengamankan komunikasi pakai kode & cipher
Cryptanalysis      = Ilmu memecahkan/melewati sistem kriptografi
Brute-Force Attack = Coba semua kemungkinan kunci/password satu per satu
Dictionary Attack  = Coba kata-kata kamus atau kombinasinya
Plaintext          = Data asli sebelum dienkripsi
Ciphertext         = Data setelah dienkripsi
Symmetric          = Satu kunci untuk enkripsi & dekripsi
Asymmetric         = Dua kunci berbeda (public & private)
Key Exchange       = Proses sepakat kunci bersama lewat jalur tidak aman
Hash               = Ringkasan unik dari data, ukuran tetap
Fingerprint        = Hash dari public key, untuk verifikasi identitas
Passphrase         = Password untuk melindungi private key (tidak dikirim)
CA                 = Certificate Authority, lembaga penerbit sertifikat
Root CA            = CA tertinggi yang dipercaya browser secara default
Chain of Trust     = Rantai kepercayaan dari Root CA ke website
Forward Secrecy    = Kunci baru tiap sesi → sesi lain aman walau satu bocor
Man-in-the-Middle  = Serangan di mana penyerang menyamar sebagai pihak lain
Discrete Log Prob  = Masalah matematika susah → dasar keamanan DH
Factorization Prob = Masalah faktorisasi bilangan besar → dasar keamanan RSA
```