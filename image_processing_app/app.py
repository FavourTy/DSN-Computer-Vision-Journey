import cv2 as cv
import numpy as np
import streamlit as st
from PIL import Image
from processors.edges import laplacian, sobel, canny
from processors.filters import blur, medianBlur, gaussianBlur, kernel
from processors.thresholding import binary, binaryInverse, otsu, adaptiveGaussian, adaptiveMean, zero
from processors.morphology import opening
from processors.segmentation import watershedSegment
from processors.transforms import resize, rotation, translation, shear, perspective_transform, affine_transform

st.title("Image Processing App")

uploaded = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Step 1 - pick category
category = st.sidebar.selectbox("Category", [
    "Edges",
    "Filters",
    "Transforms",
    "Thresholding",
    "Morphology",
    "Segmentation"
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
        "Resize",
        "Translation",
        "Shear",
        "Rotation",
        "Perspective Transform",
        "Affine Transform",
    ])
elif category == "Thresholding":
    technique = st.sidebar.selectbox("Technique", [
        "Zero",
        "Binary",
        "Binary Inverse",
        "Otsu",
        "Adaptive Mean",
        "Adaptive Gaussian"
    ])
elif category =="Morphology":
    technique = st.sidebar.selectbox("Techique", [
        "Opening"
    ])
elif category == "Segmentation":
    technique = st.sidebar.selectbox("Technique", [
        "Watershed"
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
    if technique in ["Gaussian Blur", "Median Blur", "Box Blur"]:
        k = st.sidebar.slider("Blur strength", 1, 51, 15, step=2)

    if technique == "Gaussian Blur":
        result = gaussianBlur(img, k)
    elif technique == "Median Blur":
        result = medianBlur(img, k)
    elif technique == "Box Blur":
        result = blur(img, k)
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
    
    #Morphology
    if technique == "Opening":
        result = opening(img)

    #Segmentation
    if technique == "Watershed":
        result = watershedSegment(img)

    #Transforms
    if technique == "Rotation":
        angle = st.sidebar.slider("Angle", 0, 360, 45)
    if technique == "Shear":
        shear_factor = st.sidebar.slider("Shear factor", 0.1, 1.0, 0.3)
    if technique == "Translation":
        shift_x = st.sidebar.slider("Shift X", 0, 300, 100)
        shift_y = st.sidebar.slider("Shift Y", 0, 300, 50)

    if technique == "Resize":
        result = resize(img)
    elif technique == "Translation":
        result = translation(img, shift_x, shift_y)
    elif technique == "Shear":
        result = shear(img, shear_factor)
    elif technique == "Rotation":
        result = rotation(img, angle)
    elif technique == "Perspective Transform":
        result = perspective_transform(img)
    elif technique == "Affine Transform":
        result = affine_transform(img)

    col2.image(result, caption=technique)