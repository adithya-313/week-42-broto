from fastapi import FastAPI
from fastapi.responses import Response
from prometheus_client import generate_latest
from metrics import prediction_counter, api_requests
import joblib
from pydantic import BaseModel


app = FastAPI()

# Load trained model
model = joblib.load("models/model.pkl")

class Features(BaseModel):
    features: list

    
@app.get("/")
def home():

    api_requests.inc()

    return {
        "status": "running"
    }



from pydantic import BaseModel

class Features(BaseModel):
    features: list


@app.post("/predict")
def predict(data: Features):

    api_requests.inc()
    prediction_counter.inc()

    prediction = model.predict([data.features])

    return {
        "prediction": int(prediction[0])
    }


@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type="text/plain"
    )