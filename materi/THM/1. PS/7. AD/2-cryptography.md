```
=== Cryptography - Resume Materi ===
[27 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU KRIPTOGRAFI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Ilmu mengamankan komunikasi menggunakan
           aturan matematika & kunci rahasia
Tujuan   : Melindungi Confidentiality & Integrity (bagian CIA Triad)
Cara     : Mengubah data yang bisa dibaca menjadi
           data acak yang tidak bermakna
Analogi  : Seperti mengunci surat dalam kotak → hanya
           pemegang kunci yang bisa membacanya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH DASAR WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Plaintext   = Data asli yang bisa dibaca siapapun
              Contoh : HELLO / Patient name: Alice Smith

Ciphertext  = Data yang sudah diacak, tidak bermakna
              Contoh : KHOOR / Sdwlhqw qdph: Dolfh Vplwk

Kunci (Key) = Rahasia yang mengontrol cara enkripsi
              & dekripsi bekerja → seperti password
              untuk algoritma

Algoritma   = Resep/langkah publik cara menggunakan
              kunci pada pesan
              PENTING : Algoritma boleh publik,
              KUNCI harus tetap rahasia

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PROSES ENKRIPSI & DEKRIPSI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Enkripsi : plaintext + algoritma + key → ciphertext
Dekripsi : ciphertext + algoritma + key → plaintext

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ENKRIPSI SIMETRIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Satu kunci yang SAMA untuk enkripsi & dekripsi
Analogi  : Kotak kunci (lockbox) → 1 kunci untuk kunci
           & buka kotak yang sama
Sifat    :
  ✓ Cepat & efisien
  ✓ Cocok untuk enkripsi data massal
    (file, hard drive, network traffic)
  ✗ MASALAH : Key Distribution Problem →
    bagaimana berbagi kunci dengan aman?

Key Distribution Problem :
  → Kirim via internet biasa? Penyerang bisa curi
  → Enkripsi kuncinya? Butuh kunci lain → infinite regress
  → Inilah kelemahan utama enkripsi simetris

Contoh algoritma nyata : AES (Advanced Encryption Standard)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CAESAR CIPHER (Contoh Simetris Sederhana)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cara kerja : Geser setiap huruf sejumlah posisi tetap
             → Angka geseran = KUNCI
Contoh key = 3 :
  A→D, B→E, C→F ... X→A, Y→B, Z→C
  HELLO → H(+3)=K, E(+3)=H, L(+3)=O,
          L(+3)=O, O(+3)=R → KHOOR

Dekripsi   : Geser mundur sejumlah kunci
  KHOOR → K(-3)=H, H(-3)=E, O(-3)=L,
          O(-3)=L, R(-3)=O → HELLO

⚠ Caesar cipher TIDAK AMAN & tidak pernah
  dipakai di sistem nyata → hanya 25 kemungkinan,
  komputer bisa crack dalam 1 milidetik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ENKRIPSI ASIMETRIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Dua kunci berbeda yang terhubung secara
           matematis
Kunci    :
  Public Key  = Boleh dibagikan ke siapapun
  Private Key = Hanya pemilik yang boleh tahu

Aturan penting :
  → Enkripsi pakai PUBLIC key seseorang
    = hanya PRIVATE key mereka yang bisa dekripsi
  → Enkripsi pakai PRIVATE key sendiri
    = siapapun dengan PUBLIC key bisa dekripsi
    (digunakan untuk tanda tangan digital)

Analogi  : Kotak surat (mailbox)
  Celah surat  = Public Key (siapapun bisa masukkan surat)
  Pintu kunci  = Private Key (hanya pemilik bisa ambil)

Keunggulan :
  ✓ Memecahkan Key Distribution Problem
  ✓ Tidak perlu bertukar rahasia dulu sebelum komunikasi
  ✗ Lebih lambat → hanya untuk data kecil

Alur Alice → Bob :
  1. Bob buat public key & private key
  2. Bob bagikan public key ke publik
  3. Alice enkripsi pesan pakai public key Bob
  4. Bob dekripsi pakai private key-nya
  → Tidak ada kunci rahasia yang berpindah!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PENGGUNAAN NYATA : HTTPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ikon gembok di browser = HTTPS aktif

Proses saat buka https://google.com :
  1. Browser minta public key website
  2. Website kirim public key dalam SERTIFIKAT
  3. Browser & website pakai asimetris untuk
     sepakati kunci simetris bersama (shared secret)
  4. Selanjutnya pakai enkripsi SIMETRIS
     (lebih cepat) untuk sisa sesi

Ini disebut HYBRID APPROACH :
  Asimetris → selesaikan key distribution
  Simetris  → tangani data karena lebih cepat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SERTIFIKAT DIGITAL & CA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Masalah : Bagaimana tahu public key benar milik Bob,
          bukan penyerang yang pura-pura jadi Bob?
Solusi  : Sertifikat Digital

Sertifikat berisi :
  → Public key pemilik
  → Identitas pemilik (misal: example.com)
  → Tanda tangan digital dari Certificate Authority (CA)

CA (Certificate Authority) :
  = Otoritas terpercaya yang memverifikasi & menandatangani
    sertifikat
  Contoh CA terkenal : Google Trust Services, DigiCert

Browser cek sertifikat :
  ✓ Ditandatangani CA terpercaya?
  ✓ Masih valid (belum expired/dicabut)?
  → Jika OK : tampilkan gembok ✓
  → Jika gagal : tampilkan WARNING ⚠

Info dalam sertifikat :
  Issued To   = domain website
  Issued By   = CA yang tanda tangan
  Valid From / Valid Until = masa berlaku

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBANDINGAN SIMETRIS vs ASIMETRIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fitur         │ Simetris          │ Asimetris
──────────────┼───────────────────┼─────────────────────
Jumlah kunci  │ 1 kunci           │ 2 kunci (pub+priv)
Berbagi kunci │ Harus sama-sama   │ Public key bebas
              │ punya kunci rahasia│ dibagikan
Kecepatan     │ Sangat cepat      │ Lebih lambat
Kegunaan      │ Enkripsi data     │ Berbagi kunci &
              │ massal            │ sertifikat digital
Analogi       │ 1 kunci buka &    │ Kotak surat :
              │ kunci kotak       │ siapa saja kirim,
              │                   │ hanya pemilik ambil
Kelemahan     │ Key distribution  │ Lambat untuk
              │ problem           │ data besar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SISTEM NYATA PAKAI KEDUANYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Asimetris → mulai koneksi & bagikan kunci simetris
Simetris  → tangani semua data selanjutnya

Dipakai oleh : HTTPS, VPN, aplikasi pesan terenkripsi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Plaintext          = Data asli yang bisa dibaca
Ciphertext         = Data terenkripsi / diacak
Enkripsi           = Proses ubah plaintext → ciphertext
Dekripsi           = Proses ubah ciphertext → plaintext
Kunci (Key)        = Rahasia yang kontrol enkripsi/dekripsi
Algoritma          = Metode/langkah publik pakai kunci
Public Key         = Kunci yang bebas dibagikan
Private Key        = Kunci rahasia milik satu orang
CA                 = Certificate Authority, pihak
                     terpercaya yang verifikasi sertifikat
Hybrid Approach    = Kombinasi asimetris+simetris di HTTPS
Key Distribution   = Masalah cara berbagi kunci dengan aman
Problem
Sertifikat Digital = Dokumen berisi public key yang sudah
                     diverifikasi CA
HTTPS              = Protokol web aman pakai kriptografi
                     hybrid → ditandai ikon gembok
```

