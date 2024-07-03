import cv2
import numpy as np
import matplotlib.pyplot as plt

def watermark_image(original_image, hidden_image, bit_to_set):
    # Convert color image to grayscale
    if len(original_image.shape) > 2:
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Resize the cover image to the same size as the hidden image
    original_image = cv2.resize(original_image, (hidden_image.shape[1], hidden_image.shape[0]))

    # Threshold the hidden image
    _, binary_image = cv2.threshold(hidden_image, 70, 255, cv2.THRESH_BINARY)

    # Convert watermark to uint8
    watermark = binary_image.astype(np.uint8)

    # Set the bit of original image to the value of the watermark
    watermarked_image = np.copy(original_image)
    watermarked_image = np.bitwise_or(watermarked_image, (watermark << (bit_to_set - 1)))

    return watermarked_image

# Read the original and hidden images
original_image = cv2.imread('bright.png', cv2.IMREAD_GRAYSCALE)
hidden_image = cv2.imread('qr.jpg', cv2.IMREAD_GRAYSCALE)

# Get the bit plane to hide the image in
bit_to_set = int(input('Enter the bit plane you want to hide the image in (1 - 8): '))

# Watermark the image
watermarked_image = watermark_image(original_image, hidden_image, bit_to_set)

# Save the watermarked image to a file
# output_file = 'watermarked_image.bmp'
# cv2.imwrite(output_file, watermarked_image)
# print(f'Watermarked image saved as {output_file}')

# Display the images
plt.figure(figsize=(10, 8))

plt.subplot(3, 3, 1)
plt.imshow(hidden_image, cmap='gray')
plt.title('Image to be Hidden')

plt.subplot(3, 3, 2)
plt.hist(hidden_image.ravel(), bins=256, range=(0, 255))
plt.title('Histogram of Image to be Hidden')

plt.subplot(3, 3, 3)
plt.imshow(cv2.threshold(hidden_image, 70, 255, cv2.THRESH_BINARY)[1], cmap='gray')
plt.title('Thresholded Image')

plt.subplot(3, 3, 4)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')

plt.subplot(3, 3, 5)
plt.imshow(hidden_image, cmap='gray')
plt.title(f'Hidden Image\nBit Plane {bit_to_set}')

plt.subplot(3, 3, 6)
plt.imshow(watermarked_image, cmap='gray')
plt.title('Watermarked Image')

plt.tight_layout()
plt.show()
