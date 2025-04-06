import os
from decouple import config

# Turn off information log.
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

import dataset_parser as dataset_parser
import spam_detector_train as sd_train
import spam_detector_test as sd_test

# Main directory for the project.
MAIN_DIR = config("MAIN_DIR")

# Model storage directory.
MODEL_DUMP_DIRECTORY = MAIN_DIR + config("MODEL_DUMP_DIRECTORY")

# Prepare the dataset.
( train_set_input,
  train_set_output,
  test_set_input,
  test_set_output ) = dataset_parser.process_dataset()

# Input layer size for the sequential model.
model_input_size = len(train_set_input[0])


print("\n\nTraining model...\n\n")

# Train the model.
model_accuracy = sd_train.train_model(model_input_size, 
                                      train_set_input,
                                      train_set_output, 
                                      test_set_input, 
                                      test_set_output, 
                                      MODEL_DUMP_DIRECTORY)

print("\n\nTesting model...\n\n")

# Test the model.
test_result = sd_test.test_model(test_set_input, 
                                 test_set_output, 
                                 MODEL_DUMP_DIRECTORY)

# How the model performed.
print("\n\nModel Accuracy: ", test_result, "\n\n")
