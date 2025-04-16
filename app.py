import streamlit as st
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Streamlit app title
st.title("TIF to Text Converter")

# Option to upload a TIF file
tif_file = st.file_uploader("Upload a TIF image", type=["tif", "tiff"])

# Option to load a TIF file from a URL
url = st.text_input("Or enter a TIF image URL")

# Process the uploaded file
if tif_file is not None:
    image = Image.open(tif_file)
    st.image(image, caption="Uploaded TIF Image", use_column_width=True)

    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(image)
    st.subheader("Extracted Text:")
    st.text(extracted_text)

# Process the URL
elif url:
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="TIF Image from URL", use_column_width=True)

        extracted_text = pytesseract.image_to_string(image)
        st.subheader("Extracted Text:")
        st.text(extracted_text)
    except Exception as e:
        st.error(f"Error loading image from URL: {e}")

