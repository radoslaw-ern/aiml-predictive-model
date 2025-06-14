from config import config
import read_file
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import keras

dataframe = read_file.read_csv_from_server("training_data.csv")

x = dataframe.drop(columns = config.columns_to_drop)
y = dataframe[config.column_to_predict]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = config.test_size, random_state = config.random_state)

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = keras.models.Sequential()
model.add(keras.Input(shape = x_train.shape[1:]))
model.add(keras.layers.Dense(units = 32, activation = "relu", kernel_regularizer = keras.regularizers.l1(0.1)))
model.add(keras.layers.Dropout(0.05))
model.add(keras.layers.Dense(units = 16, activation = "relu", kernel_regularizer = keras.regularizers.l1(0.1)))
model.add(keras.layers.Dropout(0.05))
model.add(keras.layers.Dense(units = 1, activation = "sigmoid"))

model.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])

early_stop = keras.callbacks.EarlyStopping(patience = config.early_stop_patience, monitor="accuracy", restore_best_weights = True)
model.fit(x_train, y_train, epochs = 512, callbacks = [early_stop])
model.evaluate(x_test, y_test)

model.save("model.keras")
