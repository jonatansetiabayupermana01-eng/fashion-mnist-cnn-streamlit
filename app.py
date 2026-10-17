import os

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

from preprocess import to_fmnist

CLASSES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot",
]
MODEL_FILE = "fashion_mnist_cnn_tuned.keras"
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), MODEL_FILE)


@st.cache_resource
def load_model():
    import tensorflow as tf  # impor di sini agar startup tidak berat

    return tf.keras.models.load_model(MODEL_PATH)


st.set_page_config(page_title="Klasifikasi Fashion-MNIST")
st.title("Klasifikasi Fashion-MNIST")
st.write(
    "Unggah foto satu produk fashion, lalu model CNN akan memprediksi "
    "kelasnya dari 10 kategori."
)

if not os.path.exists(MODEL_PATH):
    st.error(f"Berkas model tidak ditemukan: {MODEL_FILE}")
    st.stop()

uploaded = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png", "webp"])

if uploaded is None:
    st.stop()

original = Image.open(uploaded)
x = to_fmnist(original)

model = load_model()
probs = model.predict(x[np.newaxis, ..., np.newaxis], verbose=0)[0]
top3 = np.argsort(probs)[::-1][:3]

col_a, col_b = st.columns(2)
with col_a:
    st.image(original, caption="Gambar asli")
with col_b:
    preview = Image.fromarray((x * 255).astype(np.uint8)).resize(
        (224, 224), Image.Resampling.NEAREST
    )
    st.image(preview, caption="Input model (28x28, diperbesar)")

best = int(top3[0])
st.subheader(f"Prediksi: {CLASSES[best]}")
st.write(f"Keyakinan: {probs[best] * 100:.1f}%")

st.table(
    pd.DataFrame(
        {
            "Kelas": [CLASSES[i] for i in top3],
            "Probabilitas (%)": [round(float(probs[i]) * 100, 1) for i in top3],
        }
    )
)

st.caption(
    "Catatan: model dilatih pada foto produk 28x28 grayscale dengan latar polos. "
    "Foto dengan latar ramai atau objek kecil dapat salah diklasifikasikan. "
    "Pada uji 19 foto nyata, model benar 8 dari 19 (42%) dan cenderung menebak Bag. "
    "Akurasi 90,7% hanya berlaku untuk data test Fashion-MNIST."
)
