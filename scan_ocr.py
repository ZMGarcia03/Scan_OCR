import pytesseract
from PIL import Image
import cv2

def scan_and_ocr(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply some preprocessing to improve OCR accuracy
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    # Save the processed image temporarily
    processed_image_path = "temp_processed_image.png"
    cv2.imwrite(processed_image_path, gray)
    
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(Image.open(processed_image_path))
    
    # Remove the temporary file
    import os
    os.remove(processed_image_path)
    
    return text

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")
    ocr_text = scan_and_ocr(image_path)
    print("OCR Text:")
    print(ocr_text)
