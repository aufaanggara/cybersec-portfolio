# Information Security Fundamentals - Resume Materi
*07 Mar 2026*

## Defence in Depth
- **Definisi**: Penggunaan BANYAK lapisan keamanan yang bervariasi pada sistem & data organisasi.
- **Tujuan**: Memberikan redundansi pada perimeter keamanan.
- **Analogi**: Benteng berlapis — kalau 1 tembok bobol, masih ada tembok lain.
- **Prinsip**: Jangan andalkan 1 lapisan keamanan saja.

## CIA Triad
- **Apa itu**: Model keamanan informasi → standar industri sejak 1998.
- **Sifat**: Bukan 3 bagian terpisah → SIKLUS BERKELANJUTAN.
- **Penting**: Jika 1 elemen gagal → 2 elemen lain TIDAK BERGUNA (seperti segitiga api).
- **Cakupan**: Bukan hanya cybersecurity → juga filing, penyimpanan catatan, dll.

### C → CONFIDENTIALITY (Kerahasiaan)
Melindungi data dari akses tidak sah & penyalahgunaan.
- **Contoh**: HR admin saja yang akses data karyawan. Pemerintah pakai klasifikasi: top-secret, classified, unclassified.
- **Prinsip**: Makin sensitif datanya → makin ketat kontrol aksesnya.

### I → INTEGRITY (Integritas)
Informasi tetap AKURAT & KONSISTEN kecuali ada perubahan yang diotorisasi.
- **Ancaman**: Akses ceroboh, error sistem, akses tidak sah.
- **Cara Jaga**: Access control & autentikasi ketat, Hash verification, Digital signature.
- **Aturan**: Info harus tidak berubah selama penyimpanan, transmisi & penggunaan.

### A → AVAILABILITY (Ketersediaan)
Data harus tersedia & bisa diakses saat dibutuhkan user yang berwenang.
- **Benchmark**: 99.99% uptime (diatur dalam SLA).
- **Risiko Jika Gagal**: Kerusakan reputasi + kerugian finansial.
- **Cara Jaga**: Hardware andal & teruji, Teknologi & layanan redundan, Protokol keamanan yang kuat.

## Principles of Privileges
2 Faktor penentu level akses:
1. Peran/fungsi individu dalam organisasi.
2. Sensitivitas informasi yang disimpan di sistem.

- **PIM (Privileged Identity Management)**: Menerjemahkan PERAN USER di organisasi menjadi PERAN AKSES di sistem.
- **PAM (Privileged Access Management)**: Mengelola HAK-HAK yang dimiliki peran akses tersebut. Juga mencakup password management, auditing policy, pengurangan attack surface.
- **Least Privilege Principle (WAJIB HAPAL)**: User hanya boleh dapat privilege SEMINIMAL MUNGKIN. Hanya yang BENAR-BENAR PERLU untuk menjalankan tugas. Tujuannya adalah meminimalisir risiko jika akun tersebut disusupi.

## Security Models
*Info System = sistem/perangkat apapun yang menyimpan informasi*

### Bell-La Padula Model
- **Fokus**: CONFIDENTIALITY
- **Aturan**: "No write down, no read up" (Tidak boleh menulis ke level bawah, Tidak boleh membaca ke level atas).
- **Cara Kerja**: Akses data berdasarkan *strictly need-to-know basis*.
- **Cocok**: Militer & pemerintah (karena anggota sudah melalui vetting).
- **Vetting**: Proses screening latar belakang untuk nilai risiko seseorang.
- **Kelebihan**: Bisa direplikasi ke hierarki organisasi nyata. Sederhana, mudah dipahami, terbukti berhasil.
- **Kekurangan**: User tidak bisa akses objek tapi TAHU objek itu ada → tidak 100% rahasia. Bergantung pada kepercayaan besar dalam organisasi.