# Rangkuman Lengkap — Cryptography Course

---

## Task 1 — Pengantar Kriptografi

Kriptografi adalah ilmu mengamankan komunikasi menggunakan aturan matematika dan kunci rahasia, sehingga hanya pihak yang berwenang yang bisa membaca atau memahami informasi tersebut. Di dunia nyata, data yang kamu kirim lewat internet tidak berpindah langsung dari kamu ke penerima — data itu melewati lusinan komputer dan router di sepanjang jalan. Tanpa perlindungan, siapa saja yang punya akses ke sistem-sistem tersebut bisa membaca, mengubah, atau bahkan memblokir datamu.

Kriptografi berkaitan langsung dengan **CIA Triad** yang sudah dibahas di modul sebelumnya. Dari tiga pilar yaitu Confidentiality, Integrity, dan Availability, kriptografi terutama bertugas melindungi dua yang pertama. Penyerang mencoba membobol ketiganya melalui disclosure (kebocoran data), alteration (manipulasi data), dan destruction (perusakan data) — dan kriptografi adalah salah satu senjata utama untuk mencegah hal tersebut.

Dua konsep visual paling dasar dalam kriptografi adalah **plaintext** dan **ciphertext**. Plaintext adalah pesan asli yang bisa dibaca siapapun — seperti kata "HELLO" atau "Patient name: Alice Smith". Ciphertext adalah versi yang sudah diacak sehingga tidak bermakna bagi yang tidak punya kunci — seperti "KHOOR" atau "Sdwlhqw qdph: Dolfh Vplwk". Tujuan enkripsi adalah mengubah plaintext menjadi ciphertext, dan tujuan dekripsi adalah kebalikannya.

