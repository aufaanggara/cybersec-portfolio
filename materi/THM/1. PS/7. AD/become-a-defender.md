# Ringkasan - Become a Defender

```
=== Defensive Security - Resume Materi ===
[27 Mar 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU DEFENSIVE SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi : Memahami apa yang perlu dilindungi & menerapkan
           langkah keamanan untuk MENCEGAH, MENDETEKSI,
           dan MEMITIGASI dampak serangan
Tujuan   : Siap menghadapi insiden & merespons saat terjadi
Pelaku   : Blue Team (kelompok defender keamanan siber)
Analogi  : Seperti penjaga kota — harus tahu tata letak,
           awasi masalah, dan tahu cara merespons
Beda     : Offensive (Red Team) = cari cara masuk
           Defensive (Blue Team) = pastikan tidak ada yang masuk

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CIA TRIAD (FONDASI KEAMANAN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
C = Confidentiality → Data hanya bisa diakses yang berwenang
I = Integrity       → Data tidak boleh diubah tanpa izin
A = Availability    → Sistem harus selalu tersedia saat dibutuhkan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 5 KONSEP FONDASI DEFENSIVE SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Prevention (Pencegahan)
   → Hentikan serangan SEBELUM terjadi
   → Cara : Firewall, antivirus, regular patching

2. Detection (Deteksi)
   → Monitor sistem untuk identifikasi aktivitas mencurigakan
   → Cara : Logs, alerts, security tools

3. Mitigation (Mitigasi)
   → Ambil tindakan SAAT insiden untuk batasi kerusakan
   → Cara : Blokir traffic, isolasi sistem, nonaktifkan akun

4. Analysis (Analisis)
   → Selidiki APA yang terjadi, BAGAIMANA, sistem mana terdampak
   → Cara : Tinjau logs & bukti-bukti lainnya

5. Response & Improvement (Respons & Peningkatan)
   → Pulihkan dari insiden & tingkatkan pertahanan
   → Tujuan : Kurangi risiko serangan serupa di masa depan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 MEMAHAMI LINGKUNGAN (SCOPE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prinsip  : Kamu TIDAK BISA melindungi apa yang tidak kamu ketahui
Scope    : Defender hanya lindungi milik organisasi/klien,
           BUKAN semua yang ada di internet
Isi scope: Perangkat harian + Server + Jaringan penghubung

TABEL ANALOGI KOTA vs KEAMANAN NYATA:
┌─────────────────────────────┬──────────────────────────────┐
│ Pertanyaan Defender         │ Setara Keamanan Nyata        │
├─────────────────────────────┼──────────────────────────────┤
│ Apa yang dilindungi?        │ Server, data, workstation,   │
│ (Sistem & Infrastruktur)    │ users                        │
├─────────────────────────────┼──────────────────────────────┤
│ Bisakah kamu melihatnya?    │ Logs, network traffic,       │
│ (Visibilitas)               │ alerts                       │
├─────────────────────────────┼──────────────────────────────┤
│ Apa perilaku mencurigakan?  │ Repeated logins,             │
│                             │ unusual IP addresses         │
├─────────────────────────────┼──────────────────────────────┤
│ Bagaimana hentikan ancaman? │ Firewall rules,              │
│                             │ IP address blocking          │
└─────────────────────────────┴──────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KOMPONEN INFRASTRUKTUR KLIEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌──────────────────┬───────────────────────────────┬────────────┐
│ Komponen         │ Fungsi                        │ Analogi    │
├──────────────────┼───────────────────────────────┼────────────┤
│ Employee Devices │ Tempat kerja & akses sumber   │ Rumah      │
│                  │ daya perusahaan               │            │
├──────────────────┼───────────────────────────────┼────────────┤
│ Web Server       │ Host website/aplikasi         │ Toko /     │
│                  │ yang diakses user             │ Gedung pub │
├──────────────────┼───────────────────────────────┼────────────┤
│ Mail Server      │ Kirim & terima email          │ Kantor pos │
│                  │ organisasi                    │            │
├──────────────────┼───────────────────────────────┼────────────┤
│ Firewall         │ Kontrol traffic masuk/keluar  │ Gerbang    │
│                  │                               │ kota       │
├──────────────────┼───────────────────────────────┼────────────┤
│ Internet         │ Jaringan eksternal di luar    │ Di luar    │
│                  │ kendali organisasi            │ kota       │
└──────────────────┴───────────────────────────────┴────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 THE DEFENDER MINDSET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prinsip  : Lihat sistem sebagai RANTAI, bukan bagian terpisah
           Penyerang kompromikan 1 aset → pindah ke aset berikutnya
Contoh   : Email jahat → workstation karyawan → curi kredensial
           → akses mail server → curi data di database server

4 PRINSIP UTAMA DEFENDER:
1. Threat Anticipation → Tanya "bagaimana jika?" untuk tiap sistem
                         Bayangkan jalur realistis yang diambil penyerang
2. Attack Awareness    → Pelajari rantai serangan & framework umum
                         Serangan ikuti tahapan yang bisa dikenali
3. Risk Prioritization → Tidak semua sistem risikonya sama
                         Identifikasi sistem & target bernilai tinggi
4. Continuous Adaptation→ Pertahanan BUKAN pengaturan satu kali
                          Ancaman terus berkembang, teknik berubah

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 PERTAHANAN PER KOMPONEN (LAYERED)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prinsip  : Tidak ada 1 alat yang bisa hentikan semua serangan
           Gunakan PERTAHANAN BERLAPIS agar penyerang sulit berhasil

┌──────────────────┬───────────────────────────┬──────────────────────────┐
│ Komponen         │ Risiko                    │ Pertahanan               │
├──────────────────┼───────────────────────────┼──────────────────────────┤
│ Employee Devices │ Klik link jahat /         │ Antivirus +              │
│                  │ download software unsafe  │ Update rutin             │
├──────────────────┼───────────────────────────┼──────────────────────────┤
│ Web Server       │ Penyerang coba            │ Hanya izinkan traffic    │
│                  │ terobos website           │ aman + enkripsi          │
├──────────────────┼───────────────────────────┼──────────────────────────┤
│ Mail Server      │ Email jahat /             │ Spam filter +            │
│                  │ menipu                    │ Scan lampiran            │
├──────────────────┼───────────────────────────┼──────────────────────────┤
│ Firewall         │ Orang asing dari          │ Firewall rules +         │
│                  │ internet coba masuk       │ Blokir IP berbahaya      │
├──────────────────┼───────────────────────────┼──────────────────────────┤
│ Internet         │ Ancaman eksternal         │ Batasi inbound traffic + │
│                  │ datang dari sini          │ Monitor aktivitas        │
└──────────────────┴───────────────────────────┴──────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 JALUR KARIR DEFENSIVE SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SOC (Security Operations Center)
→ Monitor jaringan & sistem
→ Deteksi & selidiki aktivitas mencurigakan / alert keamanan

Threat Intelligence
→ Riset ancaman, penyerang & tren terkini
→ Bantu organisasi persiapkan diri dari potensi serangan

DFIR (Digital Forensics & Incident Response)
→ Selidiki insiden keamanan
→ Pahami BAGAIMANA serangan terjadi
→ Pulihkan sistem yang terdampak

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH PENTING WAJIB HAPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Blue Team          = Kelompok defender keamanan siber
Client Infra       = Jaringan, server, perangkat, aplikasi milik
                     organisasi yang butuh perlindungan
Visibility         = Kemampuan melihat & memantau aktivitas sistem
Threat             = Bahaya potensial (hacker/malware) yang bisa
                     merusak sistem atau data
Prevention         = Hentikan ancaman sebelum terjadi
Detection          = Identifikasi ancaman/aktivitas mencurigakan
Mitigation         = Kurangi/hentikan dampak ancaman yang terdeteksi
Risk               = Kemungkinan & dampak ancaman yang berhasil
                     merugikan organisasi
Attack Surface     = Semua titik/celah yang bisa diserang di sistem
Layered Defense    = Pertahanan berlapis — tidak bergantung 1 alat
Logs               = Catatan aktivitas sistem untuk audit & deteksi
Patching           = Pembaruan software untuk tutup celah keamanan
Firewall Rules     = Aturan yang tentukan traffic mana boleh lewat
Incident Response  = Respons terstruktur saat insiden keamanan terjadi
```

