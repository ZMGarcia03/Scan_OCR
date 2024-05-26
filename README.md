# Scan_OCR

# OCR (Optical Character Recognition) Document Scanning

This project includes implementations in Python and Java to scan a printed document and generate OCR (Optical Character Recognition) text from the scanned image.

## Python Implementation (scan_ocr.py)

- **File Extension:** `.py`
- **Dependencies:**
  - `pytesseract`
  - `Pillow`
  - `opencv-python`

- **Usage:**
  1. Install the required Python libraries:
     ```sh
     pip install pytesseract Pillow opencv-python
     ```
  2. Ensure Tesseract OCR is installed on your system and its path is added to the environment variables.
  3. Save the `scan_ocr.py` script to your computer.
  4. Run the script:
     ```sh
     python scan_ocr.py
     ```
  5. Enter the path to the image file when prompted.
  6. The script will process the image and output the OCR text.

## Java Implementation (ScanOCR.java)

- **File Extension:** `.java`
- **Dependencies:**
  - Tess4J (a Java JNA wrapper for Tesseract OCR API)

- **Usage:**
  1. Download and add Tess4J library to your project.
  2. Ensure Tesseract OCR is installed on your system and its `tessdata` folder is correctly set in the code.
  3. Save the `ScanOCR.java` file to your computer.
  4. Compile the Java file:
     ```sh
     javac -cp .;path\to\tess4j.jar ScanOCR.java
     ```
  5. Run the compiled class:
     ```sh
     java -cp .;path\to\tess4j.jar ScanOCR
     ```
  6. Enter the path to the image file when prompted.
  7. The program will process the image and output the OCR text.


>[!IMPORTANT]
>This project is protected under [MIT License](LICENSE).
