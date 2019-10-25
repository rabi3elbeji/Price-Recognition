import pytesseract

class OCR(object):
    """docstring for OCR."""

    def __init__(self):
        super(OCR, self).__init__()
        pytesseract.pytesseract.tesseract_cmd = 'tesseract'

    def process(self, input_image):
        text = pytesseract.image_to_string(input_image, lang="eng", config='--psm 6 -c tessedit_char_whitelist=0123456789')
        return text
