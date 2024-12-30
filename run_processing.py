import sys
import os

# Add the root directory of the project to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from processing.preprocess import preprocess_image
from processing.segment import segment_image

# Define directories
raw_dir = "/home/mukthar/MediScan/data/gaussian_filtered_images/gaussian_filtered_images/Mild"       # Input: Raw images
preprocessed_dir = "output/preprocessed/Mild"       # Output: Preprocessed images
segmented_dir = "output/segmented/Mild"             # Output: Segmented images

# Step 1: Preprocess all images
print("Preprocessing images...")
for file_name in os.listdir(raw_dir):
    input_path = os.path.join(raw_dir, file_name)
    preprocess_image(input_path, preprocessed_dir)

# Step 2: Segment all preprocessed images
print("Segmenting images...")
for file_name in os.listdir(preprocessed_dir):
    input_path = os.path.join(preprocessed_dir, file_name)
    segment_image(input_path, segmented_dir)

print("Processing complete!")
