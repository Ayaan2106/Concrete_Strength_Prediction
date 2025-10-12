from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import os

# path to trained model
MODEL_PATH = "concrete_model.pkl"

# try to load model at startup
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
else:
    model = None

# create app
app = FastAPI(
    title="Concrete Strength Prediction API",
    description="Predict concrete strength using a trained model",
    version="1.0"
)

# input data
class ConcreteInput(BaseModel):
    cement: float
    slag: float
    ash: float
    water: float
    superplastisizer: float
    coarse_agg: float
    fine_agg: float
    age: float

@app.get("/")
def home():
    """Check if the model is loaded."""
    return {
        "message": "Welcome to the Concrete Strength Prediction API!",
        "model_loaded": model is not None
    }

@app.post("/predict")
def predict_strength(data: ConcreteInput):
    """Return predicted concrete strength."""
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded! Please ensure concrete_model.pkl is in the same folder.")

    # convert input to array
    features = np.array([[ 
        data.cement,
        data.slag,
        data.ash,
        data.water,
        data.superplastisizer,
        data.coarse_agg,
        data.fine_agg,
        data.age
    ]])

    try:
        prediction = model.predict(features)
        return {"predicted_strength": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
