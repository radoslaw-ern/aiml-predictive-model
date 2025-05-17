import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_CPP_MIN_VLOG_LEVEL'] = '3'
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

import absl.logging
absl.logging.set_verbosity(0)
absl.logging.set_stderrthreshold(0)

import logging
logging.basicConfig(level=logging.CRITICAL)
logging.getLogger("keras").setLevel(logging.CRITICAL)
logging.getLogger("keras").addHandler(logging.NullHandler(logging.CRITICAL))

import keras
keras.config.disable_interactive_logging()




import json
import pandas as pd;
import readFile
from sklearn.model_selection import train_test_split



# Read the configuration file
with open('./config.json') as config_file:
  config = json.load(config_file)

# Read the training data from the .csv file
dataframe = readFile.read_csv_from_server("trainingData.csv")

x = dataframe.drop(columns = config.get("columns_to_drop"))
y = dataframe[config.get("column_to_predict")]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = config.get("test_size"), random_state = config.get("random_state"))

model = keras.models.Sequential()
model.add(keras.layers.Dense(units = 64, activation = "sigmoid", input_shape = x_train.shape))
model.add(keras.layers.Dense(units = 64, activation = "sigmoid"))
model.add(keras.layers.Dense(units = 64, activation = "sigmoid"))

data = {
  "propability": 0.33
}

# print(json.dumps(data))