from decouple import config

import dataset_parser as dataset_parser
import spam_detector_train as sd_train
import spam_detector_test as sd_test

MAIN_DIR = config("MAIN_DIR")

# Model storage directory.
MODEL_DUMP_DIRECTORY = MAIN_DIR + "/spam-detector/spam_detector_model_dump_dir"


print("Preparing dataset...\n\n")

# Prepare the dataset.
( train_set_input,
  train_set_output,
  test_set_input,
  test_set_output ) = dataset_parser.process_dataset()

# Input layer size for the sequential model.
model_input_size = len(train_set_input[0])


print("\n\nTraining model...\n\n")

# Train the model.
model_accuracy = sd_train.train_model(model_input_size, train_set_input,
  train_set_output, test_set_input, test_set_output, MODEL_DUMP_DIRECTORY)

print("\n\nTesting model...\n\n")

# How the model performed.
print("\n\nModel Accuracy: ", model_accuracy, "\n\n")