### Biba Model
- **Fokus**: INTEGRITY
- **Aturan**: "No write up, no read down" (Tidak boleh menulis ke level atas, Tidak boleh membaca ke level bawah).
- **Cara Kerja**: Subjek BOLEH tulis ke level mereka/bawahnya. Subjek HANYA BOLEH baca level di atasnya.
- **Cocok**: Software development (integritas > kerahasiaan). Contoh: Developer junior tidak bisa langsung ubah database produksi.
- **Kelebihan**: Sederhana diimplementasikan. Mengatasi keterbatasan Bell-La Padula (cover confidentiality & integrity).
- **Kekurangan**: Banyak level akses → mudah ada yang terlewat. Bisa sebabkan keterlambatan bisnis.

> **PERBANDINGAN CEPAT**
> - **Bell-La Padula** → Militer → Takut INFO BOCOR → No read up
> - **Biba** → Software → Takut DATA RUSAK → No read down

## Threat Modelling
- **Definisi**: Proses meninjau, meningkatkan & menguji protokol keamanan dalam infrastruktur IT & layanan organisasi.
- **Tujuan**: Identifikasi ancaman & kerentanan sistem/aplikasi.
- **Sifat**: Kompleks → butuh review & diskusi terus-menerus.
- **Siklus**: Preparation → Identification → Mitigations → Review → (ulang).

Effective threat model mencakup: Threat intelligence, Asset identification, Mitigation capabilities, Risk assessment.

### Framework STRIDE
*Dibuat oleh 2 peneliti Microsoft pada tahun 1999, masih relevan hingga kini.*

- **S → Spoofing**: Pihak jahat memalsukan identitasnya sebagai orang lain. Solusi: API keys, enkripsi, autentikasi.
- **T → Tampering**: Merusak/mengubah data tanpa izin. Solusi: anti-tampering measures, jaga integritas data.
- **R → Repudiation**: Menyangkal aktivitas yang dilakukan. Solusi: logging aktivitas sistem/aplikasi.
- **I → Information Disclosure**: Data tampil ke orang yang tidak berhak. Solusi: konfigurasi agar hanya tampilkan info ke pemiliknya saja.
- **D → Denial of Service**: Penyalahgunaan resource sistem sampai sistem down. Solusi: batasi & proteksi penggunaan resource aplikasi/layanan.
- **E → Elevation of Privilege (SKENARIO TERBURUK)**: User berhasil naikkan level akses → jadi administrator. Risiko: eksploitasi lanjut, pencurian data, ambil kendali penuh sistem.

## Incident Response
- **Insiden**: Pelanggaran/breach keamanan yang terjadi.
- **IR**: Tindakan untuk menyelesaikan & memulihkan ancaman tersebut.
- **CSIRT**: Computer Security Incident Response Team (Tim karyawan teknis yang menangani insiden).

### 6 Fase Incident Response
1. **Preparation**: Apakah kita punya resource & rencana untuk hadapi insiden?
2. **Identification**: Apakah ancaman & pelaku sudah teridentifikasi dengan benar?
3. **Containment**: Bisakah ancaman dikurung agar tidak menyebar ke sistem lain?
4. **Eradication**: Hapus ancaman yang aktif.
5. **Recovery**: Tinjau penuh sistem yang terdampak → kembalikan ke operasi normal.
6. **Lessons Learned**: Apa yang bisa dipelajari? Contoh: insiden karena phishing → latih karyawan deteksi phishing.

## Istilah Penting Wajib Hapal
| Istilah | Arti |
|---|---|
| **CIA Triad** | Confidentiality, Integrity, Availability |
| **Information Sys** | Sistem/perangkat apapun yang menyimpan informasi |
| **Vetting** | Proses screening latar belakang seseorang |
| **Least Privilege** | Beri akses seminimal yang diperlukan saja |
| **Attack Surface** | Semua titik/celah yang bisa diserang di suatu sistem |
| **Redundancy** | Lapisan cadangan jika satu sistem/akses gagal |
| **SLA** | Service Level Agreement (kontrak uptime/layanan) |
| **CSIRT** | Tim responder insiden keamanan komputer |
| **STRIDE** | Framework threat modelling (6 prinsip) |
| **Incident** | Pelanggaran keamanan yang terjadi |
| **IR** | Incident Response — tindakan mengatasi insiden |
| **PIM** | Privileged Identity Management |
| **PAM** | Privileged Access Management |
| **Need-to-know** | Hanya beri akses kepada yang benar-benar perlu tahu |