import os

# Turn off information log.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

import word_processor as wp
import keras as keras
import argparse

from decouple import config
from sklearn.feature_extraction.text import HashingVectorizer

# Load configurations.
MAIN_DIR = config("MAIN_DIR")
MODEL_DUMP_DIRECTORY = MAIN_DIR + config("MODEL_DUMP_DIRECTORY")

# Main function.
def main():
  # Parse command-line arguments
  parser = argparse.ArgumentParser(description="SPAM DETECTOR")

  # For the number of files to process.
  parser.add_argument("--data_size", type=int, required=True, help="Number of spam data files")

  # Location of the file(s) to process.
  parser.add_argument("--files", nargs='+', required=True, help="List of paths to spam data files")

  # Parse.
  args = parser.parse_args()

  # Load the model peripherals.
  vectorizer = HashingVectorizer(n_features=200)
  vectorized_data = []

  # Read the spam data from file --> vectorize it --> load in array.
  for spam_train in range(args.data_size):
    with open(args.files[spam_train], "rt", encoding="ISO-8859-1") as fh:
      text = ""
      for row in fh:
        # Process the data.
        text += wp.process_word(False, True, row, "\n")

      # Encode the data.
      vectorized_data = vectorizer.transform([text]).toarray()
      print(run_model(vectorized_data, MODEL_DUMP_DIRECTORY))
      
# Load the model disk and return the output.
def run_model(input_data, model_store_dir):

  # Load the model from disk and return the result.
  result = keras.models.load_model(model_store_dir).predict(input_data)[0][0]
  
  # Return the verdict on the input.
  if (result > 0.8):
    return "Spam"
  elif (result < 0.4):
    return "Not Spam"

  # Its somewhere in between.
  else:
    return "Somewhat Spam"

# __GO__
main()