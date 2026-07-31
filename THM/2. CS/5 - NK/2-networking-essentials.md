```
=== Networking Essentials - Resume Materi ===
[28 Apr 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 DHCP — Dynamic Host Configuration Protocol
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Konfigurasi jaringan otomatis saat perangkat terhubung
Yang dikonfigurasi :
  → IP address + subnet mask
  → Router / gateway
  → DNS server

Protokol : Application-level, berbasis UDP
  → Server listen di port UDP 67
  → Client kirim dari port UDP 68

Keuntungan otomatisasi :
  → Tidak perlu konfigurasi manual tiap perangkat
  → Cegah konflik IP (dua perangkat IP sama)

Default  : Smartphone & laptop pakai DHCP secara default

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PROSES DORA (4 Langkah DHCP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
D → Discover    : Client broadcast DHCPDISCOVER cari server
O → Offer       : Server balas DHCPOFFER tawarkan IP
R → Request     : Client balas DHCPREQUEST terima tawaran
A → Acknowledge : Server balas DHCPACK konfirmasi IP assigned

Catatan penting :
  → Saat Discover & Request, client belum punya IP
  → Source IP    = 0.0.0.0   (belum punya IP)
  → Destination  = 255.255.255.255 (broadcast ke semua)
  → MAC broadcast = ff:ff:ff:ff:ff:ff

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ARP — Address Resolution Protocol
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Terjemahkan IP address → MAC address
Mengapa  : Komunikasi di layer 2 (Ethernet/WiFi) butuh MAC address,
           bukan IP address
Layer    : Dianggap layer 2 (MAC), tapi support operasi IP (layer 3)
           → ARP = jembatan layer 3 ke layer 2

MAC address : 48-bit, format hexadecimal
              Contoh : 44:DF:65:D8:FE:6C

Cara kerja :
  → ARP Request  : broadcast ke ff:ff:ff:ff:ff:ff
                   "Who has IP x.x.x.x? Tell x.x.x.x"
  → ARP Reply    : unicast balik ke penanya
                   "IP x.x.x.x is at MAC xx:xx:xx:xx:xx:xx"

Penting    : ARP TIDAK dibungkus UDP/IP
             → Langsung dikemas dalam Ethernet frame
             → Type field = 0x0806

Tools baca ARP :
  tshark   → tampilkan "Who has / is at"
  tcpdump  → tampilkan "Request / Reply"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ICMP — Internet Control Message Protocol
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Diagnostik jaringan & pelaporan error
Bukan untuk : kirim data biasa (file, web)

── PING ──────────────────────────────
Fungsi   : Cek konektivitas & ukur RTT (Round-Trip Time)
Cara     : Kirim ICMP Echo Request → tunggu Echo Reply

Type 8   = Echo Request  (dikirim client)
Type 0   = Echo Reply    (dikirim server/target)

Output ping :
  → bytes      = ukuran data yang dikirim
  → ttl        = Time-to-Live sisa
  → time       = RTT dalam milidetik
  → Statistik  : min/avg/max/mdev RTT + % packet loss

Switch ping :
  -c [n]  → stop setelah kirim n paket (Linux)

Kenapa bisa gagal :
  → Target offline / mati
  → Firewall memblokir paket ICMP

── TRACEROUTE ────────────────────────
Fungsi   : Lacak rute / jalur paket dari source ke destination
           Setiap router yang dilewati akan terungkap

Cara kerja (pakai TTL) :
  → TTL = jumlah maksimum router yang boleh dilewati paket
  → Setiap router kurangi TTL sebesar 1
  → Ketika TTL = 0 → router buang paket &
    kirim ICMP Type 11 (Time Exceeded) ke pengirim
  → Traceroute manfaatkan ini untuk ungkap tiap router

Nama perintah :
  Linux/UNIX  → traceroute
  Windows     → tracert

Output traceroute :
  → Nomor hop  = urutan router
  → Nama/IP    = identitas router
  → 3x waktu   = RTT ke router tsb (3 probe)
  → * * *      = router tidak merespons (blokir ICMP)

Catatan :
  → Rute bisa berubah setiap kali dijalankan ulang
  → Router ISP bisa ungkap IP privat atau publik mereka
  → Bisa cari lokasi geografis router dari IP publiknya

ICMP Types penting :
  Type 0  = Echo Reply
  Type 8  = Echo Request
  Type 11 = Time Exceeded (dipakai traceroute)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ROUTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Tentukan jalur terbaik untuk kirim paket
           antar jaringan yang berbeda
Cara     : Router pakai routing table & algoritma routing
           untuk pilih link yang tepat

TTL      : Field di IP header, cegah paket loop selamanya
           Setiap hop kurangi 1, sampai 0 paket dibuang

Routing Protocols (kenali nama & fungsinya) :

OSPF  → Open Shortest Path First
        Router saling share peta topologi jaringan
        Hitung jalur PALING EFISIEN
        Cocok : jaringan besar enterprise

EIGRP → Enhanced Interior Gateway Routing Protocol
        Milik CISCO (proprietary)
        Pertimbangkan bandwidth & delay dalam pilih rute
        Cocok : jaringan Cisco

BGP   → Border Gateway Protocol
        Protokol UTAMA di Internet
        Hubungkan antar jaringan berbeda (antar ISP)
        Pastikan data bisa lintas banyak jaringan

RIP   → Routing Information Protocol
        Paling SEDERHANA
        Pilih rute berdasarkan jumlah hop terkecil
        Cocok : jaringan KECIL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 NAT — Network Address Translation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi   : Izinkan BANYAK IP privat berbagi SATU IP publik
Masalah  : IPv4 max 4 miliar alamat → hampir habis
Solusi   : NAT → hemat IP publik

Cara kerja :
  → Router NAT kelola tabel translasi
  → Tabel petakan : IP privat + port → IP publik + port baru
  → Paket keluar : IP privat diganti IP publik
  → Paket masuk  : IP publik diterjemahkan balik ke IP privat

Contoh tabel NAT :
  Internal             | External
  192.168.0.129:15401  | 212.3.4.5:19273
  192.168.0.137:27912  | 212.3.4.5:32759
  192.168.0.112:38192  | 212.3.4.5:41251

Batas NAT :
  → Port TCP range = 0 - 65535
  → Maks ~65.000 koneksi simultan per 1 IP publik

Perbedaan dengan routing :
  → Routing  = alami, forward paket ke tujuan
  → NAT      = harus track & terjemahkan semua koneksi aktif

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 BROADCAST ADDRESS — WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IP broadcast  : 255.255.255.255  → kirim ke SEMUA host di jaringan
MAC broadcast : ff:ff:ff:ff:ff:ff → kirim ke SEMUA perangkat di LAN
Keduanya      : semua bit = 1 (nilai maksimum)
Dipakai oleh  : DHCP Discover, DHCP Request, ARP Request

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RTT          = Round-Trip Time, waktu bolak-balik paket
TTL          = Time-to-Live, batas hop paket sebelum dibuang
Hop          = satu lompatan paket melewati satu router
MAC address  = alamat fisik perangkat, 48-bit hexadecimal
IP privat    = alamat internal jaringan lokal (tidak routable di Internet)
IP publik    = alamat yang dikenali Internet
Broadcast    = kirim ke semua perangkat sekaligus
Unicast      = kirim ke satu perangkat spesifik
mdev         = mean deviation, ukuran variasi/konsistensi RTT
Packet loss  = persentase paket yang hilang/tidak sampai
Port         = nomor identifikasi layanan/koneksi (0-65535)
```