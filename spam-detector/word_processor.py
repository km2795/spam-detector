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

  # Perform word stemming and lemmatization together.
  if stem and lemma:
    do_stem = [stemmer.stem(o) for o in words]
    do_lemma = [lemmatizer.lemmatize(item) for item in do_stem]
    processed_words = do_lemma
  
  # Perform either stemming or lemmatization only.
  else:
    processed_words = [stemmer.stem(item) for item in words] if stem else [lemmatizer.lemmatize(item) for item in words]

  # Return as a string if received as a string.
  return " ".join(processed_words) if str_flag else processed_words
