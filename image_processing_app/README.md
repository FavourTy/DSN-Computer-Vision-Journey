# Image Processing App

Hola! Welcome to my Computer Vision Journey project. This is a simple, interactive Image Processing App built with Python, OpenCV, and Streamlit. It allows you to easily apply different computer vision techniques to your images straight from your browser. 

I'm mainly using this project to get hands-on experience with core computer vision concepts.

*(Note: I plan to add a demo video here later on so you can see it in action without running it!)*

## Features

The app is broken down into several image processing categories. You just upload an image, pick a category, choose a specific technique, and the app displays the original and processed image side-by-side!

Here's what you can currently play around with:

- **Edges**: Canny, Sobel, Laplacian
- **Filters**: Gaussian Blur, Median Blur, Box Blur, Custom Kernel (includes an adjustable blur strength slider for some filters!)
- **Transforms**: Resize, Translation, Shear, Rotation, Perspective Transform, Affine Transform (with interactive sliders to adjust angles and shifts)
- **Thresholding**: Zero, Binary, Binary Inverse, Otsu, Adaptive Mean, Adaptive Gaussian
- **Morphology**: Opening
- **Segmentation**: Watershed

## Technologies Used

- **Python**: Core programming language.
- **OpenCV**: The backbone for all the image processing tasks.
- **Streamlit**: Used to quickly spin up the interactive web UI.
- **NumPy & Pillow (PIL)**: For handling image arrays and byte conversions.

## How to Run It Locally

If you'd like to run this app on your own machine, just follow these steps:

1. Clone this repository (or download the source).
2. Make sure you have the required dependencies installed. You can install them using:
   ```bash
   pip install opencv-python numpy streamlit pillow
   ```
3. Navigate to the folder containing `app.py`.
4. Run the Streamlit app by executing:
   ```bash
   streamlit run app.py
   ```
5. Open the local URL provided in your terminal (usually `http://localhost:8501`) in your web browser.

## Thoughts / Contributing

This is mainly a personal learning project, but if you have suggestions, tips, or want to point out a bug, feel free to open an issue or drop a PR!

---
Thanks for checking out my computer vision journey!
