from flask import Flask, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route("/")
def home():
    return "Background Removal API is running."

@app.route("/remove-background", methods=["GET"])
def remove_background():
    try:
        # Assuming 'logo.jpg' is in the same folder as app.py
        with open("logo.jpg", "rb") as f:
            input_data = f.read()

        output_data = remove(input_data)

        return send_file(
            io.BytesIO(output_data),
            mimetype="image/png",
            download_name="logo_no_bg.png",
            as_attachment=True
        )
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
