from PIL import Image
import numpy as np

def calculate_mse(image1, image2):
    np_image1 = np.array(image1)
    np_image2 = np.array(image2)
    mse = np.mean((np_image1 - np_image2) ** 2)
    return mse

# Open the grayscale fingerprint images
fingerprint1 = Image.open("input_sample.jpeg").convert("L")
fingerprint2 = Image.open("grayscale_fingerprint.jpg").convert("L")

# Calculate the mean squared error (MSE)
mse = calculate_mse(fingerprint1, fingerprint2)

# Define a threshold for similarity
similarity_threshold = 100  # Adjust as needed based on your images and requirements

if mse < similarity_threshold:
    print("Fingerprints are similar.")
else:
    print("Fingerprints are not similar.")