Skenario dunia nyata yang digunakan sebagai ilustrasi adalah klinik medis kecil yang perlu mengirim rekam medis pasien kepada spesialis dan perusahaan asuransi lewat internet. Tanpa kriptografi, siapa saja yang duduk di antara pengirim dan penerima bisa membaca atau memanipulasi data sensitif tersebut.

---

## Task 2 — Enkripsi Simetris

### Empat Istilah Fondasi

Sebelum masuk ke teknis enkripsi, ada empat istilah yang harus benar-benar dipahami karena akan terus muncul:

- **Plaintext** adalah pesan asli yang bisa dibaca secara normal, misalnya `HELLO` atau `Patient name: Alice Smith`. Ini adalah data sebelum disentuh proses enkripsi apapun.
- **Ciphertext** adalah versi acak dari plaintext yang tidak seharusnya masuk akal bagi siapapun tanpa kunci, misalnya `KHOOR` atau `Sdwlhqw qdph: Dolfh Vplwk`.
- **Kunci (Key)** adalah bahan rahasia yang mengontrol cara pengacakan dan pembongkaran acakan bekerja. Analoginya seperti password yang digunakan oleh algoritma — tanpa kunci yang tepat, ciphertext tidak bisa dibaca.
- **Algoritma** adalah resep publik, yaitu sekumpulan langkah yang menjelaskan cara menggunakan kunci pada pesan. Yang penting dipahami: **algoritma boleh diketahui publik, tapi kunci harus tetap rahasia**. Keamanan sistem kriptografi bukan berasal dari kerahasiaan algoritmanya, melainkan dari kerahasiaan kuncinya.

Proses enkripsi secara formal ditulis sebagai:
**plaintext + algoritma enkripsi + kunci → ciphertext**

Dan proses dekripsi:
**ciphertext + algoritma dekripsi + kunci → plaintext**

### Analogi Kotak Kunci (Lockbox)

Untuk memahami enkripsi simetris secara intuitif, materi menggunakan analogi kotak kunci fisik. Dalam analogi ini, algoritmanya adalah cara kerja kunci — semua orang bisa melihatmu memasukkan kunci dan memutarnya, jadi itu bukan rahasia. Kuncinya adalah kunci logam spesifikmu — hanya orang dengan kunci yang sama persis yang bisa membuka kotak. Plaintextnya adalah surat di dalam kotak, dan ciphertextnya adalah kotak terkunci yang sedang dikirim melalui sistem pos.

