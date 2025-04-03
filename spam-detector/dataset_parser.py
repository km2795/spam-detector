import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer
from decouple import config

import word_processor as wp
import dataset_handler as ds_handler


MAIN_DIR = config("MAIN_DIR")


# Load the file data and prepare for vectorization,
# finally organize the dataset into training and test set.
def process_dataset():

  """

  Dataset info.

  """

  spam_data, not_spam_data = ds_handler.get_dataset_map().values()
  vectorized_spam_data, vectorized_not_spam_data = [], []

  spam_data_size = len(spam_data)
  not_spam_data_size = len(not_spam_data)

  # Split the train and test in 70:30 ratio.
  spam_train_size = int(0.7 * len(spam_data))
  spam_test_size = spam_data_size - spam_train_size

  not_spam_train_size = int(0.7 * len(not_spam_data))
  not_spam_test_size = not_spam_data_size - not_spam_train_size

  """

  Read each file and vectorize the content, finally stuff the vectors inside arrays.

  """

  # Hashing Vectorizer; 'feature size' may change later (set arbitrarily).
  vectorizer = HashingVectorizer(n_features=200)

  # Read the spam data from file --> vectorize it --> load in array.
  for spam_train in range(spam_data_size):
    with open(spam_data[spam_train], "rt", encoding="ISO-8859-1") as fh:
      text = ""
      for row in fh:
        # Process the data.
        text += wp.process_word(False, True, row, "\n")

      # Encode the data.
      vectorized_spam_data.append(np.append(vectorizer.transform([text]).toarray(), [1]))

  # Read the not spam data from file --> vectorize it --> load in array.
  for not_spam_train in range(not_spam_data_size):
    with open(not_spam_data[not_spam_train], "rt", encoding="ISO-8859-1") as fh:
      text = ""
      for row in fh:
        # Process the data.
        text += wp.process_word(False, True, row, "\n")

      # Encode the data.
      vectorized_not_spam_data.append(np.append(vectorizer.transform([text]).toarray(), [0]))

  # Merge the two vector set.
  vectorized_spam_data.extend(vectorized_not_spam_data)

  # Save the dataset in a file, for easier separation (fix this later).
  np.savetxt(MAIN_DIR + "/spam-detector/vectorized_dataset.csv", vectorized_spam_data, delimiter=",")

  # Load the dataset for separation.
  dataset = np.loadtxt(MAIN_DIR + "/spam-detector/vectorized_dataset.csv", delimiter=",")


  """

  Separate the training and test data.

  """
  # Spam train and test set.
  spam_set = dataset[0:(spam_data_size)]
  spam_train_set = spam_set[0:spam_train_size]
  spam_test_set = spam_set[-spam_test_size:]

  # Not spam train and test set.
  not_spam_set = dataset[(spam_data_size):]
  not_spam_train_set = not_spam_set[0:not_spam_train_size]
  not_spam_test_set = not_spam_set[-not_spam_test_size:]

  # Concatenate the spam and not spam into training set.
  train_set = np.concatenate((spam_train_set, not_spam_train_set))
  train_set_input = train_set[:, 0:(train_set.shape[1] - 1)]
  train_set_output = train_set[:, (train_set.shape[1] - 1)]

  # Concatenate the spam and not spam into test set.
  test_set = np.concatenate((spam_test_set, not_spam_test_set))
  test_set_input = test_set[:, 0:(test_set.shape[1] - 1)]
  test_set_output = test_set[:, (test_set.shape[1] - 1)]

  return train_set_input, train_set_output, test_set_input, test_set_output
