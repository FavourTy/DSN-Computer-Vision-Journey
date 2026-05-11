import cv2 as cv
import numpy as np
import streamlit as st
from PIL import Image
from processors.edges import laplacian, sobel, canny
from processors.filters import blur, medianBlur, gaussianBlur, kernel
from processors.thresholding import binary, binaryInverse, otsu, adaptiveGaussian, adaptiveMean, zero

st.title("Image Processing App")

uploaded = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Step 1 - pick category
category = st.sidebar.selectbox("Category", [
    "Edges",
    "Filters",
    "Transforms",
    "Thresholding"
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
elif category == "Thresholding":
    technique = st.sidebar.selectbox("Technique", [
        "Zero",
        "Binary",
        "Binary Inverse"
        "Otsu",
        "Adaptive Mean",
        "Adaptive Gaussian"
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
  
    #Filters
    if technique == "Gaussian Blur":
        result = gaussianBlur(img)
    elif technique == "Median Blur":
        result = medianBlur(img)
    elif technique == "Box Blur":
        result = blur(img)
    elif technique == "Custom Kernel":
        result = kernel(img)
    
    #Thresholding
    if technique == "Zero":
        result = zero(img)
    elif technique == "Binary":
        result = binary(img)
    elif technique == "Binary Inverse":
        result = binaryInverse(img)
    elif technique == "Otsu":
        result = otsu(img)
    elif technique == "Adaptive Mean":
        result = adaptiveMean(img)
    elif technique == "Adaptive Gaussian":
        result = adaptiveGaussian(img)
    
    col2.image(result, caption=technique)