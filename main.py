from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model('model_fixed.h5')

# Preprocessing gambar
def preprocess_image(image):
    # Ubah ukuran gambar sesuai input model (224x224)
    image = image.resize((224, 224))
    # Konversi ke array NumPy dan normalisasi (0-1)
    image_array = np.array(image) / 255.0
    # Tambahkan dimensi batch (1, 224, 224, 3)
    return np.expand_dims(image_array, axis=0)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil file gambar dari request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        file = request.files['file']

        # Buka gambar menggunakan PIL
        image = Image.open(file.stream).convert('RGB')

        # Preprocess gambar
        input_data = preprocess_image(image)  # Pastikan preprocess_image didefinisikan dengan benar

        # Lakukan prediksi
        predictions = model.predict(input_data)

        # Ambil hasil prediksi dengan confidence tertinggi
        predicted_class = tf.argmax(predictions[0]).numpy()
        confidence = predictions[0][predicted_class] * 100

        # Daftar nama kelas
        class_names = ['battery', 'bio', 'cardboard', 'clothes', 'glass', 'metal', 'paper', 'plastic', 'shoes', 'trash']

        return jsonify({
            'predicted_class': int(predicted_class),
            'confidence': float(confidence),
            'prediction_result': class_names[predicted_class]
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
