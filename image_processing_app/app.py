import cv2 as cv
import numpy as np
import streamlit as st
from PIL import Image
from processors.edges import laplacian, sobel, canny

st.title("Image Processing App")

uploaded = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Step 1 - pick category
category = st.sidebar.selectbox("Category", [
    "Edges",
    "Filters",
    "Transforms",
])

# Step 2 - pick technique under that category
if category == "Edges":
    technique = st.sidebar.selectbox("Technique", [
        "Canny",
        "Sobel",
        "Laplacian",
    ])
elif category == "Filters":
    technique = st.sidebar.selectbox("Technique", [
        "Gaussian Blur",
        "Median Blur",
        "Box Blur",
        "Custom Kernel",
    ])
elif category == "Transforms":
    technique = st.sidebar.selectbox("Technique", [
        "Rotation",
        "Perspective Transform",
        "Affine Transform",
    ])

if uploaded:
    file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
    img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)

    col1, col2 = st.columns(2)
    col1.image(cv.cvtColor(img, cv.COLOR_BGR2RGB), caption="Original")

    # Edges
    if technique == "Canny":
        result = canny(img)
    elif technique == "Sobel":
        result = sobel(img)
    elif technique == "Laplacian":
        result = laplacian(img)

    col2.image(result, caption=technique)