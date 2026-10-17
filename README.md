# Klasifikasi Fashion-MNIST dengan CNN (Tugas Kelompok 2)

Aplikasi Streamlit untuk mengklasifikasikan foto produk fashion ke 10 kelas Fashion-MNIST.
Model: `fashion_mnist_cnn_tuned.keras` (akurasi test Fashion-MNIST 90,70%).

Versi online (tanpa instalasi): https://fashion-mnist-kelompok4.streamlit.app

## Dependensi

Program yang harus ada di komputer:

| Program | Versi | Keterangan |
|---|---|---|
| Git | bebas | untuk mengambil repo |
| Python | 3.10 sampai 3.13 | di Linux/macOS, `run.sh` mengunduh Python 3.12 otomatis jika tidak ada |
| Koneksi internet | - | instalasi pertama mengunduh sekitar 500 MB |

Paket Python (dipasang otomatis oleh skrip dari `requirements.txt`):

| Paket | Versi |
|---|---|
| tensorflow-cpu (Windows/Linux) atau tensorflow (macOS) | 2.21 |
| keras | 3.15 |
| streamlit | 1.66 |
| pillow, numpy, pandas | terbaru |

## Instalasi dan menjalankan (salin-tempel)

Pilih sesuai sistem operasi. Salin satu blok, tempel di terminal, tekan Enter. Setelah muncul `Local URL: http://localhost:8501`, buka alamat itu di browser. Jangan tutup terminal selama aplikasi dipakai.

### Windows (PowerShell)

```
winget install -e --id Git.Git
winget install -e --id Python.Python.3.12
```

Tutup PowerShell, buka lagi, lalu:

```
git clone https://github.com/jonatansetiabayupermana01-eng/fashion-mnist-cnn-streamlit.git
cd fashion-mnist-cnn-streamlit
.\run.bat
```

### Ubuntu / Debian / Linux Mint

```
sudo apt update && sudo apt install -y git curl python3 python3-venv
git clone https://github.com/jonatansetiabayupermana01-eng/fashion-mnist-cnn-streamlit.git
cd fashion-mnist-cnn-streamlit
bash run.sh
```

### Fedora

```
sudo dnf install -y git curl python3
git clone https://github.com/jonatansetiabayupermana01-eng/fashion-mnist-cnn-streamlit.git
cd fashion-mnist-cnn-streamlit
bash run.sh
```

### Arch Linux

```
sudo pacman -S --needed git curl python
git clone https://github.com/jonatansetiabayupermana01-eng/fashion-mnist-cnn-streamlit.git
cd fashion-mnist-cnn-streamlit
bash run.sh
```

### macOS

```
xcode-select --install
git clone https://github.com/jonatansetiabayupermana01-eng/fashion-mnist-cnn-streamlit.git
cd fashion-mnist-cnn-streamlit
bash run.sh
```

### NixOS

```
nix-shell -p git --run "git clone https://github.com/jonatansetiabayupermana01-eng/fashion-mnist-cnn-streamlit.git"
cd fashion-mnist-cnn-streamlit
bash run.sh
```

Di NixOS, `run.sh` otomatis masuk ke `nix-shell` (lihat `shell.nix`) yang menyediakan Python 3.12 dan library yang dibutuhkan TensorFlow. Jika `nix-shell` tidak menemukan `<nixpkgs>`:

```
nix-shell -I nixpkgs=https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz shell.nix --run "bash run.sh"
```

## Menjalankan lagi

Dari dalam folder repo, jalankan `bash run.sh` (Linux/macOS/NixOS) atau `.\run.bat` (Windows). Instalasi tidak diulang.

## Memperbarui repo

```
cd fashion-mnist-cnn-streamlit
git pull
```

## Masalah umum

| Pesan | Penyebab | Solusi |
|---|---|---|
| `destination path ... already exists` | folder sudah ada dari clone sebelumnya | `cd fashion-mnist-cnn-streamlit && git pull` |
| `ERR_CONNECTION_REFUSED` di browser | server belum jalan atau terminal ditutup | tunggu sampai muncul `Local URL`, biarkan terminal terbuka |
| `Butuh Python 3.10 sampai 3.13` (Windows) | Python belum terpasang atau versinya tidak didukung | jalankan `winget install -e --id Python.Python.3.12`, buka ulang terminal |
| `No module named venv` (Debian/Ubuntu) | paket venv belum ada | `sudo apt install -y python3-venv` |

## Cara manual

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