Contoh kasusnya: Alice ingin mengirim surat rahasia kepada Bob, tapi surat itu harus melewati sistem pos publik di mana siapa saja bisa membukanya. Alice menulis pesannya, memasukkannya ke kotak kunci yang kokoh, menguncinya dengan gembok, lalu mengirimkan kotak itu. Bob yang memegang salinan kunci yang sama bisa membuka dan membaca pesannya. Siapapun yang mencegat kotak di tengah jalan hanya melihat kotak logam terkunci yang tidak berguna tanpa kunci. Itulah inti dari enkripsi simetris: **satu kunci yang sama digunakan untuk mengunci dan membuka**.

### Caesar Cipher — Contoh Konkret

Untuk membuat konsep ini benar-benar konkret, materi menggunakan **Caesar Cipher** sebagai contoh. Caesar Cipher dinamai dari Julius Caesar yang menggunakan teknik ini lebih dari 2000 tahun lalu untuk mengirim pesan militer. Cara kerjanya sederhana: setiap huruf dalam pesan digeser sejumlah posisi tetap dalam alfabet, dan angka geseran itu adalah kuncinya.

Dengan kunci = 3:
- A bergeser 3 posisi menjadi D
- B menjadi E, C menjadi F, dan seterusnya
- X menjadi A (melingkar kembali ke awal alfabet)
- Y menjadi B, Z menjadi C

Contoh enkripsi kata `HELLO` dengan kunci 3:
- H → K
- E → H
- L → O
- L → O
- O → R

Hasilnya: `HELLO` menjadi `KHOOR`

Untuk dekripsi, Bob cukup membalik prosesnya — menggeser setiap huruf mundur sebanyak 3:
- K → H, H → E, O → L, O → L, R → O
- Hasilnya kembali: `HELLO`

Dalam Caesar Cipher ini, algoritmanya (geser huruf sejumlah angka tertentu) sepenuhnya publik dan semua orang boleh tahu. Yang rahasia hanya angka kuncinya — dalam contoh ini angka 3 — yang hanya diketahui Alice dan Bob.

**Peringatan penting:** Caesar Cipher sama sekali tidak aman dan tidak pernah digunakan di sistem nyata. Hanya ada 25 kemungkinan kunci (pergeseran 1 sampai 25), dan komputer bisa mencoba semua kemungkinan itu dalam sekitar satu milidetik. Caesar Cipher hanya dipakai di sini karena mudah dipahami untuk mengilustrasikan cara kerja kunci dan algoritma. Algoritma nyata seperti **AES (Advanced Encryption Standard)** jauh lebih kompleks tapi mengikuti ide dasar yang sama.

### Keunggulan dan Kelemahan Enkripsi Simetris

Enkripsi simetris memiliki dua keunggulan utama: **cepat** karena algoritma simetris bisa memproses data dalam jumlah sangat besar dengan sangat cepat, dan **efisien** sehingga cocok untuk mengenkripsi file, hard drive, dan lalu lintas jaringan di mana kecepatan sangat penting.

Namun ada satu kelemahan fatal yang disebut **Key Distribution Problem** (masalah distribusi kunci). Pertanyaannya: bagaimana Alice dan Bob berbagi kunci itu dengan aman sejak awal sebelum komunikasi dimulai? Jika kunci dikirim lewat internet secara terbuka, penyadap bisa mengambilnya dan mendekripsi semua pesan selanjutnya. Kalau kuncinya dienkripsi dulu, dibutuhkan kunci lain untuk mengenkripsi kunci itu — dan kunci lain lagi untuk yang itu — mundur tanpa batas (infinite regress). Inilah titik lemah enkripsi simetris ketika digunakan sendiri, dan inilah yang mendorong lahirnya enkripsi asimetris.

---

## Task 3 — Enkripsi Asimetris

### Dua Kunci, Bukan Satu

Enkripsi asimetris muncul sebagai solusi langsung dari Key Distribution Problem. Alih-alih satu kunci, enkripsi asimetris menggunakan **dua kunci yang terhubung secara matematis**:

- **Kunci publik (public key)** — yang boleh diketahui dan digunakan oleh siapa saja
- **Kunci privat (private key)** — yang hanya satu orang simpan sebagai rahasia mutlak

