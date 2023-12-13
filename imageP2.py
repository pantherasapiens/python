from PIL import Image #, ImageFilter

# Open an image file
input_image_path = "avatar.jpeg"
output_image_path = "output_avatar.jpeg"

image = Image.open(input_image_path)

# Display original image
image.show()

# Resize the image
resized_image = image.resize((300, 200))
resized_image.save("resized_image.jpg")
resized_image.show()

# Convert the image to grayscale
grayscale_image = image.convert("L")
grayscale_image.save("grayscale_image.jpg")
grayscale_image.show()

# Apply a blur filter
# blurred_image = image.filter(ImageFilter.BLUR)
# blurred_image.save("blurred_image.jpg")
# blurred_image.show()

# Rotate the image
# rotated_image = image.rotate(45)
# rotated_image.save("rotated_image.jpg")
# rotated_image.show()

# Crop a region from the image
# cropped_image = image.crop((100, 100, 400, 300))
# cropped_image.save("cropped_image.jpg")
# cropped_image.show()
