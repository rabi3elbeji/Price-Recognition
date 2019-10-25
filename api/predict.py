import configparser
import cv2


from utils.price_box_detection import *
from utils.ocr_prediction import *

# -------------------
# FUNCTIONS
# -------------------
def expand_image(img):
    return np.expand_dims(img, axis=0)

# preprocess frame
def preprocess_frame(frame):
    preprocessed_img = expand_image(frame)
    payload = {"instances": preprocessed_img.tolist()}
    return frame, preprocessed_img, payload


# ------------------
# CONFIGURATION
# ------------------

# config
_CONFIG_FILE = "config.ini"

# init parser
config = configparser.ConfigParser()

# road config
config.read(_CONFIG_FILE)

# url
_TF_SERVING_URL = config["Tensorflow"]["tf_serving_url"]

# ------------------
# Image FEED URL
# ------------------

_DETECTION_SOURCE = config["General"]["detection_source"]


# -------------------
# Process
# -------------------

frame = cv2.imread(
    _DETECTION_SOURCE
)

_HEIGHT, _WIDTH, _ = frame.shape

# preprocess frame
frame, img_processed, payload = preprocess_frame(frame)

# image width and height
y = np.size(frame, 0)
x = np.size(frame, 1)

predictPriceBBox = PredictPriceBBox(_TF_SERVING_URL)
ocr = OCR()

xmin, ymin, xmax, ymax = predictPriceBBox.process(payload, x, y)
crop = frame[ymin:ymax,xmin:xmax]


text = ocr.process(crop)

print(text)

cv2.rectangle(frame,(xmin,ymin),(xmax,ymax),(0,0,255),10)
cv2.putText(frame,text, (xmax+10,ymin+int((ymax-ymin)/2)), cv2.FONT_HERSHEY_SIMPLEX, 4, (0,0,255), 5)

cv2.imwrite("detected-boxes.jpg", frame)
