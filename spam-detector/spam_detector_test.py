import keras as keras
from sklearn.metrics import mean_squared_error

# Calculate the mean squared error of the model.
def calculate_mse(predictions, test_data_output):
  return mean_squared_error(test_data_output, predictions)

# Load the model disk and test on the data provided.
# Return the mean error.
def test_model(test_data_input, test_data_output, model_store_dir):

  # Load the model from disk.
  model = keras.models.load_model(model_store_dir)

  # Test the model.
  predictions = model.predict(test_data_input)

  # Return the mean squared error.
  return calculate_mse(predictions, test_data_output)

