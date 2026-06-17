from fastapi import FastAPI
from pydantic import BaseModel
from metrics import prediction_counter , api_counter
import joblib
from fastapi.responses import Response
from prometheus_client import generate_latest

app =  FastAPI()

model = joblib.load('models/model.joblib')

class PredictionInput(BaseModel):
    features: list[list[float]]

@app.post("/predict")
def predict(data: PredictionInput):

    api_counter.inc()

    prediction_counter.inc()

    prediction = model.predict(data.features)

    return {'prediciton' : int(prediction[0])}

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type='text/plain'
    )
