import cv2
import numpy as np
from tkinter import Tk, simpledialog, messagebox
import matplotlib.pyplot as plt

# Function to retrieve the hidden image from a specific bit plane in a single channel
def retrieve_hidden_image_from_channel(stego_channel, bit_plane):
    # Get the dimensions of the stego channel
    visible_rows, visible_columns = stego_channel.shape
    recovered_watermark = np.zeros((visible_rows, visible_columns), dtype=np.uint8)
    
    # Extract the specified bit plane
    for row in range(visible_rows):
        for column in range(visible_columns):
            recovered_watermark[row, column] = (stego_channel[row, column] >> (bit_plane - 1)) & 1
    
    # Scale the binary image to 0-255
    recovered_watermark *= 255
    
    return recovered_watermark

# Read the image that has another image hidden into it
base_file_name = 'tst.png'
folder = r'C:\Users\hi\OneDrive\Desktop\VITB notes\Personel_project\Steganography'
full_file_name = f"{folder}/{base_file_name}"

# Check if file exists
try:
    stego_image = cv2.imread(full_file_name)
    if stego_image is None:
        raise FileNotFoundError
except FileNotFoundError:
    messagebox.showerror("Error", f"Error: {full_file_name} does not exist.")
    exit()

# Get the bit plane to retrieve the image from stego_img
Tk().withdraw()  # Hide the root window
bit_plane = simpledialog.askinteger("Enter Bit Plane to Retrieve", "Enter the bit plane you want to retrieve the image from (1 - 8)", minvalue=1, maxvalue=8)

# Retrieve the hidden image from each color channel
recovered_watermark_blue = retrieve_hidden_image_from_channel(stego_image[:, :, 0], bit_plane)
recovered_watermark_green = retrieve_hidden_image_from_channel(stego_image[:, :, 1], bit_plane)
recovered_watermark_red = retrieve_hidden_image_from_channel(stego_image[:, :, 2], bit_plane)

# Combine the recovered watermark channels into a single color image
recovered_watermark_color = cv2.merge((recovered_watermark_blue, recovered_watermark_green, recovered_watermark_red))

# Display the images
plt.figure(figsize=(10, 8))
plt.subplot(3, 3, 9)
plt.imshow(cv2.cvtColor(recovered_watermark_color, cv2.COLOR_BGR2RGB))
caption = f'Watermark Recovered\nfrom Bit Plane {bit_plane}\nof Stego Image'
plt.title(caption, fontsize=12)
plt.show()

# messagebox.showinfo("Done", "Done with demo!")
