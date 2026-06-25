import os
import io

import numpy as np
import cv2
from PIL import Image
import streamlit as st
from keras.models import load_model

st.set_page_config(page_title="SignatureGuard", page_icon="✅", layout="centered")

SIZE = 224
MODEL_PATH = "signature_model.h5"

@st.cache_resource(show_spinner=False)
def get_model():
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found: {MODEL_PATH}")
        st.stop()
    return load_model(MODEL_PATH)

model = get_model()

def predict_signature(pil_image: Image.Image) -> str:
    img = np.array(pil_image)
    img = cv2.resize(img, (SIZE, SIZE))
    img = img / 255.0
    img = img.reshape(1, SIZE, SIZE, 3)

    pred = model.predict(img)
    class_idx = int(np.argmax(pred, axis=1)[0])

    return "Forged Signature ❌" if class_idx == 1 else "Genuine Signature ✅"

st.title("SignatureGuard")
st.write("Upload a signature image to check if it looks **Genuine** or **Forged**.")

uploaded = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "bmp", "tif", "tiff", "gif"])

if uploaded is not None:
    try:
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Uploaded signature", use_container_width=True)

        if st.button("Verify", type="primary"):
            with st.spinner("Analyzing signature..."):
                result = predict_signature(image)
            st.success(result)
    except Exception:
        st.error("Invalid image or failed to process.")

