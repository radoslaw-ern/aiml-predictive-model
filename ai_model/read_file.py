from config import config
import os
from dotenv import load_dotenv
import requests
import json
import pandas as pd

load_dotenv()

apiEndpoint = os.getenv("APP_UPLOAD_URL")

def handle_error(error_string):
  error = {
    "error": error_string
  }
  print(json.dumps(error))

  exit()

def read_csv_from_server(file_name):
  file_path = apiEndpoint + "/" + file_name

  try:
    response = requests.head(file_path)

    if response.status_code == 200:
      dataframe = pd.read_csv(filepath_or_buffer = file_path, delimiter = config.csv_delimiter)

      return dataframe
    
    else:
      handle_error(f"The file {file_name} does not exist.")
    
  except FileNotFoundError as exception:
    handle_error(f"Error: {exception}")

  except Exception as exception:
    handle_error(f"Error: {exception}")



