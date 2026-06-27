# Introduction to Digital Forensics — TryHackMe Writeup

**Date:** 2026-06-27
**Platform:** TryHackMe
**Difficulty:** Easy
**Category:** Digital Forensics

---

## Overview

This room introduces the fundamentals of digital forensics through a practical scenario: a household cat ("Gado") has been "kidnapped," and the kidnapper sent a ransom note as an MS Word document (converted to PDF), along with an attached photo. The hands-on objective is to use metadata analysis to identify the author of the document and the location/camera used to take the attached photo — demonstrating how everyday digital artifacts (documents, images) leak forensic evidence even when the creator doesn't intend it.

Practical work was performed on a local Kali Linux VM rather than the provided AttackBox, using the room's case files (`ransom-letter.pdf`, `ransom-letter.doc`, `letter-image.jpg`).

## Tools Used

- `pdfinfo` (part of `poppler-utils`) — extract metadata from PDF files
- `exiftool` (part of `libimage-exiftool-perl`) — extract EXIF metadata from image files
- Bing Maps — reverse-lookup GPS coordinates to a physical address/street
- Standard Linux file management (`mkdir`, `cd`, `mv`, `ls`)

---

## Task 5 — Practical Example of Digital Forensics

**Objective:** Using the ransom note (PDF) and attached image, determine: (1) the author of the PDF, (2) the street name where the attached photo was taken, and (3) the camera model used to take the photo.

**Approach:**

The case files were first inspected at the file-manager level to get a baseline (file type, size, and timestamps) before touching them in the terminal — a habit worth keeping since file-manager metadata can sometimes hint at inconsistencies before deeper tools are used.

> 📸 ![download task file](../docs/docs%20hands%20on/part%205/01-download-task-files.png)

A dedicated working directory was created to keep the case files isolated from the rest of the home directory, mirroring the chain-of-custody principle of keeping evidence in a controlled, identifiable location:

```bash
mkdir -p ~/Rooms/introdigitalforensics
cd ~/Rooms/introdigitalforensics
```
- `mkdir -p` — creates the directory, including any missing parent directories, without erroring if it already exists.
- `cd` — switches the working directory so subsequent commands operate on the case files directly.

> 📸 `07-buat-direktori-kerja.png`

The case files (provided as a shared VM folder) were moved into the working directory:

```bash
mv /media/sf_ShareVM/ransom-lettter-2/* ~/Rooms/introdigitalforensics
```
- `mv` — moves the files; `*` expands to all files inside the source folder, so every case file is relocated in one command.

> 📸 `08-pindahkan-file-ke-direktori-kerja.png`

**Step 1 — Identify the PDF author.**

`pdfinfo` was not installed by default on this Kali VM, so it was installed first:

```bash
sudo apt update
sudo apt install poppler-utils -y
```
- `sudo apt update` — refreshes the local package index against the Kali mirrors; this resolved an earlier `404 Not Found` error caused by a stale package cache pointing to a `.deb` version no longer hosted on the mirror.
- `apt install poppler-utils -y` — installs the package providing `pdfinfo`; `-y` auto-confirms the installation prompt.

> 📸 `09-install-poppler-utils.png`

With the tool installed, the PDF metadata was read directly:

```bash
pdfinfo ransom-letter.pdf
```
- No flags were needed — `pdfinfo` dumps all available metadata fields (Title, Subject, Author, Creator, Producer, CreationDate, etc.) by default.

The output revealed the document's **Author** field directly in the metadata, despite no author name appearing anywhere in the visible ransom note text — a reminder that document metadata can deanonymize an author even when the visible content is deliberately vague.

> 📸 `10-jalankan-pdfinfo-ransom-letter.png`

**Step 2 & 3 — Identify the photo's location (street) and camera model.**

`exiftool` likewise needed to be installed:

```bash
sudo apt install libimage-exiftool-perl
```
- Installs the Perl-based ExifTool package used to read/write metadata in image files.

