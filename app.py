from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = float(request.form["age"])
    exp = float(request.form["experience"])
    prediction = model.predict(np.array([[age, exp]]))
    prediction_value = float(prediction[0])  # ✅ extract scalar

    return render_template("index.html", prediction_text=f"Predicted Salary: ${prediction_value:.2f}")  # ✅ fix

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