# Defensive Security — TryHackMe Pre Security Path

---

## 1 — What Is Defensive Security

Defensive Security adalah cabang keamanan siber yang berfokus pada **memahami apa yang perlu dilindungi** dan menerapkan langkah-langkah keamanan untuk mencegah, mendeteksi, dan memitigasi dampak dari potensi serangan. Berbeda dengan offensive security yang berusaha menerobos masuk, defensive security justru berusaha memastikan tidak ada yang bisa masuk tanpa izin — dan jika pun terjadi insiden, sistem sudah siap merespons.

Para defender bekerja untuk mendapatkan **visibilitas** ke dalam sistem, mengidentifikasi titik-titik lemah, dan memastikan sistem tetap tersedia serta terlindungi. Semua ini selaras langsung dengan prinsip **CIA Triad** yang menjadi fondasi keamanan informasi, yaitu Confidentiality (data hanya bisa diakses yang berwenang), Integrity (data tidak boleh diubah sembarangan), dan Availability (sistem harus selalu bisa diakses saat dibutuhkan).

Para defender sering disebut sebagai **Blue Team**, dan mereka perlu memahami cara kerja penyerang — bukan untuk menyerang, tapi agar bisa membangun pertahanan yang efektif. Dengan memahami bagaimana penyerang berpikir, apa yang mereka targetkan, dan bagaimana serangan biasanya berlangsung, Blue Team bisa mengidentifikasi infrastruktur kritis dan menerapkan perlindungan yang tepat.