> 📸 `11-install-libimage-exiftool-perl.png`

EXIF data was then extracted from the attached photo:

```bash
exiftool letter-image.jpg
```
- No flags needed — by default `exiftool` prints every embedded metadata tag it can find.

The first page of output included the **Make** and **Camera Model Name** fields, immediately answering the camera-model question.

> 📸 `12-jalankan-exiftool-letter-image-bagian-1.png`

Scrolling further into the output revealed the embedded **GPS Latitude**, **GPS Longitude**, and combined **GPS Position** fields, along with lens details (Lens ID, Focal Length).

> 📸 `13-jalankan-exiftool-letter-image-bagian-2.png`

The raw GPS coordinate format from `exiftool` (`51 deg 30' 51.90" N, 0 deg 5' 38.73" W`) is not directly accepted by most map search bars. It had to be reformatted by replacing `deg` with the degree symbol `°` and removing extra whitespace:

```
51°30'51.9"N 0°5'38.73"W
```

This was searched on Bing Maps, which resolved to a specific address in London:

> 📸 `14-cari-koordinat-gps-di-bing-maps.png`

Zooming into the resulting pin on the map confirmed the exact street name where the photo was taken:

> 📸 `15-zoom-lokasi-nama-jalan.png`

**Result:**

All three room questions were answered correctly and validated by the platform:

| Question | Answer |
|---|---|
| Author of `ransom-letter.pdf` | `Ann Gree Shepherd` |
| Street where the photo was taken | `Milk Street` |
| Camera model used | `Canon EOS R6` |

> 📸 `16-jawaban-benar-semua-soal.png`

---

## Proof of Completion

```
Q1 (PDF Author):        Ann Gree Shepherd
Q2 (Street name):       Milk Street
Q3 (Camera model):      Canon EOS R6
```
> 📸 `16-jawaban-benar-semua-soal.png`

---

## Lessons Learned

- **Document metadata can deanonymize authors** even when the visible content of a file is deliberately anonymous or vague — `pdfinfo`/`exiftool`-style metadata extraction should be a default step when investigating any suspicious document.
- **EXIF GPS data in photos is a major OPSEC leak.** Smartphones and many digital cameras embed precise GPS coordinates by default; unless explicitly stripped, any shared photo can reveal the exact location it was taken — relevant both for forensic investigators and for red-team/OSINT engagements where geolocating a target via shared images is a common technique.
- **Coordinate format matters for tooling interoperability** — `exiftool`'s raw DMS (degrees/minutes/seconds) output isn't directly map-search-compatible; minor reformatting (replacing `deg` with `°`, trimming whitespace) is often needed when piping forensic tool output into other tools/services.
- **Stale `apt` package indices cause confusing 404 errors** — when a Kali install fails with `404 Not Found` on a specific `.deb`, running `sudo apt update` first (to resync the package index with the mirror) is the standard first troubleshooting step, before assuming the mirror itself is broken.
- This exercise mirrors real-world OSINT/forensic workflows used in incident response and threat intelligence: extracting and correlating metadata across multiple file types (PDF + image) to build an evidentiary picture of an anonymous actor.

---

## Notes / Items to Fill In Manually

- This writeup only covers **Task 5 (Practical Example of Digital Forensics)** — Tasks 1–4 in this room were pure theory/conceptual content (definitions, NIST phases, forensics types, evidence acquisition principles, Windows forensics tooling overview) with no hands-on commands executed, so per the writeup scope they were intentionally excluded.
- No sensitive real-world data (real IPs, credentials, hashes, or real personal/client information) was found in this room — all names, the GPS location, and the camera details belong to the room's fictional training scenario, so no redaction was necessary.
- Screenshot files `06-` through `16-` referenced above correspond to the images you captured during the actual hands-on session on your own Kali VM — make sure these are saved/renamed accordingly in your screenshots folder before publishing.