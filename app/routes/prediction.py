from flask import Blueprint, request, jsonify
from app.services.model_handler import predict_image

bp = Blueprint('prediction', __name__)

@bp.route('/predict', methods=['POST'])
def predict_endpoint():
    try:
        # Periksa apakah file ada di request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        file = request.files['file']

        # Prediksi gambar
        result = predict_image(file.stream)

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
