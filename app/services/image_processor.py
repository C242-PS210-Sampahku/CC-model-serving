from PIL import Image
import numpy as np

def preprocess_image(image_stream):
    """
    Preprocess gambar untuk input model.
    """
    # Buka gambar dari stream dan ubah ke RGB
    image = Image.open(image_stream).convert('RGB')

    # Ubah ukuran gambar ke (224, 224)
    image = image.resize((224, 224))

    # Konversi ke array NumPy dan normalisasi
    image_array = np.array(image) / 255.0

    # Tambahkan dimensi batch
    return np.expand_dims(image_array, axis=0)
