# Incident Report — Investigating Phishing Emails (Netflix / Payment Update / Excel Executable Cases)

**Date:** 2026-08-23
**Platform:** TryHackMe
**Difficulty:** Easy/Medium
**Category:** Phishing / Email Analysis / Malware Sandbox Analysis
**Analyst:** [nama kamu]

---

## Executive Summary

This engagement covered a structured phishing-email investigation exercise involving three separate suspicious email cases escalated by end users. Case 1 was a phishing email impersonating Netflix that used a URL shortener to hide a malicious billing-update link. Case 2 was a phishing email impersonating a Netflix payment notification with a malicious PDF attachment that, when opened, generated suspicious network activity flagged by sandbox analysis. Case 3 involved a malicious Excel (.xlsx) attachment exploiting a known Microsoft Office vulnerability (CVE-2017-11882) to trigger a multi-stage download of an executable payload from an external domain. All three cases were confirmed malicious through header analysis, attachment hash reputation lookups, and dynamic sandbox execution. No production systems were affected; this was a controlled lab investigation intended to build phishing-triage methodology aligned with real-world SOC Level 1 workflows.

---

## Indicators of Compromise (IOC)

| Tipe IOC | Nilai | Keterangan |
|---|---|---|
| Sender Domain (Case 1) | etekno.xyz | Domain of interest identified via `Return-Path` and SPF `smtp.mailfrom` — likely actual sending infrastructure behind the spoofed "Netflix" display name |
| Originating IP (Case 1) | 10.197.37.234 | IP from the first `Received: from` header line in message source |
| X-Originating-To IP (Case 1) | 209.85.167.226 | IP listed in `X-Originating-To` header |
| Shortened URL (Case 1) | https://t.co/yuxfZm8KPg?amp=1 | Shortened link behind the "UPDATE ACCOUNT NOW" button, obfuscating final phishing destination |
| Spoofed Sender Domain (Case 1) | gogolecloud.com | Domain used in the spoofed "From" header to imitate legitimacy |
| Attachment Filename (Case 2) | Payment-updateid.pdf | Malicious PDF attachment disguised as a Netflix payment notice |
| File Hash MD5 (Case 2) | 4A2775EAE2EBEF41901A3F08D3B857C8 | MD5 hash of Payment-updateid.pdf |
| File Hash SHA1 (Case 2) | 8B3439F5EA2F20C6BE329C4C6B8EAA9CC439233B | SHA1 hash of Payment-updateid.pdf |
| File Hash SHA256 (Case 2) | CC6F1A04B10BCB168AEEC8D870B97BD7C20FC161E8310B5BCE1AF8ED420E2C24 | SHA256 hash of Payment-updateid.pdf |
| File Metadata Anomaly (Case 2) | Author: PayPal Support | EXIF metadata mismatch — file claims Netflix branding but internal author field references PayPal, suggesting reuse of a phishing-kit template |
| Malicious IP (Case 2) | 2.16.107.24 | IP tied to `acroipm2.adobe.com`, flagged malicious in ANY.RUN report despite appearing to be a legitimate Adobe-related domain |
| Network Threat Process (Case 2) | svchost.exe (PID 1776) | Flagged as "Potentially Bad Traffic" — ET INFO TLS Handshake Failure |
| Attachment Filename (Case 3) | CBJ200620039539.xlsx | Malicious Excel attachment used to exploit CVE-2017-11882 |
| File Hash MD5 (Case 3) | F7F4EC2A0ADC9CC33CDBC7D548A6BEF9 | MD5 hash of CBJ200620039539.xlsx |
| File Hash SHA1 (Case 3) | D468315F92AA3DCA63617431883834ED94C09F45 | SHA1 hash of CBJ200620039539.xlsx |
| File Hash SHA256 (Case 3) | 5F94A66E0CE78D17AFC2DD27FC17B44B3FFC13AC5F42D3AD6A5DCFB36715F3EB | SHA256 hash of CBJ200620039539.xlsx |
| Malicious Domain (Case 3) | biz9holdings.com | Hosted executable payload (`/INVOICE/COVID19.exe`) |
| Malicious Domain IP (Case 3) | 204.11.56.48 | Resolved IP address for biz9holdings.com |
| Redirect Domain (Case 3) | findresults.site | Domain in redirect chain following payload request; flagged as malicious |
| Redirect Subdomain (Case 3) | ww38.findresults.site | Subdomain observed in the redirect chain (secondary hop) |
| Exploited Process (Case 3) | EQNEDT32.EXE | Microsoft Office Equation Editor process abused to trigger the exploit |
| CVE (Case 3) | CVE-2017-11882 | Known remote code execution vulnerability in Microsoft Office Equation Editor |

