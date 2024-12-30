import cv2
import os

def segment_image(input_path, output_path):
    # Load the preprocessed image
    image = cv2.imread(input_path)
    if image is None:
        print(f"Error: Unable to load image {input_path}")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply binary thresholding
    _, segmented = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    
    # Save the segmented image
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, os.path.basename(input_path))
    cv2.imwrite(output_file, segmented)
    print(f"Segmented image saved at: {output_file}")
