Concrete Strength Prediction API
-A simple FastAPI app that predicts the compressive strength of concrete using a trained machine learning model.

How It Works ?
-You enter values like cement, water, and age.
-The API uses a saved model (concrete_model.pkl) to predict concrete strength in MPa.
-You can test it easily using FastAPI’s built-in interface.
🛠️ Setup

Clone the repo first
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

(Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Add your trained model
Make sure your file concrete_model.pkl is in the same folder as main.py.

Run the main.py
Then open this link in your browser:
http://127.0.0.1:8000/docs
