Concrete Strength Prediction API

A simple FastAPI app that predicts the compressive strength of concrete using a trained machine learning model.

How It Works

Enter input values such as cement, water, and age.

The API uses a saved model (concrete_model.pkl) to predict the concrete strength in MPa.

You can test it easily using FastAPI’s built-in interactive interface.

Setup 🛠️

Clone the repository

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

(Optional) Create a virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt

Add your trained model
Make sure the file concrete_model.pkl is in the same folder as main.py.

Run the API

python main.py


Open the FastAPI docs in your browser
http://127.0.0.1:8000/docs

You can now interact with the API and test predictions easily.
