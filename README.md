# Concrete Strength Prediction Model

A machine learning project that predicts the **compressive strength of concrete (MPa)** based on its mix components and age.  
The model is trained and evaluated using **XGBoost**, **k-Nearest Neighbour**, and **Random Forest** algorithms.

> **Best Model:** XGBoost  
> **R² = 0.93 | MAE = 2.72**

---

## 🚀 Features
- Predict compressive strength of concrete using pre-trained models  
- Visualize results using **Matplotlib** and **Seaborn**  
- Evaluate models with metrics such as **R²**, **MAE**, and **RMSE**  
- Display tabular results using **Tabulate**  
- Simple reproducibility with `requirements.txt`

---

## 📂 Repository Structure
.
├── Concrete_Data.csv
├── Recognition of Concrete Code - Final.ipynb # Main notebook
├── requirements.txt
└── README.md

---

## ⚙️ Setup & Usage
```bash
# Clone the repository
git clone https://github.com/Ayaan2106/Concrete_Strength_Prediction.git
cd Concrete_Strength_Prediction

# Create and activate environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Open and run the notebook
jupyter notebook "Recognition of Concrete Code - Final.ipynb"
📊 Input Features
Feature	Description
cement	Cement content (kg/m³)
slag	Blast furnace slag (kg/m³)
ash	Fly ash (kg/m³)
water	Water content (kg/m³)
superplastisizer	Superplasticizer amount (kg/m³)
coarse_agg	Coarse aggregate (kg/m³)
fine_agg	Fine aggregate (kg/m³)
age	Age of concrete (days)

Output: Compressive Strength (MPa)

📈 Results Summary
•XGBoost achieved the highest accuracy (93%)
Visualisations include:
•Parity plots
•Residual plots
•Feature importance charts

🧰 Tech Stack
•Python 3.10+
•Pandas, Numpy, scikit-learn, XGBoost, matplotlib, seaborn, tabulate