Aturan kerjanya:
- Jika sesuatu dienkripsi menggunakan **public key** seseorang, maka hanya **private key** orang itu yang bisa mendekripsinya
- Jika sesuatu dienkripsi menggunakan **private key** sendiri, maka siapapun yang punya **public key**-nya bisa mendekripsinya — ini terutama digunakan untuk tanda tangan digital

Kedua kunci terhubung dengan matematika yang sangat kompleks. Komputer biasa butuh ratusan hingga ribuan tahun untuk mendapatkan kunci privat dari kunci publik — kesulitan komputasi inilah yang menjadi fondasi keamanan enkripsi asimetris.

### Analogi Kotak Surat (Mailbox)

Untuk memahaminya secara intuitif, materi menggunakan analogi kotak surat fisik di sudut jalan. **Celah surat di bagian atas** adalah public key — siapa saja yang lewat bisa memasukkan surat, sepenuhnya terbuka dan bisa diakses. **Pintu terkunci di bagian depan** adalah private key — hanya pemilik kotak surat yang punya kunci untuk membukanya dan mengambil isinya.

Ketika Alice ingin mengirim pesan rahasia kepada Bob menggunakan sistem ini:
1. Alice mencari public key Bob — ini bukan rahasia, Bob bahkan bisa mempostingnya di websitenya
2. Alice menulis pesannya, mengenkripsinya dengan public key Bob, dan mengirimkannya
3. Hanya Bob yang bisa mendekripsinya karena hanya dia yang punya private key-nya

Bahkan jika penyerang mencegat pesan terenkripsi di tengah jalan, mereka tidak bisa mendekripsinya tanpa private key Bob.

### Memecahkan Key Distribution Problem

Alur lengkap komunikasi aman antara Alice dan Bob dengan enkripsi asimetris:
1. Bob membuat public key dan private key di komputernya, menyimpan private key untuk dirinya sendiri, dan membagikan public key ke seluruh dunia
2. Alice mengambil public key Bob — bisa dari website Bob atau server kunci publik
3. Alice mengenkripsi pesannya menggunakan public key Bob dan mengirimkannya
4. Bob menerima dan mendekripsinya menggunakan private key-nya

Yang sangat penting untuk dipahami: **tidak ada satu pun momen di mana kunci rahasia berpindah melalui jaringan**. Satu-satunya yang berpindah secara publik adalah public key Bob, yang memang dirancang untuk tidak rahasia. Itulah mengapa Key Distribution Problem terpecahkan.

### Penggunaan Nyata: HTTPS

Penggunaan enkripsi asimetris yang paling umum dalam kehidupan sehari-hari adalah **HTTPS** — protokol aman yang ditandai dengan ikon gembok di address bar browser. Inilah yang sebenarnya terjadi ketika kamu mengunjungi `https://google.com`:

1. Browsermu meminta public key dari website Google
2. Google mengirimkan public key-nya yang dibungkus dalam sebuah **sertifikat digital**
3. Browsermu dan server Google menggunakan enkripsi asimetris untuk menyepakati sebuah **shared secret** — yaitu kunci simetris bersama — tanpa ada pihak lain yang bisa melihatnya
4. Setelah kunci simetris disepakati, komunikasi selanjutnya beralih ke **enkripsi simetris** yang jauh lebih cepat untuk sisa sesi

Kombinasi ini disebut **pendekatan hibrida (hybrid approach)**. Enkripsi asimetris menyelesaikan masalah distribusi kunci di awal, lalu enkripsi simetris mengambil alih untuk menangani semua data karena kecepatannya. Itulah mengapa HTTPS bisa aman sekaligus cukup cepat untuk browsing normal.

### Sertifikat Digital dan Certificate Authority

Muncul satu pertanyaan penting: bagaimana browsermu tahu bahwa public key yang diterima benar-benar milik Google, dan bukan milik penyerang yang berpura-pura menjadi Google? Jawabannya adalah **sertifikat digital**.

Sertifikat digital adalah dokumen digital yang berisi tiga hal: public key pemiliknya, pernyataan identitas siapa pemilik kunci itu (misalnya `example.com`), dan tanda tangan digital dari pihak ketiga terpercaya yang disebut **Certificate Authority (CA)**.

