from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def character_recognise(img: Image) -> str:
    return ocr_tesseract(img)


def ocr_tesseract(img: Image) -> str:

    ocr_string = ''
    try:
        ocr_string = pytesseract.image_to_string(img, timeout=5)

        return ocr_string
    except RuntimeError:
        return "The given image is either not supported or is unreadable in nature."
