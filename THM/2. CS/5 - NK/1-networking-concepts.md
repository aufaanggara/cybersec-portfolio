```
=== Networking Concepts - Resume Materi ===
[26 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 OSI MODEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : Model konseptual ISO yang mendefinisikan kerangka kerja
           komunikasi jaringan komputer → 7 layer
Mnemonik : "Please Do Not Throw Spinach Pizza Away" (layer 1→7)
Penting  : Hapal nomor layer-nya! → "layer 3 switch", "layer 7 firewall"

LAYER    NAMA               FUNGSI UTAMA                    PROTOKOL/CONTOH
─────────────────────────────────────────────────────────────────────────────
7        Application        Layanan ke aplikasi end-user     HTTP, FTP, DNS,
                                                             POP3, SMTP, IMAP
6        Presentation       Encoding, enkripsi, kompresi     Unicode, MIME,
                                                             JPEG, PNG, MPEG
5        Session            Bangun, jaga, sinkron sesi       NFS, RPC
4        Transport          Komunikasi end-to-end            TCP, UDP
3        Network            Logical addressing & routing     IP, ICMP, IPSec
2        Data Link          Transfer data antar node         Ethernet (802.3),
                            di segmen yang sama              WiFi (802.11)
1        Physical           Media transmisi fisik            Electrical, optical,
                                                             wireless signals

NAMA UNIT DATA PER LAYER → WAJIB HAPAL!
  Layer 7  → Application Data
  Layer 4 TCP → Segment
  Layer 4 UDP → Datagram
  Layer 3  → Packet
  Layer 2  → Frame

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TCP/IP MODEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : Model yang BENAR-BENAR diimplementasikan di dunia nyata
Dibuat   : Tahun 1970-an oleh Department of Defense (DoD) Amerika
Alasan   : Jaringan tetap berfungsi meski sebagian diserang/rusak

PERBANDINGAN OSI vs TCP/IP :
  OSI Layer 7,6,5  →  TCP/IP : Application Layer  (HTTP,FTP,SSH,Telnet,dll)
  OSI Layer 4      →  TCP/IP : Transport Layer     (TCP, UDP)
  OSI Layer 3      →  TCP/IP : Internet Layer      (IP, ICMP, IPSec)
  OSI Layer 2      →  TCP/IP : Link Layer          (Ethernet 802.3, WiFi 802.11)
  OSI Layer 1      →  (tidak ada di RFC 1122, ada di versi 5 layer)

Versi 5 layer (buku modern) : Application, Transport, Network, Link, Physical

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 IP ADDRESS & SUBNET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Struktur : 4 oktet × 8 bit = 32 bit total
           Setiap oktet = 0 sampai 255
           Contoh : 192.168.1.1
                    [Oktet1].[Oktet2].[Oktet3].[Oktet4]

Reserved : Angka 0 → Network address (contoh: 192.168.1.0)
           Angka 255 → Broadcast address (contoh: 192.168.1.255)
           Broadcast = kirim ke SEMUA host dalam jaringan

Total IPv4 : ±4 miliar alamat (2³²) → sekarang sudah hampir habis
Solusi     : IPv6 (128 bit) → jauh lebih banyak

SUBNET MASK :
  255.255.255.0  =  /24  → 24 bit pertama dikunci (tidak berubah)
  Artinya 3 oktet pertama sama di seluruh subnet
  Range : 192.168.66.1 sampai 192.168.66.254

COMMAND CEK IP :
  Windows         → ipconfig
  Linux/UNIX      → ifconfig  ATAU  ip address show  (ip a s)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PRIVATE vs PUBLIC IP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ditetapkan oleh : RFC 1918 → sudah PATEN, berlaku global

RANGE PRIVATE (WAJIB HAPAL) :
  10.0.0.0   – 10.255.255.255    →  10/8
  172.16.0.0 – 172.31.255.255    →  172.16/12
  192.168.0.0– 192.168.255.255   →  192.168/16

Ciri cepat :
  Diawali 10.xxx         → PASTI private
  Diawali 172.16–31.xxx  → PASTI private
  Diawali 192.168.xxx    → PASTI private
  Selain itu             → PUBLIC

Private  : Tidak bisa dijangkau dari Internet langsung
Public   : Terdaftar, bisa diakses dari seluruh Internet
NAT      : Teknologi yang memungkinkan private IP akses Internet
           via router yang punya public IP

IP SPESIAL LAIN :
  127.0.0.1       → Localhost / Loopback = "komputer itu sendiri"
  0.0.0.0         → Semua alamat / tidak ada alamat spesifik
  255.255.255.255 → Broadcast ke semua perangkat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ROUTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Router   : Meneruskan paket data ke jaringan yang tepat
Layer    : Bekerja di layer 3 (Network Layer)
Cara     : Inspeksi IP address → forward ke router berikutnya
           yang membuat paket makin dekat ke tujuan
Fakta    : Paket biasanya melewati BEBERAPA router sebelum sampai tujuan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 UDP vs TCP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keduanya : Protokol transport layer (layer 4)
Port     : Berkisar 1 – 65535 (2¹⁶ - 1), port 0 dicadangkan

UDP (User Datagram Protocol) :
  Sifat    : Connectionless → tidak perlu bangun koneksi dulu
  Konfirm  : TIDAK ADA → tidak tahu apakah paket sampai
  Kecepatan: LEBIH CEPAT
  Cocok    : Streaming, gaming, DNS, VoIP
  Unit data: Datagram

TCP (Transmission Control Protocol) :
  Sifat    : Connection-oriented → wajib bangun koneksi dulu
  Konfirm  : ADA (ACK) → tahu pasti paket sampai
  Sequence : Setiap oktet data punya sequence number
  Kecepatan: Lebih lambat tapi reliable
  Cocok    : Web, email, transfer file
  Unit data: Segment

THREE-WAY HANDSHAKE (cara TCP bangun koneksi) :
  1. SYN     → Client kirim SYN ke server (+ sequence number acak client)
  2. SYN-ACK → Server balas SYN-ACK (+ sequence number acak server)
  3. ACK     → Client kirim ACK → koneksi TERBENTUK → data bisa dikirim

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ENCAPSULATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : Proses setiap layer menambahkan header (kadang trailer)
           ke data yang diterima sebelum dikirim ke layer bawahnya

PROSES (atas ke bawah saat KIRIM) :
  Application Data
  → Transport layer tambah TCP/UDP Header    = TCP Segment / UDP Datagram
  → Network layer tambah IP Header           = IP Packet
  → Link layer tambah Ethernet/WiFi Header
    + Ethernet/WiFi Trailer                  = Frame

PROSES KEBALIKAN saat TERIMA (de-enkapsulasi) :
  Frame → Packet → Segment/Datagram → Application Data

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TELNET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Apa itu  : TELNET = Teletype Network
           Protokol untuk koneksi terminal jarak jauh via TCP
Fungsi   : Terhubung ke server manapun yang listen di TCP port
Risiko   : Tidak terenkripsi → tidak aman untuk produksi

PENGGUNAAN :
  telnet [IP] [PORT]

PORT PENTING YANG DIUJI :
  Port 7   → Echo server   (memantulkan balik semua yang dikirim)
  Port 13  → Daytime server (balas waktu saat ini lalu tutup koneksi)
  Port 80  → HTTP/Web server

REQUEST HTTP via Telnet :
  1. telnet [IP] 80
  2. Ketik : GET / HTTP/1.1   (HARUS KAPITAL SEMUA)
  3. Ketik : Host: [hostname]
  4. Tekan Enter DUA KALI
  Respons sukses : HTTP/1.1 200 OK

CARA KELUAR dari sesi Telnet :
  CTRL + ]  → masuk mode kontrol telnet
  quit      → tutup koneksi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OSI          = Open Systems Interconnection
TCP/IP       = Transmission Control Protocol / Internet Protocol
MAC Address  = Media Access Control → alamat fisik perangkat (6 byte/48 bit)
               Format : a4:c3:f0:85:ac:2d
               3 byte kiri = vendor, 3 byte kanan = alamat unik
Network Seg. = Sekelompok perangkat yang terhubung via medium bersama
Octet        = 8 bit = 1 byte → nilainya 0-255
Subnet       = Pembagian jaringan besar menjadi jaringan kecil
RFC 1918     = Standar yang menetapkan range private IP address
NAT          = Network Address Translation → private IP bisa akses Internet
SYN          = Synchronise → flag TCP untuk mulai koneksi
ACK          = Acknowledgment → flag TCP untuk konfirmasi terima
Loopback     = 127.0.0.1 → alamat "diri sendiri"
Broadcast    = Kirim ke semua host dalam jaringan (x.x.x.255)
Encapsulation= Proses pembungkusan data dengan header di setiap layer
Frame        = Unit data di layer 2 (Ethernet/WiFi)
Packet       = Unit data di layer 3 (IP)
Segment      = Unit data TCP di layer 4
Datagram     = Unit data UDP di layer 4
```