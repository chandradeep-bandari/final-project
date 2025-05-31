import pytest
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from model import load_data, train_model, evaluate_model
import joblib

@pytest.fixture(scope='module')
def setup_dummy_data():
    # Create a dummy salary_data.csv to simulate your dataset
    data = {
        'age': [25, 30, 35, 40, 45],
        'experience': [1, 3, 5, 7, 9],
        'salary': [30000, 35000, 40000, 45000, 50000]  # Your target variable
    }
    df = pd.DataFrame(data)
    df.to_csv('salary_data.csv', index=False)
    yield
    os.remove('salary_data.csv')

def test_load_data(setup_dummy_data):
    X_train, X_test, y_train, y_test = load_data()
    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(y_train) > 0
    assert len(y_test) > 0
    # Check if the features have correct columns
    assert all(col in X_train.columns for col in ['age', 'experience'])
    assert isinstance(y_train, pd.Series)

def test_train_model(setup_dummy_data):
    X_train, _, y_train, _ = load_data()
    model = train_model(X_train, y_train, model_path='test_model.joblib')
    assert isinstance(model, LinearRegression)
    assert os.path.exists('test_model.joblib')
    loaded_model = joblib.load('test_model.joblib')
    assert isinstance(loaded_model, LinearRegression)
    os.remove('test_model.joblib')

def test_evaluate_model(setup_dummy_data):
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train, model_path='test_model_eval.joblib')
    mse = evaluate_model(model, X_test, y_test)
    assert isinstance(mse, float)
    assert mse >= 0
    os.remove('test_model_eval.joblib')
