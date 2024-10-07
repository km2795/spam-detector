from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Word stemming algorithm.
stemmer = PorterStemmer()

# Word lemmatizing algorithm.
lemmatizer = WordNetLemmatizer()

# Utility to perform word stemming or lemmatization.
def process_word(stem, lemma, words, delim):
  # If argument passed is a string or not,
  # Need to return it as the same type.
  str_flag = False

  # See if there is need to split the input or not.
  if (type(words) == str):
    words = words.split(delim)
    str_flag = True

  # Perform word stemming.
  if stem:
    processed_words = [stemmer.stem(item) for item in words]

  # Perform word lemmatization.
  elif lemma:
    processed_words= [lemmatizer.lemmatize(item) for item in words]

  # Perform both consecutively.
  else:
    do_stem = [stemmer.stem(o) for o in words]
    do_lemma = [lemmatizer.lemmatize(item) for item in do_stem]
    processed_words = do_lemma

  # Return as a string if received as a string.
  return " ".join(processed_words) if str_flag else processed_words
