# Concrete Strength Prediction API (FastAPI)

A lightweight REST API that serves a trained model to predict **compressive strength of concrete (MPa)** from mix components and age.

> Uses the trained **XGBoost** model from the main branch  
> **R² = 0.93 | MAE = 2.72**

---

## 🚀 What this API provides
- `GET /` — Health check (confirms the model is loaded)
- `POST /predict` — Predicts compressive strength (MPa) from input features
- Interactive API docs at `/docs` (Swagger) and `/redoc`

---

## 📂 Repository Structure
.
├── main.py # FastAPI app (app = FastAPI(...))
├── concrete_model.pkl # Trained model artifact (place in repo root)
├── requirements.txt
└── README.md

yaml
Copy code

> **Note:** The app expects the model file at `./concrete_model.pkl`.  
> If it’s missing, predictions will return an informative `500` error.

---

## ⚙️ Setup & Run
```bash
# Clone and switch to the FastAPI branch
git clone https://github.com/Ayaan2106/Concrete_Strength_Prediction.git
cd Concrete_Strength_Prediction
git checkout fastapi

# Create and activate environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make sure the trained model exists in the project root
# (Copy it from the main branch if needed)
#   ./src/models/concrete_model.pkl  ->  ./concrete_model.pkl

# Run the API
uvicorn main:app --reload
# Visit:
#   http://127.0.0.1:8000/       (health)
#   http://127.0.0.1:8000/docs   (Swagger)
#   http://127.0.0.1:8000/redoc  (ReDoc)
🔌 API Endpoints
Health
sql
Copy code
GET /
Example response

json
Copy code
{
  "message": "Welcome to the Concrete Strength Prediction API!",
  "model_loaded": true
}
Predict
bash
Copy code
POST /predict
Content-Type: application/json
Request body

json
Copy code
{
  "cement": 540.0,
  "slag": 0.0,
  "ash": 0.0,
  "water": 162.0,
  "superplastisizer": 2.5,
  "coarse_agg": 1040.0,
  "fine_agg": 676.0,
  "age": 28.0
}
Response

json
Copy code
{
  "predicted_strength": 64.73
}
curl example

bash
Copy code
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"cement":540,"slag":0,"ash":0,"water":162,"superplastisizer":2.5,"coarse_agg":1040,"fine_agg":676,"age":28}'
Python example

python
Copy code
import requests

payload = {
    "cement": 540.0,
    "slag": 0.0,
    "ash": 0.0,
    "water": 162.0,
    "superplastisizer": 2.5,
    "coarse_agg": 1040.0,
    "fine_agg": 676.0,
    "age": 28.0
}
res = requests.post("http://127.0.0.1:8000/predict", json=payload)
print(res.json())


Output: predicted_strength in MPa.
