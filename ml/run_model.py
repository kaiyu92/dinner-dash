import tensorflow as tf
import numpy as np

json_file = open('../data/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = tf.keras.models.model_from_json(loaded_model_json)
loaded_model.load_weights("../data/model.h5")

tf.keras.utils.plot_model(loaded_model, to_file='model.png', show_shapes=True, show_layer_names=True)

loaded_model.compile(loss='mean_squared_error', optimizer='adam')


"""Predict"""

test = np.asarray([1, 1, 1]).transpose()
test = np.asarray([test])
#print(X[:1])
prediction = loaded_model.predict(test)

y_0 = prediction[0]
#print('Prediction with scaling - {}'.format(y_0))
#y_0 -= added
#y_0 /= multiplied_by
print("Dinner Prediction  - {}".format(y_0))

#Y_0 = Y[0]
#print('Ground truth with scaling - {}'.format(Y_0))
#Y_0 -= added
#Y_0 /= multiplied_by

#print('Ground Truth Dinner peeps - {}'.format(Y_0))
