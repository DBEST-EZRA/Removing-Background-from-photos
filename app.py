from flask import Flask, request, send_file, jsonify
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Background Removal API is running."


@app.route("/remove-background", methods=["POST"])
def remove_background():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    uploaded_file = request.files['image']

    if uploaded_file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    try:
        input_bytes = uploaded_file.read()
        output_bytes = remove(input_bytes)

        return send_file(
            io.BytesIO(output_bytes),
            mimetype='image/png',
            download_name='no_background.png',
            as_attachment=True
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
