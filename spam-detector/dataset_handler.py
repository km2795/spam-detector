import os
from decouple import config

# Main/Parent dataset directory.
DATASET_DIR = config("MAIN_DIR") + "spam-detector/dataset/"

def get_dataset_map():

  # Separate files (file names) based on spam or ham (not_spam).
  dataset_map = {
    "spam": [],
    "not_spam": []
  }

  # Fetch the list of sub-directories from the parent dataset directory.
  directories = os.listdir(DATASET_DIR)

  # Traverse the sub-directories.
  for dir in directories:
    if (dir == "spam" or dir == "spam_2"):
      mark_spam = True
    else:
      mark_spam = False

    # Load file list from the directory.
    files = os.listdir(DATASET_DIR + dir)
    dir_name = DATASET_DIR + dir + "/"

    # For every file in the directory.
    for file in files:
      if mark_spam:
        dataset_map["spam"].append(dir_name + file)
      else:
        dataset_map["not_spam"].append(dir_name + file)

  return dataset_map
