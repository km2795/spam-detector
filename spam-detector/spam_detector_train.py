import keras as keras

# Train the model, return the model after training is complete.
# Hyperparameters may change later (set arbitrarily).
def train_model(input_size, train_data_input, train_data_output, model_store_directory):
  # Initialize a model.
  model = keras.models.Sequential()

  # First hidden layer with input parameters.
  model.add(keras.layers.Dense(300, input_dim=input_size, activation="relu"))

  # Second hidden layer.
  model.add(keras.layers.Dense(100, activation="relu"))

  # Output layer.
  model.add(keras.layers.Dense(1, activation="sigmoid"))

  # Compile the model.
  model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

  # Start training.
  model.fit(train_data_input, train_data_output, epochs=10, batch_size=10)

  # Save the model.
  keras.models.save_model(model, model_store_directory)

  return model
