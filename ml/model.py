import tensorflow as tf
import numpy as np

class Model:
    def __init__(self, path_to_model, path_to_weights):
        self.model = self._load_model(path_to_model, path_to_weights)
    
    def _load_model(self, path_to_model, path_to_weights):
        json_file = open('data/model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = tf.keras.models.model_from_json(loaded_model_json)
        loaded_model.load_weights("model.h5")

        loaded_model.compile(loss='mean_squared_error', optimizer='adam')
        return loaded_model

    def _preprocess(self, array):
        input_data = np.asarray(array).transpose()
        return np.asarray([input_data])

    def predict(self, data):
        input_data = self._preprocess(data)
        prediction = self.model.predict(input_data)

        return prediction[0]

