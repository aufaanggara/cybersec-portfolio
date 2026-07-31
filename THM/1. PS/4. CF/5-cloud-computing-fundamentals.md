```
=== Cloud Computing - Resume Materi ===
[26 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU CLOUD COMPUTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Menggunakan sumber daya komputasi (server, storage,
           jaringan) melalui internet, bukan dari komputer sendiri
Analogi  : Seperti memindahkan file dari laptop ke Google Drive
           → bisa diakses dari mana saja
Manfaat  : Lebih mudah diakses, lebih andal, siap berkembang
Dasar    : Dibangun di atas Virtualization & Containers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 EVOLUSI SERVER → CLOUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1960s-2000s │ Physical Servers Era
            │ Server fisik di gedung, 1 server = 1 job
            │ Mahal, lambat dikembangkan

1999-2006   │ Virtualization
            │ Banyak VM di 1 mesin fisik
            │ Hardware lebih efisien, provisioning lebih cepat

2003-2006   │ Automation & Remote Management
            │ Server dikelola via internet
            │ Infrastruktur makin cepat & fleksibel

2006        │ Cloud Computing (AWS Launch)
            │ Sewa VM & storage sesuai kebutuhan
            │ Tidak perlu punya hardware, elastic scaling

2012-kini   │ Modern Cloud Era
            │ AWS, Azure, Google Cloud
            │ Fokus pada apps bukan server, skala global

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MANFAAT & KARAKTERISTIK CLOUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scalability        → Naik/turun kapasitas sesuai kebutuhan
On-demand          → Buat/hapus server instan, tanpa tunggu hardware
Pay as you use     → Bayar sesuai pemakaian, bukan biaya di muka
Security           → Penyedia cloud lindungi infrastruktur
High Availability  → Aplikasi tetap jalan walau sebagian sistem gagal
Global Access      → Bisa diakses pengguna dari seluruh dunia

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TIPE DEPLOYMENT CLOUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Public Cloud  → Dipakai bersama banyak orang/perusahaan via internet
                Cocok : startup, website, apps global
                Kelebihan : murah, mudah scale, no infra management

Private Cloud → Khusus 1 perusahaan saja
                Cocok : bank, healthcare, pemerintah
                Kelebihan : kontrol penuh, keamanan & compliance tinggi

Hybrid Cloud  → Gabungan public + private, bisa saling berbagi data
                Cocok : e-commerce (data sensitif private,
                        traffic tinggi scale ke public)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MODEL LAYANAN CLOUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IaaS  → Infrastructure as a Service
        Sewa server virtual, storage, jaringan
        Kamu kelola : OS + aplikasi
        Provider kelola : hardware fisik
        Analogi : Apartemen KOSONG
                  → kamu pilih furnitur & urus sendiri

PaaS  → Platform as a Service
        Provider kelola infra + OS
        Kamu fokus : bangun & deploy aplikasi saja
        Analogi : Apartemen SEMI-FURNISHED
                  → fasilitas dasar sudah ada, tinggal huni

SaaS  → Software as a Service
        Pakai aplikasi lengkap via browser/app
        Provider kelola SEGALANYA
        Contoh : Gmail, Zoom
        Analogi : HOTEL
                  → semua sudah siap, tinggal pakai

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TERMINOLOGI AWS (EC2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EC2           = Virtual computer/server di cloud
                Punya CPU, RAM, bisa jalankan aplikasi
Instance Type = Ukuran power VM (contoh: t3.micro, m5.large)
                Lebih besar = lebih powerful = lebih mahal
Region        = Lokasi geografis server berada
                Contoh : us-east-1 (N. Virginia), Europe

Contoh harga :
  t3.micro  = 10 kredit/bulan  → kecil, ringan
  m5.large  = 70 kredit/bulan  → besar, powerful

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PRAKTIK DEPLOY (SIMULASI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tujuan : Host aplikasi pelatihan cyber security
Model  : IaaS → butuh akses penuh ke OS untuk install tools

VM yang dibuat :
  application-interface  │ t3.micro │ 10 kredit/bulan
  study-machine-1        │ m5.large │ 70 kredit/bulan
  study-machine-2        │ m5.large │ 70 kredit/bulan

Total saat semua running = 170 kredit/bulan

Optimasi biaya :
  → Stop study-machine-1 & study-machine-2
  → Mesin stopped = 0 biaya
  → Total turun jadi 30 kredit/bulan

Pelajaran : Di cloud, kamu HANYA bayar yang sedang berjalan
            Stop VM yang tidak dipakai = hemat biaya besar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 VENDOR CLOUD UTAMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AWS (Amazon)  → Pemimpin industri, jangkauan global terluas
Azure (MS)    → Kuat di enterprise & hybrid cloud
GCP (Google)  → Unggul di data analytics, AI, machine learning
Alibaba Cloud → Pemain utama di Asia
IBM Cloud     → Fokus hybrid cloud & solusi AI bisnis
Oracle Cloud  → Fokus enterprise apps & database

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERUSAHAAN BESAR & PENGGUNAAN CLOUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Netflix    → Seluruh platform di AWS, stream ke jutaan user sekaligus
Spotify    → Tangani jutaan lagu & user, scale cepat saat rilis fitur baru
Instagram  → Simpan & kirim foto/video masif ke seluruh dunia
Toko Online→ Tangani lonjakan traffic Black Friday tanpa beli infra permanen

Alasan utama : scale mudah + hemat biaya + andal +
               fokus kembangkan produk, bukan urus hardware

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Instance       = Satu unit VM/server virtual yang berjalan di cloud
Scalability    = Kemampuan naik/turun kapasitas sesuai kebutuhan
Elastic        = Bisa berkembang & menyusut otomatis
Provisioning   = Proses menyiapkan & mengaktifkan server/resource
Shared Infra   = Infrastruktur fisik yang dipakai bersama banyak user
High Avail.    = Sistem tetap jalan meski ada bagian yang gagal
Pay-as-you-go  = Model bayar sesuai penggunaan, bukan biaya tetap
Deployment     = Proses meluncurkan/menjalankan aplikasi ke server
Billing        = Sistem penagihan berdasarkan resource yang digunakan
Stopped VM     = VM yang dimatikan sementara → tidak dikenakan biaya
```