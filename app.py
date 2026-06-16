import joblib
from fastapi import FastAPI
from metrics import prediction_counter, api_requests
from fastapi.responses import Response  
from prometheus_client import generate_latest

app = FastAPI()

model = joblib.load('models/model.joblib')

@app.post('predict/')
def predict(features : list):
    api_counter.inc()

    prediction_counter.inc()

    prediction = model.predict(features)

    return {
        "prediction" : int(prediction[0])
    }


@app.get('metrics/')
def metrics():
    return Response(
        generate_latest(),
        media_type='text/plain'
    )