CA adalah otoritas terpercaya yang bertugas memverifikasi identitas pemilik domain dan menandatangani sertifikat mereka. Contoh CA terkenal adalah Google Trust Services dan DigiCert. Browsermu dan sistem operasimu sudah dilengkapi sejak awal dengan daftar CA yang dipercaya.

Ketika sebuah website menyerahkan sertifikat, browser melakukan tiga pengecekan:
- Apakah sertifikat ini ditandatangani oleh CA yang terpercaya?
- Apakah sertifikat ini masih valid (belum kadaluarsa atau dicabut)?
- Jika semua oke, browser menampilkan ikon gembok dan mempercayai public key tersebut

Jika ada yang tidak beres — sertifikat kadaluarsa, ditandatangani oleh CA yang tidak dikenal, atau domain tidak cocok — browser menampilkan peringatan dan bisa menolak koneksi sepenuhnya. Inilah cara browsermu membedakan website asli dari versi palsu buatan penyerang.

Informasi yang bisa dilihat dalam sertifikat nyata (contoh dari `tryhackme.com`):
- **Issued To:** tryhackme.com
- **Issued By:** WE1, Google Trust Services
- **Issued On:** 25 November 2025
- **Expires On:** 23 Februari 2026

Kamu bisa melihat sertifikat ini sendiri dengan mengklik ikon gembok di browser, lalu pilih "Connection is secure" atau "View certificate".

### Perbandingan Simetris vs Asimetris

| Fitur | Enkripsi Simetris | Enkripsi Asimetris |
|---|---|---|
| Jumlah kunci | 1 kunci untuk enkripsi & dekripsi | 2 kunci: public dan private |
| Berbagi kunci | Kedua pihak harus punya kunci rahasia yang sama | Public key bebas dibagikan ke siapapun |
| Kecepatan | Sangat cepat | Lebih lambat, hanya untuk data kecil |
| Kegunaan utama | Enkripsi data massal (file, network traffic) | Berbagi kunci aman & sertifikat digital |
| Analogi | Satu kunci buka dan kunci kotak | Kotak surat: siapapun kirim, hanya pemilik ambil |
| Kelemahan utama | Key Distribution Problem | Lebih lambat dari simetris |

Dalam praktiknya, sistem nyata selalu menggunakan **keduanya secara bersamaan**: enkripsi asimetris untuk memulai koneksi dan menyepakati kunci, lalu enkripsi simetris untuk menangani semua data selanjutnya secara efisien. Inilah cara HTTPS, VPN, dan aplikasi pesan terenkripsi seperti WhatsApp semuanya beroperasi.

---

## Task 4 — Kesimpulan

Kriptografi adalah salah satu alat paling penting dalam dunia keamanan siber. Ia melindungi confidentiality dan integrity, dan menjadi tulang punggung dari hampir setiap sistem aman yang digunakan secara online — mulai dari banking, email, hingga chat sehari-hari. Namun penting untuk dipahami bahwa kriptografi bukan sihir dan bukan solusi tunggal. Ia hanyalah satu lapisan dalam gambaran keamanan yang jauh lebih besar.

Lapisan-lapisan lain yang sama pentingnya:
- **Praktik password yang kuat** — password lemah bisa membuat enkripsi sekuat apapun menjadi tidak berguna
- **Penyimpanan kunci yang aman** — kunci yang bocor berarti enkripsi yang gagal
- **Kesadaran dan pelatihan pengguna** — manusia sering menjadi titik lemah terbesar dalam sistem apapun
- **Pembaruan perangkat lunak secara rutin** — kerentanan di software bisa membuka jalan masuk tanpa harus membobol enkripsi
- **Pemantauan dan respons insiden** — mendeteksi dan merespons serangan yang sudah terjadi

Memahami cara kerja kriptografi dan di mana ia bisa gagal membantu kita berpikir lebih cermat tentang semua lapisan keamanan ini secara keseluruhan.