Tujuan akhir dari defensive security bukan hanya mencegah serangan, tapi juga **siap menghadapi insiden dan merespons dengan cepat** ketika insiden tersebut benar-benar terjadi.

---

## 2 — Understanding Your Environment

### Mengapa Memahami Lingkungan Itu Penting

Sebelum bisa melindungi apapun, seorang defender harus punya **visibilitas yang jelas** tentang apa yang ada dalam lingkungan yang menjadi tanggung jawabnya — apa saja sistemnya, bagaimana mereka saling terhubung, dan di mana letak titik-titik rentannya. Analogi yang dipakai dalam materi ini sangat tepat: bayangkan infrastruktur klien seperti sebuah **kota yang sibuk**. Sama seperti penjaga kota yang harus tahu tata letak kota, mengawasi masalah, dan tahu cara merespons ancaman — defender harus memahami lingkungan mereka secara menyeluruh sebelum bisa menjaganya tetap aman.

### Tabel Analogi Kota vs Konsep Keamanan Nyata

Materi ini menggunakan tabel analogi untuk menjelaskan bagaimana pertanyaan-pertanyaan dasar dalam defensive security diterjemahkan ke dunia nyata:

- **Apa yang kamu lindungi?** — Di kota analoginya adalah rumah, gedung, dan orang-orang. Di dunia nyata artinya server klien, data, workstation, dan pengguna yang mengakses sistem.
- **Bisakah kamu melihat apa yang kamu lindungi?** — Di kota analoginya adalah kamera pengawas, laporan, dan patroli. Di dunia nyata artinya logs sistem, network traffic, dan alerts yang muncul saat ada aktivitas mencurigakan.
- **Apa yang dikategorikan sebagai perilaku mencurigakan?** — Di kota analoginya adalah percobaan membuka pintu yang terkunci atau mobil yang berputar-putar. Di dunia nyata artinya login berulang yang gagal atau alamat IP yang tidak biasa mengakses sistem.
- **Bagaimana cara menghentikan ancaman?** — Di kota analoginya adalah polisi, pemblokiran jalan, dan jam malam. Di dunia nyata artinya firewall rules dan pemblokiran IP address.

