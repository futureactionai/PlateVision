from studio.custom_block import *
import cv2
import numpy as np
import pytesseract
from datetime import datetime

class PlateReader_PyTesseract(Block):
    op_code = 'PlateReader_PyTesseract'
    tooltip = 'Detect license plates using pytesseract'

    def init(self):
        self.width = 350
        self.height = 300

        self.input_sockets = [SocketTypes.ImageAny('Input Image')]
        self.output_sockets = [
            SocketTypes.ImageAny('Output Image'),
            SocketTypes.String('Detected Texts'),
            SocketTypes.String('Log Message')
        ]

        self.param['label'] = Label(text='PyTesseract License Plate Reader', tooltip='OCR-based plate reading')

    def run(self):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        img = self.input['Input Image'].data
        if img is None or not isinstance(img, np.ndarray):
            self.logError(f"Geçersiz görüntü: {type(img)}")
            return

        try:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        except Exception as e:
            self.logError(f"cv2.cvtColor hatası: {e}")
            return

        try:
            custom_config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
            data = pytesseract.image_to_data(img_rgb, output_type=pytesseract.Output.DICT, config=custom_config)
        except Exception as e:
            self.logError(f"OCR okuma hatası: {e}")
            return

        detected_texts = []
        boxes = []

        for i in range(len(data['text'])):
            text = data['text'][i]
            if text.strip() != '':
                x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                detected_texts.append(text)
                boxes.append([(x, y), (x + w, y), (x + w, y + h), (x, y + h)])

        plate_text = "".join(detected_texts)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"Plaka '{plate_text}' ({timestamp}) Excel'e kaydedildi."

        self.logInfo(f"Algılanan metinler: {detected_texts}")
        self.logInfo(log_message)

        self.output['Output Image'].data = img
        self.output['Detected Texts'].data = plate_text
        self.output['Log Message'].data = log_message 

add_block(PlateReader_PyTesseract.op_code, PlateReader_PyTesseract)

