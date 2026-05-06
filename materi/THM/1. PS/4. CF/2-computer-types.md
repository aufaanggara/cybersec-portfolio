```
=== Computer Types - Resume Materi ===

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU KOMPUTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Mesin yang memproses informasi sesuai instruksi
Fakta    : Komputer tidak hanya laptop/HP — ada di pintu, kulkas,
           lampu, mesin kopi, bel pintu, dll
Prinsip  : "There is no best computer. There is only the right
           tool for the job!"
           (Tidak ada komputer terbaik, hanya alat yang tepat
           untuk pekerjaan yang tepat)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KOMPUTER YANG KAMU DUDUK DI DEPANNYA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Laptop
  Layar & Keyboard : Ada
  Tujuan Utama     : Komputasi sehari-hari yang portabel
  Kelebihan        : Mudah dibawa kemana-mana
  Kelemahan        : Mudah panas, performa terbatas
  Alasan           : Ukuran kecil + baterai = sulit jaga
                     suhu → performa dikompromikan

Desktop
  Layar & Keyboard : Ada
  Tujuan Utama     : Performa stabil di lokasi tetap
  Kelebihan        : Pendinginan lebih baik, konsisten
  Kelemahan        : Tidak bisa dipindah-pindah
  Alasan           : Pakai listrik stopkontak → bebas
                     batasi performa untuk pendinginan

Workstation
  Layar & Keyboard : Ada
  Tujuan Utama     : Presisi & keandalan untuk tugas profesional
  Kelebihan        : Akurat untuk simulasi, 3D model, komputasi berat
  Kelemahan        : Mahal, biasanya di tempat tetap
  Alasan           : Komponen khusus → kurangi error di
                     komputasi panjang/kompleks

Server
  Layar & Keyboard : TIDAK ADA
  Tujuan Utama     : Melayani banyak user lewat jaringan
  Kelebihan        : Jalan terus 24/7, layani banyak user sekaligus
  Kelemahan        : Tidak dioperasikan langsung oleh manusia
  Alasan           : Dirancang untuk keandalan, bukan interaksi

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KOMPUTER TERSEMBUNYI DI BENDA SEHARI-HARI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Smartphone
  Apa itu  : Komputer seukuran saku
  Fokus    : Daya tahan baterai + konektivitas
  Contoh   : iPhone, Android phone

Tablet
  Apa itu  : Komputer layar sentuh ukuran lebih besar
  Fokus    : Touch-first (utamakan layar sentuh)
  Contoh   : iPad, drawing tablet

IoT Device (Internet of Things)
  Apa itu  : Perangkat terhubung jaringan dengan 1 fungsi khusus
  Fokus    : Kirim data / terima perintah lewat jaringan
  Contoh   : Thermostat, smart doorbell, fitness tracker

Embedded Computer
  Apa itu  : Komputer yang ditanam di dalam perangkat lain
  Fokus    : Kerjakan 1 tugas diam-diam di dalam mesin
  Contoh   : Controller mesin kopi, sensor pintu otomatis,
             chip dimmer lampu
  Fakta    : Bekerja bertahun-tahun tanpa ada yang sadar
             keberadaannya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERBEDAAN KUNCI: IoT vs EMBEDDED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Persamaan  : Keduanya bisa kecil dan satu fungsi
Perbedaan  : KONEKTIVITAS

IoT        → TERHUBUNG ke jaringan
             → Melaporkan data / menerima perintah dari luar
             → Contoh : thermostat kirim data suhu ke HP

Embedded   → TIDAK HARUS terhubung ke apapun
             → Bekerja sendiri di dalam mesin
             → Contoh : komputer di rangka pintu otomatis
                        yang deteksi gerakan & buka pintu

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MENGAPA KOMPUTER HADIR BERBEDA-BEDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prinsip Utama : "Every design is a trade-off"
                (Setiap desain adalah kompromi)

Trade-off 1 → MOBILITAS vs PERFORMA
              Makin kecil & portabel = makin terbatas performanya
              Laptop harus jaga suhu di bodi kecil → melambat

Trade-off 2 → KEANDALAN vs BIAYA
              Server pakai redundansi (power supply & disk cadangan)
              → Hindari kegagalan → tapi mahal

Trade-off 3 → TUJUAN menentukan SEGALANYA
              HP     = kamu sentuh langsung
              Server = kamu minta informasi darinya
              IoT    = bekerja diam tanpa minta perhatian

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP SERVER: REDUNDANSI & UPTIME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Masalah      : Server harus jalan 24/7 → tidak boleh mati
               karena 1 kerusakan kecil

Solusi       : REDUNDANSI = sistem berlapis cadangan

Skenario Power :
  Both On  → Power A ✅ Power B ✅ → Server ONLINE  ✅
  One Off  → Power A ❌ Power B ✅ → Server ONLINE  ✅ (redundansi bekerja!)
  Both Off → Power A ❌ Power B ❌ → Server OFFLINE ❌

Pelajaran    : "Redundant power reduces a single failure point"
               Uptime makin tinggi jika redundansi +
               backup + monitoring digabungkan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING YANG WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Portable         = Bisa dibawa-bawa, tidak terikat satu tempat
Sustained Perf.  = Performa yang stabil dalam waktu lama
Redundansi       = Sistem cadangan berlapis agar tidak ada
                   "satu titik kegagalan" yang matikan segalanya
Single Fail Point= Satu komponen yang jika rusak → seluruh
                   sistem mati
Uptime           = Berapa lama sistem tetap aktif & bisa diakses
Trade-off        = Kompromi — dapat A tapi korbankan B
IoT              = Internet of Things — benda sehari-hari yang
                   terhubung internet
Embedded System  = Komputer tersembunyi di dalam perangkat lain
Connectivity     = Kemampuan terhubung ke jaringan/internet
Mobility         = Kemampuan untuk berpindah-pindah tempat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 TABEL CEPAT — MANA YANG COCOK?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Butuh dibawa kemana-mana?      → LAPTOP / SMARTPHONE
Kerja berat di satu tempat?    → DESKTOP
Simulasi / 3D / sains?         → WORKSTATION
Layani banyak user 24/7?       → SERVER
Pantau suhu rumah lewat HP?    → IoT DEVICE
Sensor di dalam mesin?         → EMBEDDED COMPUTER
Layar sentuh besar?            → TABLET
```