from keras.models import load_model
from keras.preprocessing import image
import numpy as np

class Prediction():
    def __init__(self, image_file, plant):
        
        self.classes = plant.get("categories")

        self.cnn = load_model(f'model/{plant.get("model_name")}')
        self.image_size = tuple((64, 64))
        self.image_pred = image_file

    def read_image(self):
        test_image = image.load_img(f'{self.image_pred}', target_size = self.image_size)
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        test_image /= 255
        return test_image

    def test_single_image(self):
        images = self.read_image()
        result = self.cnn.predict(images)
        return self.format_prediction(result)

    def format_prediction(self, result):
        # result = self.test_single_image()
        result_indice = np.argmax(result[0])
        prediction = self.classes[result_indice]
        prediction_percentage = max(result[0]) * 100
        return prediction, "{:.2f}%".format(prediction_percentage)
        print("Predict = {} - {:.2f}%\n".format(prediction, prediction_percentage))
    

    pass