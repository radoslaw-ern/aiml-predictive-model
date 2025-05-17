import os
import json
import types

config_file_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(config_file_path) as config_file:
  config = json.load(config_file)

config = types.SimpleNamespace(**config)