import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("salary_data.csv")
X = data[["age", "experience"]]
y = data["salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# ✅ Correct way to save the model (use .pkl extension)
joblib.dump(model, "model.pkl") 
