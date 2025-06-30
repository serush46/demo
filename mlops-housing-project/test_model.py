import joblib
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error

# Load the saved model
model = joblib.load('model.pkl')

# Load dataset for testing
boston = load_boston()
X_test, y_test = boston.data, boston.target

# Test the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Test Mean Squared Error: {mse}")

# Assert that the MSE is below a threshold (we expect this for a good model)
assert mse < 25, f"MSE {mse} is too high"
