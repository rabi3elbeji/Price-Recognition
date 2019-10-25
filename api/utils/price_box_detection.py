import numpy as np
import requests

class PredictPriceBBox(object):
    """docstring for PredictPriceBBox."""

    def __init__(self, tf_serving_url):
        super(PredictPriceBBox, self).__init__()
        self.tf_serving_url = tf_serving_url

    def process(self, input, x, y):
        """
        process input data
        """
        # post to model  server the input image and get prediction
        res = requests.post(
            self.tf_serving_url,
            json=input
        )

        # extract prediction from json outputs
        output_dict = res.json()["predictions"][0]
        detection_boxes = np.array(output_dict['detection_boxes'])
        detection_classes = np.array(output_dict['detection_classes'], dtype="uint8")
        detection_scores = output_dict['detection_scores']

        # compute bbox coordinations
        ymin = int(detection_boxes[0][0]*y)
        xmin = int(detection_boxes[0][1]*x)
        ymax = int(detection_boxes[0][2]*y)
        xmax = int(detection_boxes[0][3]*x)

        return xmin, ymin, xmax, ymax
