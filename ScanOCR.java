import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;

import java.io.File;

public class ScanOCR {
    public static void main(String[] args) {
        Tesseract tesseract = new Tesseract();
        tesseract.setDatapath("tessdata"); // Set the tessdata path

        try {
            System.out.println("Enter the path to the image file: ");
            Scanner scanner = new Scanner(System.in);
            String imagePath = scanner.nextLine();
            
            File imageFile = new File(imagePath);
            String result = tesseract.doOCR(imageFile);
            System.out.println("OCR Text:");
            System.out.println(result);
        } catch (TesseractException e) {
            e.printStackTrace();
        }
    }
}
