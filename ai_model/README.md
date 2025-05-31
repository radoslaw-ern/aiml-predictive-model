# AI Model

## Installation

The Python scripts require libraries sklearn and Keras. To install them, run the commands below:\
```pip install python-dotenv```\
```pip install sklearn```

## Training

To train the Model, upload the training spreadsheet (```training_data.scv```) to:\
```backend\upload```\
Apply the config parameters in:\
```ai_model\config.json```
Set the Backend endpoint in the ```.env``` file.\
Run the training script:\
```python trainer.py```

## Prediction

To run the predicting script, upload the spreadsheet ```uploaded_spreadsheet.csv``` to\
```backend\upload```\
Run the predicting script\
```python predictor.py```