### 5 Konsep Fondasi Defensive Security

Setelah memahami apa yang ada di lingkungan, para defender mengorganisir pekerjaannya di sekitar lima konsep fundamental yang berlaku di hampir semua lingkungan:

1. **Prevention (Pencegahan)** — Menempatkan kontrol keamanan untuk menghentikan serangan sebelum terjadi. Contoh konkretnya adalah firewall yang memblokir traffic berbahaya, antivirus yang mendeteksi malware, dan regular patching yang menutup celah keamanan sebelum dieksploitasi penyerang.
2. **Detection (Deteksi)** — Memonitor sistem dan jaringan secara aktif untuk mengidentifikasi aktivitas mencurigakan atau berbahaya. Ini dilakukan melalui logs yang mencatat semua aktivitas, alerts yang muncul otomatis, dan berbagai security tools yang menganalisis pola traffic.
3. **Mitigation (Mitigasi)** — Mengambil tindakan cepat selama insiden berlangsung untuk membatasi kerusakan agar tidak meluas. Contohnya adalah memblokir traffic dari IP penyerang, mengisolasi sistem yang sudah terkompromikan, atau menonaktifkan akun yang dicuri kredensialnya.
4. **Analysis (Analisis)** — Menyelidiki secara mendalam apa yang terjadi, bagaimana hal itu bisa terjadi, dan sistem mana saja yang terdampak. Ini dilakukan dengan meninjau logs dan semua bukti digital yang tersedia setelah insiden.
5. **Response and Improvement (Respons dan Peningkatan)** — Memulihkan sistem dari insiden dan yang terpenting, meningkatkan pertahanan agar kejadian serupa tidak terulang di masa depan. Tahap ini menutup siklus dan memulai kembali dengan pertahanan yang lebih kuat.

### Scope: Apa yang Menjadi Tanggung Jawabmu?

Defender tidak bertanggung jawab untuk melindungi semua hal yang ada di internet. Mereka fokus pada **apa yang menjadi milik organisasi atau klien mereka** saja. Ini mencakup perangkat yang digunakan karyawan sehari-hari, server yang meng-host aplikasi dan data, serta jaringan yang menghubungkan semua sistem tersebut. Sebelum pertahanan apapun bisa diterapkan, defender harus terlebih dahulu memahami sistem apa saja yang ada, untuk apa digunakan, dan bagaimana mereka saling berhubungan dalam keseluruhan lingkungan.

### Komponen Infrastruktur Klien

Berikut adalah komponen-komponen utama yang biasanya ada dalam infrastruktur klien beserta fungsi dan analogi kotanya:

- **Employee Devices** — Perangkat tempat karyawan bekerja dan mengakses sumber daya perusahaan. Analoginya seperti rumah — tempat aktivitas utama berlangsung.
- **Web Server** — Server yang meng-host website atau aplikasi yang diakses oleh pengguna. Analoginya seperti toko atau gedung publik — tempat orang datang untuk mendapatkan layanan.
- **Mail Server** — Server yang mengirim dan menerima email untuk seluruh organisasi. Analoginya seperti kantor pos — pusat komunikasi surat-menyurat.
- **Firewall** — Sistem yang mengontrol traffic apa yang diizinkan masuk atau keluar dari jaringan. Analoginya seperti gerbang kota — penjaga yang memutuskan siapa boleh masuk dan keluar.
- **Internet** — Jaringan eksternal yang tidak dikontrol oleh organisasi. Analoginya seperti wilayah di luar kota — area yang tidak bisa dikontrol dan menjadi sumber ancaman eksternal.

---

## 3 — Defending Your Environment

### The Defender Mindset

