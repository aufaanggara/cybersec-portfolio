```
=== Networking - Packets, Frames & Protocols - Resume Materi ===
[25 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PACKET vs FRAME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Packet  → Data di Layer 3 (Network Layer) OSI
          Berisi : IP header + payload
          Konteks: saat bicara IP address = bicara packet

Frame   → Data di Layer 2 (Data Link Layer) OSI
          Berisi : packet + MAC address (encapsulated)
          Konteks: saat encapsulating info dilepas = bicara frame

Proses  → Encapsulation  = packet dibungkus jadi frame
          Decapsulation  = frame dibuka, isi packet keluar

Analogi → Surat (packet) di dalam amplop (frame)
          Amplop = untuk pengiriman
          Surat  = isi yang sebenarnya

Kenapa packet efisien?
  → Data dipecah jadi potongan kecil → less bottleneck
  → Contoh: gambar dipecah 3 packet → direkonstruksi di tujuan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 IP PACKET HEADERS (WAJIB HAPAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Time to Live    → Timer kedaluwarsa packet
(TTL)             agar tidak nyumbat jaringan selamanya

Checksum        → Cek integritas data
                  Nilai beda dari expected = data CORRUPT

Source Address  → IP pengirim (data tahu cara kembali)

Destination     → IP penerima (data tahu mau ke mana)
Address

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TCP (Transmission Control Protocol)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sifat    : Connection-based
           Harus bangun koneksi DULU sebelum kirim data

Model    : TCP/IP = 4 layer (versi ringkas OSI)
           → Application
           → Transport
           → Internet
           → Network Interface

Kelebihan TCP               Kekurangan TCP
─────────────────────       ─────────────────────────────────
Jamin integritas data       Butuh koneksi andal, 1 chunk
                            gagal = seluruh chunk kirim ulang
Sinkronisasi 2 device       Koneksi lambat = bottleneck device
agar tidak flood data         lain (koneksi direservasi terus)
Banyak proses untuk         Jauh lebih lambat dari UDP
reliability                 (lebih banyak komputasi)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TCP HEADERS (WAJIB HAPAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Source Port     → Port pengirim, dipilih ACAK (0-65535)

Destination     → Port tujuan, TIDAK acak
Port              Contoh: web server = port 80

Source IP       → IP pengirim packet

Destination IP  → IP tujuan packet

Sequence Number → Nomor acak untuk potongan data pertama

Acknowledgement → Sequence number + 1 untuk data berikutnya
Number

Checksum        → Kalkulasi matematika untuk cek integritas
                  Output beda = data corrupt

Data            → Tempat bytes file yang dikirim disimpan

Flag            → Menentukan cara packet ditangani saat
                  handshake (SYN, ACK, FIN, RST, dll)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 THREE-WAY HANDSHAKE (WAJIB HAPAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tujuan  : Membangun koneksi antara 2 perangkat

Step  Message   Pengirim   Keterangan
────  ────────  ─────────  ──────────────────────────────
1     SYN       Client→    Mulai koneksi + sync 2 device
2     SYN/ACK   ←Server    Akui upaya sync dari client
3     ACK       Client→    Akui SYN/ACK server
4     DATA      Client→    Kirim data (bytes file)
5     FIN       siapapun   Tutup koneksi dengan bersih
#     RST       siapapun   Tutup PAKSA, ada masalah serius
                           (low resource / error / crash)

Diagram:
  Alice ──── SYN ────────→ Bob
  Alice ←─── SYN/ACK ───── Bob
  Alice ──── ACK ────────→ Bob
  [koneksi terbentuk, data mulai mengalir]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SEQUENCE NUMBER & ISN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ISN = Initial Sequence Number (nomor urut awal, dipilih acak)
Setiap data berikutnya = ISN + 1

Proses kesepakatan ISN (3 langkah):
1. SYN     → Client: "ISN saya = 0, sync denganmu"
2. SYN/ACK → Server: "ISN saya = 5000, ACK ISN kamu (0)"
3. ACK     → Client: "ACK ISN kamu (5000), data saya ISN+1 = 1"

Tabel urutan:
  Device           ISN    Final
  ───────────────  ─────  ─────
  Client (Sender)  0      0+1=1
  Client (Sender)  1      1+1=2
  Client (Sender)  2      2+1=3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TCP CLOSING CONNECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kapan  : Setelah device yakin semua data sudah diterima
Kenapa : TCP reservasi resource → tutup SESEGERA MUNGKIN

Diagram:
  Alice ──── FIN ────────→ Bob   (Alice minta tutup)
  Alice ←─── ACK ────────  Bob   (Bob terima, akui)
  Alice ←─── FIN ────────  Bob   (Bob juga minta tutup)
  Alice ──── ACK ────────→ Bob   (Alice akui, selesai)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 STEALTH SCAN (HALF-OPEN SCAN) -sS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tujuan  : Scanning port tanpa tercatat di log server
Cara    : Handshake TIDAK diselesaikan (half-open)

Normal TCP (-sT):          Stealth (-sS):
  SYN →                      SYN →
  ← SYN/ACK                  ← SYN/ACK
  ACK → [konek]              RST → [batalkan, tidak jadi konek]

Perbandingan:
              -sT (TCP)       -sS (Stealth)
  Handshake   Penuh           Setengah
  Koneksi     Terbentuk       TIDAK terbentuk
  Log server  Tercatat        Kemungkinan TIDAK tercatat
  Kecepatan   Lebih lambat    Lebih cepat
  Deteksi     Mudah           Lebih sulit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 UDP (User Datagram Protocol)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sifat    : Stateless
           Tidak butuh koneksi konstan
           Tidak ada Three-Way Handshake
           Tidak ada sinkronisasi

Cocok untuk : Video streaming, voice chat, kondisi
              di mana kehilangan data masih bisa ditoleransi

Kelebihan UDP               Kekurangan UDP
─────────────────────       ──────────────────────────────
Jauh lebih cepat dari TCP   Tidak peduli data diterima/tidak
App yang kontrol kecepatan  Fleksibel tapi rawan developer
kirim packet                salah implementasi
Tidak reservasi koneksi     Koneksi tidak stabil = pengalaman
terus-menerus               user yang sangat buruk

Tidak ada safeguard seperti TCP (no data integrity check)

Diagram koneksi UDP:
  Bob  ──── REQUEST ────→ Alice
  Bob  ←─── RESPONSE ───  Alice
  Bob  ←─── RESPONSE ───  Alice   ← terus kirim tanpa
  Bob  ←─── RESPONSE ───  Alice     tunggu konfirmasi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 UDP HEADERS (lebih sedikit dari TCP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Time to Live    → Timer kedaluwarsa packet
(TTL)

Source Address  → IP pengirim (agar data tahu cara kembali)

Destination     → IP tujuan (agar data tahu ke mana pergi)
Address

Source Port     → Port pengirim, dipilih ACAK (0-65535)

Destination     → Port tujuan, TIDAK acak
Port              Contoh: web server port 80

Data            → Tempat bytes file yang dikirim disimpan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TCP vs UDP (PERBANDINGAN LENGKAP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  TCP              UDP
  ─────────────   ──────────────   ──────────────
  Jenis           Connection-based Stateless
  Handshake       ✅ Ada           ❌ Tidak ada
  Jamin diterima  ✅ Ya            ❌ Tidak
  Acknowledgement ✅ Ada           ❌ Tidak ada
  Integritas data ✅ Ada checksum  ❌ Tidak ada
  Kecepatan       Lambat           Cepat
  Resource        Reservasi        Tidak reservasi
  Cocok untuk     File transfer,   Video streaming,
                  web browsing     voice chat, game

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PORT — APA ITU & KENAPA PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Titik di mana data dipertukarkan antar perangkat
Range    : 0 – 65535
Common   : Port 0 – 1024 = Common Ports (port umum/standar)

Analogi  : Pelabuhan → port harus kompatibel dengan kapal
           Kapal pesiar ≠ bisa masuk port kapal nelayan

Fungsi   : Enforce aturan komunikasi antar perangkat
           Memastikan aplikasi berbeda bisa saling pahami data

Standar  : Misal semua browser kirim data via port 80
           → Chrome & Firefox bisa interpret data sama

CATATAN PENTING:
  Standar bisa diubah! Tapi aplikasi tetap anggap standar dipakai
  Jika pakai port non-standar → wajib tulis dengan colon (:)
  Contoh: 192.168.1.1:8080

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 COMMON PORTS — WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Port   Protokol   Kepanjangan                    Fungsi
─────  ─────────  ─────────────────────────────  ────────────────────────
21     FTP        File Transfer Protocol         Download file dari server
                                                 (client-server model)
22     SSH        Secure Shell                   Login aman via text-based
                                                 interface (untuk manajemen)
80     HTTP       HyperText Transfer Protocol    Browsing web biasa (WWW)
                                                 download teks/gambar/video
443    HTTPS      HTTP Secure                    Sama seperti HTTP tapi
                                                 TERENKRIPSI (aman)
445    SMB        Server Message Block           Share file + share device
                                                 (printer, dll) di jaringan
3389   RDP        Remote Desktop Protocol        Login ke sistem via
                                                 tampilan desktop visual
                                                 (beda dari SSH = visual!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Encapsulation    = proses membungkus packet menjadi frame
Decapsulation    = proses membuka frame untuk dapat packet
Stateless        = tidak ingat status koneksi (UDP)
Stateful         = melacak & ingat status koneksi (TCP)
ISN              = Initial Sequence Number, nomor urut awal acak
TTL              = Time to Live, timer kedaluwarsa packet
Checksum         = nilai cek integritas data matematika
Half-Open Scan   = teknik scan (-sS) yang tidak selesaikan handshake
Common Port      = port standar dalam range 0-1024
Bottleneck       = kemacetan/penumpukan data di jaringan
Acknowledgement  = konfirmasi bahwa data sudah diterima (ACK)
```