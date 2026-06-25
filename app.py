from flask import Flask, render_template, request
import numpy as np
import cv2
from keras.models import load_model
from PIL import Image

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5MB upload limit

# Load model
model = load_model("signature_model.h5")

SIZE = 224

# Prediction function
def predict_signature(image):
    # Convert PIL to numpy
    img = np.array(image)

    # Resize
    img = cv2.resize(img, (SIZE, SIZE))

    # Normalize
    img = img / 255.0

    # Reshape
    img = img.reshape(1, SIZE, SIZE, 3)

    # Predict
    pred = model.predict(img)
    class_idx = np.argmax(pred, axis=1)[0]

    if class_idx == 1:
        return "Forged Signature ❌"
    else:
        return "Genuine Signature ✅"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():
    result = None

    if request.method == "POST":
        file = request.files.get("file")

        if not file or file.filename == "":
            return render_template("verify.html", result="No file uploaded ❌")

        # Basic upload hardening
        allowed_ext = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".gif"}
        filename = file.filename
        ext = "" + filename[filename.rfind("."):].lower() if "." in filename else ""
        if ext not in allowed_ext:
            return render_template("verify.html", result="Unsupported file type ❌")

        # Optional: cap request size (Flask also supports MAX_CONTENT_LENGTH)
        image = None
        try:
            image = Image.open(file.stream).convert("RGB")
            result = predict_signature(image)
        except Exception:
            result = "Invalid image or failed to process ❌"

    return render_template("verify.html", result=result)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # Production note: run with a real WSGI server.
    # Example (Windows): waitress-serve --listen=0.0.0.0:5000 app:app
    app.run(host="0.0.0.0", port=5000, debug=False)
