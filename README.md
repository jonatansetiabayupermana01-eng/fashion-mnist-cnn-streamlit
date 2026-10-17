# Klasifikasi Fashion-MNIST dengan CNN (Tugas Kelompok 2)

Aplikasi Streamlit untuk mengklasifikasikan foto produk fashion ke 10 kelas Fashion-MNIST.
Model: `fashion_mnist_cnn_tuned.keras` (akurasi test Fashion-MNIST 90,70%).

Versi online: https://fashion-mnist-kelompok4.streamlit.app

## Jalankan di komputer sendiri

Syarat: Git dan Python 3.10 sampai 3.13.

Windows (Command Prompt):

```
git clone https://github.com/jonatansetiabayupermana01-eng/fashion-mnist-cnn-streamlit.git
cd fashion-mnist-cnn-streamlit
run.bat
```

Linux / macOS:

```
git clone https://github.com/jonatansetiabayupermana01-eng/fashion-mnist-cnn-streamlit.git
cd fashion-mnist-cnn-streamlit
bash run.sh
```

Di NixOS, `bash run.sh` otomatis masuk ke `nix-shell` (lihat `shell.nix`) untuk menyediakan Python 3.12 dan library yang dibutuhkan TensorFlow.

Skrip membuat virtual environment `.venv`, menginstal dependensi (sekali saja, sekitar 500 MB karena TensorFlow), lalu membuka aplikasi di http://localhost:8501. Jalankan perintah yang sama untuk membuka aplikasi lagi.

Cara manual:

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
