from PIL import Image, ImageFilter, ImageChops, ImageEnhance

def cartoonize_pil(input_path, output_path):
    # Open the image
    image = Image.open(input_path)

    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Apply a blur filter
    blurred_image = grayscale_image.filter(ImageFilter.BLUR)

    # Create an edge image by finding the difference between the grayscale and blurred images
    edge_image = ImageChops.difference(grayscale_image, blurred_image)

    # Increase the contrast of the edge image
    edge_image = ImageEnhance.Contrast(edge_image).enhance(2.0)

    # Combine the grayscale and edge images to create a cartoon effect
    cartoon_image = ImageChops.add(grayscale_image, edge_image)

    # Save the cartoonized image
    cartoon_image.save(output_path)

# Example usage
cartoonize_pil("img.jpg", "cartoonized_image_pil.jpg")
