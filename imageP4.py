import cv2

def cartoonize_cv2(input_path, output_path):
    # Read the image
    image = cv2.imread(input_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a bilateral filter to smooth the image while keeping the edges sharp
    smooth = cv2.bilateralFilter(gray, d=9, sigmaColor=300, sigmaSpace=75)

    # Use the adaptive thresholding to create an edge mask
    edges = cv2.adaptiveThreshold(smooth, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 15)

    # Combine the smoothed image with the edge mask
    cartoon = cv2.bitwise_and(image, image, mask=edges)

    # Save the cartoonized image
    cv2.imwrite(output_path, cartoon)

# Example usage
cartoonize_cv2("img.jpg", "cartoonized_image_cv2.jpg")
