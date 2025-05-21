from config import config
import read_file
from sklearn.model_selection import train_test_split
import keras

dataframe = read_file.read_csv_from_server("trainingData.csv")

x = dataframe.drop(columns = config.columns_to_drop)
y = dataframe[config.column_to_predict]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = config.test_size, random_state = config.random_state)

model = keras.models.Sequential()
model.add(keras.Input(shape = x_train.shape[1:]))
model.add(keras.layers.Dense(units = 128, activation = "sigmoid"))
model.add(keras.layers.Dense(units = 64, activation = "sigmoid"))
model.add(keras.layers.Dense(units = 1, activation = "sigmoid"))

model.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])
model.fit(x_train, y_train, epochs = 512)
model.evaluate(x_test, y_test)

model.save("model.keras")
