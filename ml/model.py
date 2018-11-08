import tensorflow as tf
import numpy as np

class Model:
    def __init__(self, path_to_model, path_to_weights):
        self.model = self._load_model(path_to_model, path_to_weights)
    
    def _load_model(self, path_to_model, path_to_weights):
        json_file = open(path_to_model, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = tf.keras.models.model_from_json(loaded_model_json)
        loaded_model.load_weights(path_to_weights)

        loaded_model.compile(loss='mean_squared_error', optimizer='adam')
        return loaded_model

    def _preprocess(self, array):
        input_data = np.asarray(array).transpose()
        return np.asarray([input_data])

    def _postprocess(self, prediction):
        result = []
        result.append(int(prediction[0][0]))
        result.append(int(prediction[0][1]))
        return result


    def predict(self, data):
        input_data = self._preprocess(data)
        prediction = self.model.predict(input_data)
        result = self._postprocess(prediction)
        return result

