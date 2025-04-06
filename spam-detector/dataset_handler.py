import os
from decouple import config

# Main/Parent dataset directory.
DATASET_DIR = config("MAIN_DIR") + config("DATASET_DIR")

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
      # Flag for spam directory.
      mark_spam = "spam"
    else:
      # Flag for non spam directory.
      mark_spam = "not_spam"

    # Load file list from above separated directories.
    files = os.listdir(DATASET_DIR + dir)
    dir_name = DATASET_DIR + dir + "/"

    # For every file in the directory.
    for file in files:
      dataset_map[mark_spam].append(dir_name + file)

  return dataset_map
