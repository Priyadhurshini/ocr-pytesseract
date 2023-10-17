import pytesseract as pyt
import cv2

img = cv2.imread("ocr_ex2.png")

pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

text = pyt.image_to_string(img)

print(text)