Memahami lingkungan saja tidak cukup. Seorang defender harus bisa **berpikir seperti penyerang** — memahami bagaimana mereka bergerak, apa yang mereka incar, dan bagaimana mereka memanfaatkan satu celah untuk mencapai tujuan yang lebih besar. Kunci utamanya adalah melihat sistem bukan sebagai bagian-bagian terpisah, melainkan sebagai **rantai yang saling terhubung**.

Para penyerang jarang menarget satu sistem saja. Mereka mengkompromikan satu aset, lalu berpindah ke aset berikutnya, dan terus membangun hingga mencapai tujuan akhir mereka. Contoh nyata yang dibahas dalam materi: sebuah lampiran email berbahaya bisa memengaruhi workstation karyawan. Dari workstation itu, penyerang mencuri username dan password. Dengan kredensial itu mereka mengakses mail server. Dan dari mail server, mereka akhirnya bisa mencapai database server yang menyimpan data sensitif. Setiap langkah membangun dari langkah sebelumnya — dan setiap langkah juga merupakan **kesempatan bagi defender untuk memotong rantai serangan tersebut**.

### 4 Prinsip Utama Defender Mindset

1. **Threat Anticipation (Antisipasi Ancaman)** — Tinjau setiap sistem yang dilindungi dan tanyakan secara aktif "bagaimana jika?" Bayangkan jalur-jalur realistis yang mungkin diambil penyerang untuk mencapai tujuan mereka, lalu persiapkan pertahanan di jalur-jalur tersebut sebelum penyerang memanfaatkannya.
2. **Attack Awareness (Kesadaran Serangan)** — Serangan siber biasanya tidak acak — mereka mengikuti tahapan-tahapan yang dapat dikenali. Dengan mempelajari rantai serangan umum dan framework yang digunakan penyerang, defender bisa lebih cepat mengenali tanda-tanda serangan sebelum mencapai tahap kritis.
3. **Risk Prioritization (Prioritisasi Risiko)** — Tidak semua bagian sistem membawa risiko yang sama besarnya. Seorang defender harus bisa mengidentifikasi mana sistem dan target yang bernilai tinggi sehingga alokasi sumber daya pertahanan bisa difokuskan di tempat yang paling penting.
4. **Continuous Adaptation (Adaptasi Berkelanjutan)** — Pertahanan bukan sesuatu yang dipasang sekali lalu ditinggalkan. Ancaman terus berkembang, teknik serangan berubah, dan kerentanan baru terus ditemukan. Defender harus selalu memperbarui pengetahuan dan pertahanannya secara konsisten.

### Pertahanan Berlapis Per Komponen

Tidak ada satu alat pun yang bisa menghentikan semua jenis serangan. Prinsip yang digunakan dalam defensive security adalah **pertahanan berlapis** — seperti memiliki kunci di pintu, penjaga di gerbang, dan alarm di dalam gedung secara bersamaan. Semakin banyak lapisan pertahanan, semakin sulit penyerang untuk berhasil.

Berikut adalah pertahanan yang diterapkan untuk tiap komponen infrastruktur:

- **Employee Devices** — Risikonya adalah karyawan yang tidak sengaja mengklik tautan berbahaya atau mengunduh software tidak aman. Pertahanannya adalah antivirus untuk mendeteksi program berbahaya dan pembaruan software rutin untuk menutup celah keamanan.
- **Web Server** — Risikonya adalah penyerang yang mencoba menerobos masuk ke website atau aplikasi. Pertahanannya adalah hanya mengizinkan traffic yang aman masuk dan menggunakan komunikasi terenkripsi untuk melindungi data yang dikirim.
- **Mail Server** — Risikonya adalah email berbahaya atau email phishing yang menipu karyawan. Pertahanannya adalah filter spam untuk memblokir email mencurigakan dan pemindaian lampiran sebelum sampai ke pengguna.
- **Firewall** — Risikonya adalah orang asing dari internet yang mencoba masuk ke jaringan. Pertahanannya adalah aturan firewall yang mengontrol traffic secara ketat dan pemblokiran IP address yang sudah dikenal berbahaya.
- **Internet (The Outside)** — Risikonya adalah semua ancaman eksternal yang datang dari luar. Pertahanannya adalah membatasi inbound traffic yang masuk dan memonitor secara aktif untuk mendeteksi aktivitas mencurigakan sedini mungkin.

