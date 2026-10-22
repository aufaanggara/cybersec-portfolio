# Laporan Insiden — Lab Install Software di Linux (APT, Nload, tcpdump)

**Tanggal:** Oktober 2026
**Platform:** Google Cybersecurity Certificate (lab hands-on)
**Tingkat Kesulitan:** Mudah (pengantar, sekitar 1 jam)
**Kategori:** Dasar Linux / setup tools keamanan
**Tools yang Digunakan:** APT, sudo, Nload, tcpdump

---

## Ringkasan Eksekutif

Ini lab latihan, bukan insiden sungguhan. Tujuannya melatih hal yang pasti dipakai seorang security analyst: memasang tool keamanan jaringan di mesin Linux dan memastikan tool itu benar-benar terpasang. Aku pakai package manager APT di virtual machine berbasis Debian untuk install, uninstall, dan install ulang Nload dan tcpdump, dan tiap langkah selalu kuverifikasi, bukan cuma percaya perintahnya "kelihatan jalan". Kelima task selesai dan terkonfirmasi lewat tombol *Check my progress*.

---

## Indikator Kompromi (IOC)

Tidak ada. Lab ini tidak punya attacker, malware, atau log serangan, jadi tidak ada IOC yang dicatat.

---

## Alur Investigasi

Karena tidak ada log dengan timestamp nyata, aku tulis urutan tahapannya saja:

1. Mulai lab dan masuk ke shell `analyst`
2. Cek APT sudah terpasang
3. Install Nload, verifikasi, uninstall, verifikasi lagi
4. Install tcpdump
5. List semua aplikasi terpasang dan cari tcpdump
6. Install ulang Nload dan pastikan keduanya terpasang
7. Akhiri lab

---

## Proses Investigasi

### Fase 1: Mulai Lab

- **Masalah:** Perlu lingkungan Linux untuk mengerjakan task, dan lab belum jalan.
- **Investigasi:** Klik **Start Lab**. Lab berjalan di virtual machine, jadi aman buat latihan tool keamanan karena kalau ada yang rusak, sistem bisa dikembalikan.
- **Temuan:** Muncul Bash shell dengan user `analyst` yang sudah login. Prompt berakhiran `$`, artinya aku user biasa, bukan root.
- **Kesimpulan:** Lingkungan siap. Karena bukan root, nanti install dan uninstall butuh `sudo`.

```bash
analyst@<container-id>:~$
```

<img src="docs/01-start-lab.png" width="750">

---

### Fase 2: Cek APT Terpasang (Task 1)

- **Masalah:** Sebelum install apa pun, aku harus tahu package manager-nya ada.
- **Investigasi:** Jalankan `apt` tanpa argumen. Kalau terpasang, dia menampilkan versi dan info penggunaan.
- **Temuan:** APT merespons dengan versi dan usage (di contoh lab: `apt 1.8.2.3 (amd64)`). Wajar, karena sistemnya berbasis Debian dan APT memang package manager bawaannya.
- **Kesimpulan:** APT tersedia. Di distro lain kemungkinan package manager-nya beda, misalnya YUM.

```bash
apt   # tanpa argumen: tampil versi + usage kalau APT ada
```

<img src="docs/02-confirm-apt-installed.png" width="600">

<img src="docs/03-check-progress-task1.png" width="600">

---

### Fase 3: Install dan Uninstall Nload (Task 2)

- **Masalah:** Perlu Nload (tool buat monitor traffic dan bandwidth jaringan), dan harus bisa dibuktikan terpasang lalu terhapus.
- **Investigasi:**
  - Install pakai `sudo apt install nload`, lalu tekan ENTER untuk jawaban default Yes di prompt dependensi.
  - Verifikasi dengan `nload -h`.
  - Uninstall pakai `sudo apt remove nload`, lalu verifikasi lagi dengan `nload -h`.
- **Temuan:**
  - Setelah install, `nload -h` menampilkan versi dan info lisensi (di contoh lab: `nload version 0.7.4`).
  - Setelah uninstall, `nload -h` mengeluarkan `-bash: /usr/bin/nload: No such file or directory`.
- **Kesimpulan:** Install dan uninstall berhasil. Error "No such file or directory" di langkah terakhir justru hasil yang diharapkan, karena artinya program sudah benar-benar hilang.

```bash
sudo apt install nload   # sudo = hak akses tinggi; install = pasang paket; nload = nama paket
nload -h                 # -h = tampilkan help, sekaligus bukti Nload ada
sudo apt remove nload    # hapus paket
nload -h                 # sekarang harusnya error "No such file or directory"
```

**Install Nload**

<img src="docs/04-install-nload.png" width="600">

**Konfirmasi install**

<img src="docs/05-confirm-install-nload.png" width="600">

**Verifikasi Nload terpasang**

<img src="docs/06-verify-nload-installed.png" width="600">

**Uninstall Nload**

<img src="docs/07-uninstall-nload.png" width="600">

**Verifikasi Nload sudah terhapus**

<img src="docs/08-verify-nload-uninstalled.png" width="600">

**Check progress Task 2**

<img src="docs/09-check-progress-task2.png" width="600">

