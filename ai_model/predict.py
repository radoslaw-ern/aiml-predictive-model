import keras
import os
import sys
from contextlib import contextmanager
import json
import read_file

@contextmanager
def suppress_stdout():
  with open(os.devnull, "w") as devnull:
    old_stdout = sys.stdout
    sys.stdout = devnull
    try:  
      yield
    finally:
      sys.stdout = old_stdout

path_to_model = os.path.join(os.path.dirname(__file__), "model.keras")
model = keras.models.load_model(path_to_model)

test_input = read_file.read_csv_from_server("uploaded_spreadsheet.csv")

with suppress_stdout():
  prediction = model.predict(test_input).item()

output = {
  "prediction": prediction
}

print(json.dumps(output), end = "")