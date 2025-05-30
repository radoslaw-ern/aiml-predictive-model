# Predictive Model for Tumor Type Classification

This solution is designed to run on a Linux server.\
It is based on distributed architecture. It contains 3 modules:
- AI Model
- Backend
- Frontend
Use ```undiagnosed.csv``` in the main directory to check the prediction for the tumor to be non-macancerous.

## AI Model

## Installation

The Python scripts require libraries sklearn and Keras. To install them, run the commands below:\
```pip install python-dotenv```\
```pip install sklearn```

### Training

To train the Model, upload the training spreadsheet (```training_data.scv```) to:\
```backend\upload```\
Apply the config parameters in:\
```ai_model\config.json```
Set the Backend endpoint in the ```.env``` file.\
Run the training script:\
```python trainer.py```

# Backend module

## Installation

To install the Node-red, run the command below:\
```sudo npm i -g node-red```\
```cd backend```\
```npm i```

## Running

To run the Backend module, run the command below. Change the port if needed: 
```npx http-server -p 2882 & node-red --userDir ./ --port 2881```

## Frontend module

### Installation

This application requires:\
```NodeJS version 22.14.0```

Install dependencies by running the commands below:\
```cd frontend```\
```npm i```

Set the correct Backend endpoints in:\
```frontent\src\environments```

### Running in the development mode

To run the application in Development mode, run the command below:\
```npm run start```

### Building for production

To build the application for Production mode, run the command below:\
```npm run build```