---

## 4 — Where to Go From Here

### Terminologi Kunci yang Wajib Dikuasai

- **Blue Team** — Kelompok defender keamanan siber yang bertugas melindungi sistem dan merespons ancaman yang masuk.
- **Client Infrastructure** — Keseluruhan jaringan, server, perangkat, dan aplikasi milik sebuah organisasi yang membutuhkan perlindungan dari ancaman.
- **Visibility** — Kemampuan untuk melihat dan memantau aktivitas di seluruh sistem sehingga potensi masalah bisa terdeteksi sejak dini.
- **Threat** — Bahaya potensial seperti hacker atau malware yang bisa merusak sistem atau mencuri data.
- **Prevention** — Menghentikan ancaman sebelum bisa menyebabkan kerusakan dengan cara memblokir, membatasi, atau mengurangi peluang serangan terjadi.
- **Detection** — Proses mengidentifikasi ancaman atau aktivitas mencurigakan yang sedang berlangsung di jaringan dan sistem.
- **Mitigation** — Tindakan yang diambil untuk mengurangi atau menghentikan dampak dari sebuah ancaman setelah berhasil teridentifikasi.
- **Risk** — Kemungkinan dan potensi dampak dari sebuah ancaman yang berhasil merugikan organisasi secara nyata.

### Jalur Karir Defensive Security

Defensive security menawarkan berbagai jalur karir yang menarik, khususnya bagi yang tertarik dengan blue teaming:

- **Security Operations Center (SOC)** — Bertugas memantau jaringan dan sistem secara terus-menerus untuk mendeteksi dan menyelidiki aktivitas mencurigakan atau peringatan keamanan yang muncul. Ini adalah garis terdepan dalam defensive security.
- **Threat Intelligence** — Bertugas meneliti ancaman terkini, mempelajari taktik penyerang, dan menganalisis tren serangan untuk membantu organisasi mempersiapkan pertahanan mereka secara proaktif sebelum serangan terjadi.
- **Digital Forensics & Incident Response (DFIR)** — Bertugas menyelidiki insiden keamanan secara mendalam untuk memahami bagaimana serangan terjadi, seberapa jauh dampaknya, dan bagaimana memulihkan sistem yang terdampak agar kembali normal.

### Jalur Pembelajaran Selanjutnya

Course ini menandai akhir dari jalur **Pre Security** di TryHackMe. Dari sini, ada tiga jalur lanjutan yang bisa dipilih sesuai minat:

- **Cyber Security 101** — untuk memperluas fondasi keamanan siber secara umum
- **SOC Level 1** — untuk mendalami blue team dan monitoring
- **Jr Penetration Tester** — untuk mendalami sisi offensive dan red teaming

---

## Ringkasan Alur Berpikir Keseluruhan Course

```
DEFENSIVE SECURITY
        ↓
Pahami CIA Triad sebagai fondasi
(Confidentiality, Integrity, Availability)
        ↓
Kenali lingkungan yang dilindungi
(Devices, Web Server, Mail Server, Firewall, Internet)
        ↓
Terapkan 5 Konsep Fondasi
Prevention → Detection → Mitigation → Analysis → Response
        ↓
Bangun Defender Mindset
Anticipation → Awareness → Prioritization → Adaptation
        ↓
Terapkan Pertahanan Berlapis per Komponen
(Tidak ada 1 alat yang cukup — gunakan kombinasi)
        ↓
Pilih Jalur Karir
SOC | Threat Intelligence | DFIR
```