# SignatureGuard — AI-Powered Signature Verification

SignatureGuard is a Flask-based web application that uses Artificial Intelligence and Machine Learning to verify handwritten signatures. The system analyzes uploaded signature images using a pre-trained VGG16-based deep learning model and classifies them as **Genuine** or **Forged** through an intuitive web interface.

## Features

* AI-powered signature verification
* Genuine vs Forged signature classification
* Image preprocessing with resizing and normalization
* Fast real-time prediction
* Simple and user-friendly web interface

## Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** TensorFlow, Keras, VGG16
* **Image Processing:** OpenCV, NumPy, Pillow
* **Frontend:** HTML, CSS, Bootstrap, Jinja Templates

## How It Works

1. The user uploads a signature image.
2. The application preprocesses the image:

   * Converts the image to RGB format
   * Resizes it to 224 × 224 pixels
   * Normalizes pixel values
3. The trained VGG16 model performs inference.
4. The application displays the prediction result:

   * **Forged Signature**
   * **Genuine Signature**

## Setup and Run

### Prerequisites

* Python 3.8 or higher
* pip (Python Package Manager)

### Clone the Repository

```bash
git clone <repository-url>
cd <project-folder>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run (Local)

**Flask (web server):**

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

**Streamlit (recommended for Streamlit hosting):**

```bash
pip install streamlit
streamlit run streamlit_app.py
```

Open:

```text
http://localhost:8501
```


## Usage

1. Launch the application.
2. Open the browser and navigate to the application URL.
3. Upload a signature image.
4. Click the verify button.
5. View the prediction result indicating whether the signature is genuine or forged.

## Supported Image Formats

* JPG
* JPEG
* PNG
* GIF
* BMP
* TIFF

## Limitations

* Prediction accuracy depends on the quality and diversity of the training dataset.
* Blurry, low-resolution, or heavily distorted signatures may affect performance.
* Results are intended for educational and research purposes.


