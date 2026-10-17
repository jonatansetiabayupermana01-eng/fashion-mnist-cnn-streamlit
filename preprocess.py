"""Ubah foto uji menjadi input 28x28 bergaya Fashion-MNIST (v2).

Mengikuti alur konversi Fashion-MNIST (Xiao et al., 2017, bagian 2):
trim, skala sisi terpanjang ke 28, pusatkan, latar gelap, objek terang.
"""
import numpy as np
from PIL import Image, ImageOps

SIZE = 28
BORDER_BRIGHT = 127   # rata-rata tepi di atas nilai ini berarti latar terang
BORDER_STRIP = 2      # tebal strip tepi (piksel) untuk estimasi latar
FG_FRAC = 0.15        # mask objek: arr > FG_FRAC * max
PCT_LO, PCT_HI = 1, 99  # persentil koordinat mask, mengabaikan piksel liar


def _to_gray_on_white(img):
    """Gabungkan kanal transparansi ke latar putih, lalu ubah ke grayscale."""
    has_alpha = img.mode in ("RGBA", "LA") or (
        img.mode == "P" and "transparency" in img.info
    )
    if has_alpha:
        rgba = img.convert("RGBA")
        bg = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        img = Image.alpha_composite(bg, rgba)
    return img.convert("L")


def _border(arr):
    b = BORDER_STRIP
    return np.concatenate([
        arr[:b, :].ravel(), arr[-b:, :].ravel(),
        arr[:, :b].ravel(), arr[:, -b:].ravel(),
    ])


def to_fmnist(pil_img):
    """PIL.Image -> np.ndarray (28, 28) float32 dengan nilai 0-1, max = 1.0."""
    img = ImageOps.exif_transpose(pil_img)
    img = _to_gray_on_white(img)
    arr = np.asarray(img, dtype=np.float32)

    if _border(arr).mean() > BORDER_BRIGHT:
        arr = 255.0 - arr

    bg = float(np.median(_border(arr)))
    arr = np.clip(arr - bg, 0, None)

    peak = float(arr.max())
    if peak <= 0:
        return np.zeros((SIZE, SIZE), dtype=np.float32)

    mask = arr > FG_FRAC * peak
    ys, xs = np.nonzero(mask)
    y0 = int(np.floor(np.percentile(ys, PCT_LO)))
    y1 = int(np.floor(np.percentile(ys, PCT_HI))) + 1
    x0 = int(np.floor(np.percentile(xs, PCT_LO)))
    x1 = int(np.floor(np.percentile(xs, PCT_HI))) + 1
    crop = arr[y0:y1, x0:x1]

    h, w = crop.shape
    scale = SIZE / max(h, w)
    nh = max(1, int(round(h * scale)))
    nw = max(1, int(round(w * scale)))
    crop_img = Image.fromarray(
        np.clip(np.round(crop), 0, 255).astype(np.uint8), mode="L"
    )
    small = crop_img.resize((nw, nh), Image.Resampling.LANCZOS)

    canvas = Image.new("L", (SIZE, SIZE), 0)
    canvas.paste(small, ((SIZE - nw) // 2, (SIZE - nh) // 2))
    out = np.asarray(canvas, dtype=np.float32)

    m = float(out.max())
    if m > 0:
        out = out / m
    return out.astype(np.float32)


def _check(name, out):
    print(f"[{name}] shape:", out.shape, "dtype:", out.dtype)
    print(f"[{name}] min:", float(out.min()), "max:", float(out.max()))
    print(f"[{name}] corners:", out[0, 0], out[0, -1], out[-1, 0], out[-1, -1])
    assert out.shape == (SIZE, SIZE), out.shape
    assert out.dtype == np.float32
    assert np.isclose(out.max(), 1.0), out.max()
    assert out[0, 0] == 0 and out[0, -1] == 0 and out[-1, 0] == 0 and out[-1, -1] == 0


if __name__ == "__main__":
    # Kasus 1: latar putih, persegi gelap -> objek terang di latar hitam.
    white = Image.new("RGB", (120, 90), (255, 255, 255))
    white.paste(Image.new("RGB", (50, 40), (0, 0, 0)), (35, 25))
    _check("white-bg", to_fmnist(white))

    # Kasus 2: latar abu-abu terang (200), persegi gelap (40) di tengah.
    grey = Image.new("RGB", (120, 90), (200, 200, 200))
    grey.paste(Image.new("RGB", (50, 40), (40, 40, 40)), (35, 25))
    _check("grey-bg", to_fmnist(grey))

    print("self-check OK")
