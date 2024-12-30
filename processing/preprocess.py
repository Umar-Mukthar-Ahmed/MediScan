import cv2
import os

def preprocess_image(input_path, output_path, size=(224, 224)):
    # Load the image
    image = cv2.imread(input_path)
    if image is None:
        print(f"Error: Unable to load image {input_path}")
        return
    
    # Resize the image
    resized = cv2.resize(image, size)
    
    # Normalize the image
    normalized = resized / 255.0
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(normalized, (5, 5), 0)
    
    # Save the processed image
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, os.path.basename(input_path))
    cv2.imwrite(output_file, (blurred * 255).astype('uint8'))
    print(f"Processed image saved at: {output_file}")
