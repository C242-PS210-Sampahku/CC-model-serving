import tensorflow as tf
from app.services.image_processor import preprocess_image

# Load model saat aplikasi dimulai
model = tf.keras.models.load_model('app/models/model_fixed.h5')

# Daftar nama kelas
class_names = ['battery', 'bio', 'cardboard', 'clothes', 'glass', 'metal', 'paper', 'plastic', 'shoes', 'trash']

def predict_image(image_stream):
    """
    Melakukan prediksi pada gambar yang diberikan.
    """
    # Preproses gambar
    input_data = preprocess_image(image_stream)

    # Lakukan prediksi
    predictions = model.predict(input_data)

    # Ambil hasil prediksi
    predicted_class = tf.argmax(predictions[0]).numpy()
    confidence = predictions[0][predicted_class] * 100

    return {
        'predicted_class': int(predicted_class),
        'confidence': float(confidence),
        'prediction_result': class_names[predicted_class]
    }
