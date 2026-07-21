```
=== John The Ripper - Resume Materi ===
[15 Mei 2026]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 APA ITU JOHN THE RIPPER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definisi  : Tool pemecah hash yang cepat, serbaguna, support banyak tipe hash
Versi     : Core (standar) → Jumbo John (extended, paling populer, WAJIB PAKAI)
Default   : Kali Linux sudah include Jumbo John secara bawaan
Cek versi : john --version  atau  john (lihat baris pertama output)
Wordlist  : Butuh wordlist untuk dictionary attack → RockYou paling populer
RockYou   : /usr/share/wordlists/rockyou.txt (bawaan Kali & AttackBox)
            → Berasal dari data breach rockyou.com tahun 2009

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 KONSEP HASH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hash      : Fungsi satu arah — mudah hash, mustahil un-hash
Sifat     : Input berapapun panjangnya → output selalu fixed length
Contoh    : "polo" (4 huruf) → MD5 → b53759f3ce692de7aff1b5779d3964da (32 char)
            "polomints" (9 huruf) → MD5 → 584b6e4f4586e136bc280f27f9c64f3b (32 char)
Cara crack: Dictionary attack → hash semua kata di wordlist → bandingkan

IDENTIFIER FORMAT (dalam hash Linux):
  $1$  = md5crypt
  $5$  = sha256crypt
  $6$  = sha512crypt  ← paling umum di Linux modern
  $y$  = yescrypt    ← Kali Linux modern, sangat lambat di-crack

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 IDENTIFIKASI TIPE HASH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tool 1    : hashid [hash]          → modern, langsung di CLI, output bersih
Tool 2    : hash-identifier [hash] → tampilan ASCII art, lebih visual
Pakai     : hashid lebih praktis, hash-identifier lebih "hacker vibes"

PATOKAN FORMAT JOHN (hash polos/standar):
  MD5     → Raw-MD5
  SHA1    → Raw-SHA1
  SHA256  → Raw-SHA256
  SHA512  → Raw-SHA512
  MD4     → Raw-MD4
  NTLM    → NT          ← pengecualian! bukan Raw-NT
  Whirlpool → Whirlpool ← pengecualian! tanpa prefix Raw-
  sha512crypt → sha512crypt (untuk /etc/shadow $6$)

CEK FORMAT JOHN:
  john --list=formats | grep -iF "nama_hash"
  Flags: -i = ignore case, -F = fixed string (bukan regex)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SINTAKS DASAR JOHN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Struktur  : john [options] [file path]

Mode 1 - AUTOMATIC (tidak tahu format):
  john --wordlist=[path wordlist] [file hash]
  Contoh : john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

Mode 2 - FORMAT SPECIFIC (tahu format):
  john --format=[format] --wordlist=[path wordlist] [file hash]
  Contoh : john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

Lihat hasil yang sudah di-crack:
  john --show [file hash]

CATATAN: John simpan hasil di ~/.john/john.pot
         Hash yang sama tidak akan di-crack ulang → pakai --show untuk lihat

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ALUR CRACK HASH STANDAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Cek isi file hash  : cat [file]
2. Identifikasi tipe  : hashid [hash]
3. Cari format John   : john --list=formats | grep -iF "[tipe]"
4. Crack              : john --format=[format] --wordlist=rockyou.txt [file]
5. Lihat hasil        : john --show [file]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 WINDOWS AUTHENTICATION HASH (NTLM)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nama      : NTHash / NTLM (NT = New Technology)
Disimpan  : SAM database (Security Account Manager) di Windows
Cara dapat: Dump SAM dengan Mimikatz atau dari NTDS.dit (Active Directory)
Format    : NT (bukan NTLM, bukan Raw-NT)
Serangan  : Bisa crack ATAU "pass the hash" (tidak perlu crack)

Perintah  : john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt [file]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 LINUX /etc/shadow HASH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
File      : /etc/shadow  → hash password Linux, hanya root yang bisa akses
            /etc/passwd  → info user, bisa dibaca semua user

Masalah   : John butuh kombinasi keduanya → pakai tool UNSHADOW

UNSHADOW:
  Sintaks : unshadow [path passwd] [path shadow] > [output file]
  Contoh  : unshadow local_passwd local_shadow > unshadowed.txt

CRACK:
  john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt

CARA COPY FILE:
  cp /etc/passwd ~/local_passwd
  sudo cp /etc/shadow ~/local_shadow   ← butuh sudo!

BACA FORMAT dari output unshadow:
  Lihat karakter setelah $ pertama → $6$ = sha512crypt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 SINGLE CRACK MODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cara kerja: John buat wordlist sendiri dari USERNAME → tidak butuh wordlist luar
Teknik    : Word Mangling → mutasi username jadi variasi password
            Contoh username "Markus" → Markus1, MArkus, Markus!, markus123, dst
GECOS     : John juga baca field ke-5 di /etc/passwd (nama lengkap, info user)
            → dipakai sebagai bahan tambahan tebakan password

PERSIAPAN : File hash HARUS ada username di depannya!
  Format  : username:hash
  Contoh  : joker:7bf6d9bb82bed1302f331fc6b816aada

Sintaks   : john --single --format=[format] [file hash]
Contoh    : john --single --format=raw-md5 hash.txt

PERBEDAAN MODE:
  --wordlist = kamu sediakan wordlist, John pakai
  --single   = John buat wordlist sendiri dari username, tidak butuh wordlist

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CUSTOM RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fungsi    : Definisikan pola mangling sendiri sesuai target
Lokasi    : /etc/john/john.conf (Kali) atau /opt/john/john.conf (AttackBox)
Referensi : Jumbo John sudah punya extensive rules di sekitar baris 678

STRUKTUR RULE:
  [List.Rules:NamaRule]    ← nama rule, dipanggil sebagai argumen
  cAz"[0-9][!£$%@]"       ← pola mangling

MODIFIER UTAMA:
  c   = Kapitalisasi huruf pertama
  Az  = Append (tambah di BELAKANG kata)
  A0  = Prepend (tambah di DEPAN kata)

CHARACTER SET (dalam " " dan [ ]):
  [0-9]    = angka 0 sampai 9
  [0]      = hanya angka 0
  [A-Z]    = semua huruf kapital
  [a-z]    = semua huruf kecil
  [A-z]    = huruf besar dan kecil
  [a]      = hanya huruf a
  [!£$%@]  = simbol ! £ $ % @

CONTOH RULE untuk password "Polopassword1!":
  [List.Rules:PoloPassword]
  cAz"[0-9][!£$%@]"
  → c = kapital huruf pertama
  → Az = tambah di belakang
  → [0-9] = angka
  → [!£$%@] = simbol

PAKAI RULE:
  john --wordlist=[path] --rule=NamaRule [file hash]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CRACK ZIP & RAR (TOOL KONVERSI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
POLA UMUM: [format]2john → konversi → output txt → john crack

ZIP:
  zip2john [zip file] > [output file]
  john --wordlist=/usr/share/wordlists/rockyou.txt [output file]
  Buka zip : unzip [file.zip] → masukkan password

RAR:
  rar2john [rar file] > [output file]           ← atau /opt/john/rar2john
  john --wordlist=/usr/share/wordlists/rockyou.txt [output file]
  Buka rar : unrar x [file.rar] → masukkan password
             unrar e = ekstrak tanpa struktur folder
             unrar x = ekstrak dengan struktur folder

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CRACK SSH PRIVATE KEY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
File      : id_rsa = private key SSH yang dilindungi passphrase
Tool      : ssh2john (atau python /usr/share/john/ssh2john.py di Kali)

Sintaks   : ssh2john [id_rsa file] > [output file]
Contoh    : python3 /opt/john/ssh2john.py id_rsa > id_rsa_hash.txt
Crack     : john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt

Login SSH setelah crack:
  ssh -i id_rsa user@[IP] → masukkan passphrase yang sudah di-crack

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 RINGKASAN SEMUA TOOL KONVERSI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
unshadow  → gabung /etc/passwd + /etc/shadow untuk crack Linux hash
zip2john  → konversi ZIP ke hash format John
rar2john  → konversi RAR ke hash format John
ssh2john  → konversi id_rsa SSH key ke hash format John

POLA SELALU SAMA:
  [tool]2john [file input] > [file output]
  john --wordlist=rockyou.txt [file output]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 ISTILAH & KONSEP PENTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hash           = representasi fixed-length dari data, satu arah
Dictionary Attack = hash semua kata di wordlist, bandingkan dengan target
Word Mangling  = mutasi kata (username) jadi variasi password
GECOS          = field ke-5 di /etc/passwd, berisi info umum user
SAM Database   = tempat Windows simpan hash password user
Pass the Hash  = serangan pakai hash langsung tanpa perlu crack
john.pot       = file cache John → simpan semua hasil crack sebelumnya
P vs NP        = P = mudah dihitung, NP = susah temukan tapi mudah verifikasi
                 Hash = P (mudah buat), Un-hash = NP (mustahil balik)
Wordlist       = daftar kata untuk dictionary attack
RockYou        = wordlist paling populer, 14 juta password dari breach 2009
```