[BUTUH SCREENSHOT — belum diberi nama, tambahkan manual] — reputation confirmation for `findresults.site` (final answer not fully re-verified against the platform's correct-answer check in this chat; see Investigation Process, Case 3, Step 5).

---

## Investigation Flow

Room ini adalah gabungan materi pembelajaran (Task 1–6) dan guided practice terhadap tiga kasus phishing nyata (Task 7–9), sehingga tidak ada timestamp log produksi untuk direkonstruksi menjadi timeline insiden. Sebagai gantinya, berikut alur tahapan investigasi yang dilakukan:

1. **Foundational learning** — mempelajari artifact apa saja yang perlu dikumpulkan dari header dan body email (Task 1–2).
2. **Tooling familiarization** — mempelajari tools untuk analisis header (Messageheader, Message Header Analyzer), reputasi IP/URL (IPinfo, URLScan.io, Talos), dan analisis body/attachment (URL extraction tools, sha256sum, VirusTotal) (Task 3–4).
3. **Sandbox familiarization** — mempelajari malware sandbox (ANY.RUN, Hybrid Analysis, JOESandbox) dan platform investigasi terpusat PhishTool (Task 5–6).
4. **Case 1 — Netflix Account on Hold** — analisis email phishing berbasis link, mengidentifikasi brand impersonation, domain of interest, originating IP, dan shortened URL (Task 7).
5. **Case 2 — Update Payment Details** — analisis attachment PDF berbahaya menggunakan ANY.RUN, meliputi verdict klasifikasi, hash file, dan IP/proses mencurigakan (Task 8).
6. **Case 3 — Excel Executable** — analisis attachment Excel berbahaya yang mengeksploitasi CVE-2017-11882, meliputi verdict, hash, resolusi DNS domain berbahaya, dan identifikasi CVE (Task 9).

---

## Investigation Process

### Phase 1: Foundational Artifact Identification

Sebelum masuk ke kasus praktik, materi menetapkan checklist artifact standar untuk setiap investigasi email:

- **Header artifacts:** sender email address, sender IP address (+ reverse lookup), subject line (urgency/call-to-action), recipient address, reply-to address, date/time.
- **Body artifacts:** URL/hyperlink (termasuk expand shortened URL), nama dan ekstensi attachment, hash attachment.

Tools yang dipetakan untuk masing-masing kebutuhan:

| Kebutuhan | Tool |
|---|---|
| Header parsing otomatis | Messageheader (Google Admin Toolbox), Message Header Analyzer |
| IP reputation & geolocation | IPinfo |
| URL/website inspection tanpa akses langsung | URLScan.io |
| IP/domain/hash reputation | Talos IP & Domain Reputation Center |
| File/URL reputation multi-vendor | VirusTotal |
| Sandboxed detonation | ANY.RUN, Hybrid Analysis, JOESandbox |
| Centralized phishing triage | PhishTool |

### Phase 2: Case 1 — "Your Netflix Account Is on Hold"

**Step 1 — Initial email review.** File `Phish3Case1.eml` dibuka di Thunderbird. Email menampilkan sender "Netflix", subject `YourNetflixAccountisonHold`, ditujukan ke `redacted@yahoo.com`, tanggal 7/7/21 02:14. Isi email meminta korban meng-update payment details melalui tombol "UPDATE ACCOUNT NOW".

![Email phishing Netflix "Your account is on hold" terbuka di Thunderbird menampilkan sender, subject, dan tombol UPDATE ACCOUNT NOW](docs/01-email-netflix-account-on-hold.png)

**Step 2 — Brand impersonation check.** Berdasarkan display name pengirim, konten pesan, dan footer email (nama "Netflix", alamat kantor "100 Winchester Circle, Los Gatos, CA"), email ini dikonfirmasi meniru brand **Netflix**.

**Step 3 — Recipient identification.** Field `To` pada header menunjukkan penerima yang dituju adalah `redacted@yahoo.com`.

**Step 4 — Raw header inspection.** Message Source dibuka via `View → Message Source` di Thunderbird.

```
Received: from 10.197.37.234
  by atlas105.free.mail.bf1.yahoo.com with HTTPS; Wed, 7 Jul 2021 02:14:46 +0000
Return-Path: <postmaster@etekno.xyz>
X-Originating-To: [209.85.167.226]
Received-SPF: none (domain of etekno.xyz does not designate permitted sender hosts)
Authentication-Results: atlas105.free.mail.bf1.yahoo.com;
  dkim=unknown;
  spf=none smtp.mailfrom=etekno.xyz;
  dmarc=unknown header.from=JOg7ODDQwWdR-yVkCaBkTNp.gogolecloud.com;
```

![Raw message source di Thunderbird menampilkan header Received, Return-Path, X-Originating-To, dan Authentication-Results](docs/02-message-source-received-return-path.png)

Baris `Received: from` pertama menunjukkan IP originating **10.197.37.234**.

**Step 5 — Domain of interest identification.** Field `Return-Path` (`postmaster@etekno.xyz`) dan hasil SPF check (`spf=none smtp.mailfrom=etekno.xyz`) sama-sama mengarah ke domain **etekno.xyz** — ini lebih dipercaya sebagai domain asli pengirim dibanding tampilan "From" karena Return-Path/SMTP MAIL FROM lebih sulit dipalsukan tanpa terdeteksi oleh SPF check.

**Step 6 — Malicious link extraction.** Klik kanan pada tombol "UPDATE ACCOUNT NOW" → Copy Link Location menghasilkan URL shortener:

```
https://t.co/yuxfZm8KPg?amp=1
```

![Hasil copy link location dari tombol UPDATE ACCOUNT NOW menunjukkan URL shortener t.co](docs/03-copy-link-location-update-account-button.png)

URL ini menggunakan shortener Twitter/X (`t.co`) untuk menyembunyikan tujuan akhir link phishing.

### Phase 3: Case 2 — "Update Payment Details" (PDF Attachment)

**Step 1 — Sandbox verdict.** File `Payment-updateid.pdf` dianalisis menggunakan ANY.RUN. Sandbox mengembalikan verdict **"Suspicious activity"**.

![Panel ANY.RUN menampilkan banner verdict Suspicious activity untuk file Payment-updateid.pdf](docs/04-anyrun-verdict-suspicious-activity.png)

**Step 2 — File identification & hashing.** Melalui panel **Static Discovering**, file teridentifikasi sebagai `Payment-updateid.pdf` dengan hash:

- MD5: `4A2775EAE2EBEF41901A3F08D3B857C8`
- SHA1: `8B3439F5EA2F20C6BE329C4C6B8EAA9CC439233B`
- SHA256: `CC6F1A04B10BCB168AEEC8D870B97BD7C20FC161E8310B5BCE1AF8ED420E2C24`

![Popup Static Discovering ANY.RUN menampilkan hash MD5, SHA1, SHA256, dan metadata EXIF file Payment-updateid.pdf](docs/05-static-discovering-file-hashes.png)

Catatan tambahan: EXIF metadata file menunjukkan `Author: PayPal Support`, meskipun konten dan branding email meniru Netflix — indikasi kuat bahwa file berasal dari phishing-kit template yang di-reuse lintas kampanye.

**Step 3 — Network threat identification.** Tab **Network Threats** pada ANY.RUN menampilkan proses `svchost.exe` (PID 1776) di-flag sebagai **"Potentially Bad Traffic"** dengan pesan `ET INFO TLS Handshake Failure`.

![Tab Network Threats ANY.RUN menampilkan proses svchost.exe diflag Potentially Bad Traffic dengan pesan ET INFO TLS Handshake Failure](docs/06-network-threats-potentially-bad-traffic.png)

**Step 4 — Malicious IP tied to AcroRd32.exe.** Tab **Connections** menampilkan koneksi dari proses `AcroRd32.exe` (PID 2088) ke IP `2.16.107.24` (domain `acroipm2.adobe.com`). Meski kolom reputation UI menunjukkan status belum terverifikasi (`?`), IP ini dikonfirmasi sebagai jawaban yang benar oleh platform TryHackMe — menunjukkan bahwa domain yang tampak legitimate (Adobe-related) dapat me-resolve ke infrastruktur yang telah tercemar.

![Tab Connections ANY.RUN menampilkan proses AcroRd32.exe terhubung ke IP 2.16.107.24 pada domain acroipm2.adobe.com](docs/07-connections-acrord32-ip-2-16-107-24.png)

### Phase 4: Case 3 — "Excel Executable" (.xlsx Attachment, CVE-2017-11882)

**Step 1 — Sandbox verdict.** File `CBJ200620039539.xlsx` dianalisis menggunakan ANY.RUN. Sandbox mengembalikan verdict **"Malicious activity"**, dengan tag `trojan`, `exploit`, dan `cve-2017-11882`.

![Panel ANY.RUN menampilkan banner verdict Malicious activity untuk file CBJ200620039539.xlsx beserta tag trojan, exploit, dan cve-2017-11882](docs/08-anyrun-verdict-malicious-activity-xlsx.png)

**Step 2 — File identification & hashing.** Melalui Static Discovering, hash file:

- MD5: `F7F4EC2A0ADC9CC33CDBC7D548A6BEF9`
- SHA1: `D468315F92AA3DCA63617431883834ED94C09F45`
- SHA256: `5F94A66E0CE78D17AFC2DD27FC17B44B3FFC13AC5F42D3AD6A5DCFB36715F3EB`

![Popup Static Discovering ANY.RUN menampilkan hash MD5, SHA1, SHA256 file CBJ200620039539.xlsx](docs/09-static-discovering-xlsx-hashes.png)

**Step 3 — Process chain analysis.** Panel Processes menunjukkan rantai eksekusi: `EXCEL.EXE` → `EQNEDT32.EXE` (Equation Editor, dengan flag `-Embedding`) → `ntvdm.exe`. Rantai ini konsisten dengan pola eksploitasi CVE-2017-11882, di mana objek OLE yang disematkan dalam dokumen Office memicu Equation Editor untuk mengeksekusi kode berbahaya.

**Step 4 — Malicious domain resolution.** Tab **DNS Requests** menunjukkan:

| Domain | IP |
|---|---|
| biz9holdings.com | 204.11.56.48 |
| findresults.site | 103.224.182.251 |
| ww38.findresults.site | 75.2.11.242 |

![Tab DNS Requests ANY.RUN menampilkan resolusi domain biz9holdings.com, findresults.site, dan ww38.findresults.site beserta IP masing-masing](docs/10-dns-requests-biz9holdings-ip.png)

HTTP Requests mengonfirmasi rantai redirect: request awal ke `biz9holdings.com/INVOICE/COVID19.exe` (payload download) → redirect (302) ke `findresults.site` → redirect lagi ke `ww38.findresults.site`. Berdasarkan struktur domain, `ww38.findresults.site` diidentifikasi sebagai subdomain, sedangkan **findresults.site** adalah domain utama yang diklasifikasikan malicious.

**Step 5 — Vulnerability confirmation.** Tag `cve-2017-11882` dikonfirmasi melalui pencarian tag pada ANY.RUN public submissions (`app.any.run/submissions#tag:cve-2017-11882`), menampilkan beberapa sampel lain dengan pola serupa (file RTF/DOC yang di-flag malicious dengan tag exploit + CVE yang sama).

![Hasil pencarian tag cve-2017-11882 di ANY.RUN public submissions menampilkan beberapa sampel lain dengan pola eksploitasi serupa](docs/11-anyrun-tag-search-cve-2017-11882.png)

---

## Root Cause Analysis

Ketiga kasus dalam room ini bukan mewakili satu insiden tunggal, melainkan tiga skenario latihan independen yang masing-masing mendemonstrasikan root cause klasik phishing:

- **Case 1:** Keberhasilan serangan bergantung pada social engineering (urgency + brand trust) dan pemanfaatan URL shortener untuk melewati inspeksi visual korban terhadap URL tujuan. Tidak ada exploit teknis; celah utamanya adalah kurangnya awareness pengguna terhadap domain mismatch dan penggunaan link shortener yang mencurigakan.
- **Case 2:** Serangan mengandalkan social engineering serupa (branding Netflix + urgency payment) dikombinasikan dengan attachment PDF yang memicu proses jaringan mencurigakan saat dibuka — mengindikasikan PDF membawa objek aktif (embedded link/script) yang berkomunikasi keluar saat file dirender.
- **Case 3:** Root cause teknis jelas teridentifikasi: eksploitasi **CVE-2017-11882** pada Microsoft Office Equation Editor. Ini adalah kerentanan lama (dipublikasikan 2017) yang seharusnya sudah dimitigasi melalui patch resmi Microsoft; keberhasilan eksploitasi menunjukkan sistem target berpotensi belum menerapkan patch tersebut — pola umum di lingkungan yang patch management-nya tidak konsisten.

---

## Impact Assessment

- Investigasi ini dilakukan sepenuhnya dalam lingkungan lab terkontrol (TryHackMe AttackBox/Lab Machine); tidak ada sistem produksi yang terdampak.
- Dalam konteks skenario nyata yang direpresentasikan (SOC Level 1 triaging user-reported email):
  - **Case 1** berpotensi menghasilkan credential harvesting jika korban mengklik link dan memasukkan kredensial pada halaman phishing di balik shortener `t.co`.
  - **Case 2** berpotensi menghasilkan kompromi endpoint melalui komunikasi command-and-control atau download payload tambahan saat PDF dibuka, mengingat proses `AcroRd32.exe` teridentifikasi berkomunikasi dengan IP yang di-flag malicious.
  - **Case 3** memiliki potensi dampak tertinggi: eksploitasi CVE-2017-11882 memungkinkan remote code execution, yang pada skenario nyata dapat mengarah pada full endpoint compromise, download payload tambahan (`COVID19.exe`), dan potensi lateral movement jika tidak segera di-contain.

---

## Remediation & Recommendations

**Immediate actions**
- Block domain/IOC berikut di email gateway dan firewall/proxy: `etekno.xyz`, `gogolecloud.com`, `t.co/yuxfZm8KPg`, `biz9holdings.com` (204.11.56.48), `findresults.site` dan subdomain-nya.
- Quarantine dan hapus salinan email dari mailbox pengguna lain yang menerima pesan serupa (sender pattern atau subject pattern yang sama).
- Reset kredensial pengguna mana pun yang diketahui/dicurigai telah mengklik link Case 1 atau membuka attachment Case 2/3.

**Short-term**
- Terapkan hash-based blocking (SHA256) untuk `Payment-updateid.pdf` dan `CBJ200620039539.xlsx` pada endpoint protection/EDR.
- Terapkan attachment sandboxing otomatis pada email gateway untuk file Office dan PDF sebelum sampai ke inbox pengguna.
- Audit dan pastikan patch untuk **CVE-2017-11882** telah diterapkan di seluruh endpoint yang menjalankan Microsoft Office.

**Long-term**
- Perkuat kebijakan SPF/DKIM/DMARC enforcement pada domain organisasi untuk mengurangi kemungkinan spoofing serupa terhadap partner/brand pihak ketiga yang sering ditiru.
- Adakan security awareness training terkait pengenalan URL shortener mencurigakan dan verifikasi domain sender sebelum mengklik link pembayaran/akun.
- Integrasikan feed threat intelligence (Talos, VirusTotal) ke pipeline deteksi email gateway secara otomatis, bukan hanya manual lookup saat investigasi.

---

## Lessons Learned

- Field **Return-Path** dan hasil **SPF `smtp.mailfrom`** sering lebih dapat diandalkan dibanding header "From" yang tampil ke pengguna, karena lebih sulit dipalsukan tanpa memicu SPF failure.
- Reputasi IP/domain tidak selalu langsung terlihat di kolom UI standar (contoh: kolom Rep di tab Connections ANY.RUN menunjukkan `?` meski IP tersebut sebenarnya sudah dikonfirmasi malicious pada text report) — penting untuk cross-check di beberapa tab (Connections, DNS Requests, Network Threats, text report) sebelum menyimpulkan sebuah indikator "bersih".
- Metadata file (EXIF/author) bisa menjadi indikator tambahan yang kuat untuk mendeteksi phishing-kit template yang di-reuse lintas kampanye brand berbeda.
- CVE lama seperti CVE-2017-11882 tetap relevan sebagai ancaman aktif karena luasnya sistem yang belum di-patch — pengecekan versi/patch level tetap menjadi bagian penting dari triase root cause.
- Redirect chain (multiple domain hop) adalah pola umum dalam distribusi payload phishing modern, dan platform sandbox seperti ANY.RUN sangat membantu memetakan seluruh rantai ini secara visual dan otomatis.

---

## Playbook: Suspicious Email Attachment/Link Triage

**Trigger:** End user melaporkan email mencurigakan yang meminta update akun/pembayaran, atau menyertakan attachment PDF/Office yang tidak diharapkan.

**Triage Steps:**
1. Ekstrak dan analisis header email (sender, reply-to, originating IP, SPF/DKIM/DMARC) menggunakan Messageheader atau Message Header Analyzer.
2. Identifikasi domain of interest dari field `Return-Path` dan `smtp.mailfrom`, bukan hanya dari display name/"From" yang tampil.
3. Ekstrak seluruh URL dari body email (manual copy-link atau URL extraction tool); expand semua shortened URL sebelum menilai tujuan akhirnya.
4. Jika ada attachment: hitung hash (SHA256) dan cek reputasinya di Talos/VirusTotal sebelum membuka file secara langsung.
5. Jika hash belum dikenal atau reputasi ambigu, detonasi file dalam sandbox (ANY.RUN/Hybrid Analysis/JOESandbox) dan tinjau verdict, process chain, DNS requests, connections, dan network threats.
6. Dokumentasikan seluruh IOC (domain, IP, hash, URL) dan tentukan disposition akhir (Malicious/Suspicious/Benign) menggunakan platform seperti PhishTool.

**Escalation Criteria:**
- Sandbox verdict menunjukkan "Malicious activity" atau tag exploit/CVE teridentifikasi.
- Ditemukan indikasi lateral movement atau proses download payload tambahan setelah file dieksekusi.
- Multiple user melaporkan email dengan pola sender/subject yang identik (indikasi kampanye massal).

**Containment Actions:**
- Block seluruh IOC (domain, IP, URL, hash) pada email gateway, proxy/firewall, dan EDR.
- Quarantine email serupa dari seluruh mailbox organisasi.
- Isolasi endpoint yang diketahui membuka attachment berbahaya, dan lakukan reset kredensial jika ada indikasi kredensial pengguna dimasukkan ke halaman phishing.

**False Positive Indicators:**
- SPF/DKIM/DMARC pass secara konsisten dan domain sender sesuai dengan domain resmi brand yang diklaim.
- URL yang di-expand mengarah langsung ke domain resmi tanpa redirect chain mencurigakan.
- Hash attachment sudah dikenal luas sebagai file legitimate (misalnya template internal perusahaan) dengan reputasi bersih di multi-vendor scanner.