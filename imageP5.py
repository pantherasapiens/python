import cv2
import numpy as np

def cartoonize_advanced(input_path, output_path):
    # Read the image
    img = cv2.imread(input_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filter to smooth the image and reduce noise
    smooth = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=75)

    # Use the adaptive thresholding to create an edge mask
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 15)

    # Stylization for a painterly effect
    stylized = cv2.stylization(img, sigma_s=150, sigma_r=0.25)

    # Color quantization for a flat cartoon-like appearance
    num_colors = 20
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(np.float32(stylized).reshape(-1, 3), num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    segmented = centers[np.uint8(labels.flatten())].reshape(img.shape)

    # Enhance details using the bilateral filter
    details = cv2.detailEnhance(segmented, sigma_s=10, sigma_r=0.15)

    # Combine the smoothed image with the edge mask
    cartoon = cv2.bitwise_and(details, details, mask=edges)

    # Save the cartoonized image
    cv2.imwrite(output_path, cartoon)

# Example usage
cartoonize_advanced("img.jpg", "cartoonized_image_advanced.jpg")