---

### Fase 4: Install tcpdump (Task 3)

- **Masalah:** Perlu tcpdump, tool untuk menangkap traffic jaringan dari command line.
- **Investigasi:** Pakai pola yang sama seperti Nload.
- **Temuan:** Instalasi selesai tanpa kendala dan Task 3 terkonfirmasi.
- **Kesimpulan:** tcpdump terpasang.

```bash
sudo apt install tcpdump
```

<img src="docs/10-install-tcpdump.png" width="600">

<img src="docs/11-check-progress-task3.png" width="600">

---

### Fase 5: List Aplikasi Terpasang (Task 4)

- **Masalah:** Harus bisa memvalidasi aplikasi apa saja yang benar-benar terpasang, dan kadang versinya juga.
- **Investigasi:** Jalankan `apt list --installed`, lalu cari tcpdump di dalam daftar.
- **Temuan:**
  - Daftarnya panjang karena Linux punya banyak software bawaan.
  - tcpdump muncul dengan tanda `[installed]`. Versinya bisa beda dari contoh lab (`4.9.3-1~deb10u2`) dan itu normal.
  - Nload tidak ada di daftar, sesuai ekspektasi karena sudah di-uninstall di Fase 3.
- **Kesimpulan:** Kondisi sistem cocok dengan yang kuharapkan: tcpdump ada, Nload belum.

```bash
apt list --installed   # list = tampilkan paket; --installed = hanya yang sudah terpasang
```

> Catatan buat diri sendiri: daftarnya panjang, jadi lain kali lebih cepat pakai `apt list --installed | grep tcpdump` daripada scroll.

<img src="docs/12-list-installed-apps.png" width="600">

<img src="docs/13-check-progress-task4.png" width="600">

---

### Fase 6: Install Ulang Nload (Task 5)

- **Masalah:** Nload harus kembali terpasang, dan aku perlu memastikan dua tool (Nload dan tcpdump) sama-sama ada.
- **Investigasi:** Jalankan `sudo apt install nload` lagi, lalu `apt list --installed` dan cari Nload.
- **Temuan:** Nload muncul lagi di daftar dengan tanda `[installed]` (di contoh lab: `nload/oldstable,now 0.7.4-2+b1 amd64 [installed]`).
- **Kesimpulan:** Install ulang berhasil. Nload dan tcpdump sekarang sama-sama terpasang.

```bash
sudo apt install nload
apt list --installed   # cari baris nload
```

<img src="docs/14-reinstall-nload.png" width="600">

<img src="docs/15-list-installed-after-reinstall.png" width="600">

<img src="docs/16-check-progress-task5.png" width="600">

---

### Fase 7: Mengakhiri Lab

- **Masalah:** Lab harus ditutup dengan benar supaya progres tercatat.
- **Investigasi:** Klik **End Lab**, lalu **Submit** di pop-up konfirmasi. Setelah itu tutup tab lab dan refresh halaman course.
- **Temuan:** Mengakhiri lab menghapus akses ke Bash shell, jadi semua bukti harus sudah di-screenshot sebelum langkah ini.
- **Kesimpulan:** Semua task selesai dan lab ditandai complete.

<img src="docs/17-end-lab-complete.png" width="750">

---

## Pelajaran yang Didapat

- APT sudah cukup untuk siklus lengkap: install, uninstall, dan list.
- `sudo` wajib untuk `apt install` dan `apt remove` karena perintah itu mengubah sistem.
- Install tanpa error belum tentu berarti beres. Verifikasi (jalankan tool atau list paket) yang bikin hasilnya bisa dipercaya.
- Error "No such file or directory" bisa jadi hasil yang benar, seperti saat memastikan Nload sudah terhapus.
- Dependensi dipasang otomatis oleh APT, itu yang bikin jauh lebih praktis daripada install manual.
- Di SOC nyata, skill ini kepakai waktu butuh tool seperti tcpdump di sebuah host dengan cepat dan harus yakin tool-nya ada plus versinya apa.
- Kalau mengulang, aku langsung pakai `apt list --installed | grep <nama>` dari awal.

---

## Playbook: Install dan Validasi Tool Keamanan di Host Debian

**Pemicu:** Analyst butuh sebuah tool (misal tcpdump) di host Linux berbasis Debian.

**Langkah Triase:**
1. Jalankan `apt` dan pastikan APT tersedia.
2. Install dengan `sudo apt install <paket>`, baca daftar dependensi sebelum menyetujui.
3. Verifikasi tool jalan, misalnya `<tool> -h` atau `<tool> --version`.
4. Cek `apt list --installed | grep <paket>` dan catat versinya.
5. Simpan screenshot atau output sebagai bukti.

**Kriteria Eskalasi:**
- Paket tidak ditemukan atau gagal terinstall (bisa masalah repository atau jaringan).
- Muncul paket atau versi yang tidak pernah kamu install.

**Pengecekan Setelah Uninstall:** Setelah `sudo apt remove <paket>`, jalankan tool-nya lagi dan harapkan `No such file or directory`.

**Indikator False Positive:** Error "not found" tepat setelah uninstall itu normal dan bukan masalah.