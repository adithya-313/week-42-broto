from fastapi import FastAPI
from metrics import api_counter , prediction_counter
import joblib
from prometheus_client import generate_latest
from fastapi.responses import Response

app = FastAPI()

model = joblib.load('models/model.joblib')

@app.post('/predict')
def predict(features:list):
    
    api_counter.inc()

    prediction_counter.inc()

    prediction = model.predict(features)

    return {"prediction" : int(prediction[0])}


@app.get('/metrics')
def metrics():
    return Response(
        generate_latest(),
        media_type='text/plain'
    )
