from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")  # ✅ Correct filename

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = float(request.form["age"])
    exp = float(request.form["experience"])
    #prediction = model.predict(np.array([[age, exp]]))  # Uncomment this
    prediction = 111
    return render_template("index.html", prediction_text=f"Predicted Salary: ${prediction:.2f}")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
