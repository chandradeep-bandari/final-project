import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def load_data():
    filename = "salary_data.csv"
    try:
        data = pd.read_csv(filename)
    except FileNotFoundError:
        # Try alternative paths
        filename = "salary_data.csv"
        data = pd.read_csv(filename)
    
    X = data[["age", "experience"]]
    y = data["salary"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train, model_path="model.pkl"):
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse


# If you want to run training directly, use this:
if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)
    mse = evaluate_model(model, X_test, y_test)
    print(f"Model trained. MSE on test data: {mse:.2f}")
