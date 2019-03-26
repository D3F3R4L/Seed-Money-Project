from keras.models import load_model
from keras.models import model_from_json
import json
import pandas as pd
import numpy as np


def NeuralNetwork():
    df = pd.read_csv('/home/pi/data.csv')
    X = df.iloc[:, 1:6].values
    y= df.iloc[:,6].values

    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("Prediction.h5")

    # evaluate loaded model on test data
    loaded_model.compile(loss='mse', optimizer='adam', metrics=['mse'])
    results = loaded_model.predict(np.array(X))
    score= loaded_model.evaluate(X,y,verbose=0)
    print("{}: {}".format(loaded_model.metrics_names[1], score[1]))
    print('Prediction finished')
    return results,y

