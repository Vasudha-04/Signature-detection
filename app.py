from flask import Flask, render_template, request
import numpy as np
import cv2
from keras.models import load_model
from PIL import Image

app = Flask(__name__)

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
        file = request.files["file"]

        if file:
            image = Image.open(file).convert("RGB")
            result = predict_signature(image)

    return render_template("verify.html", result=result)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)