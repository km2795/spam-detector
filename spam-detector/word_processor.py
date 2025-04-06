from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Word stemming algorithm.
stemmer = PorterStemmer()

# Word lemmatizing algorithm.
lemmatizer = WordNetLemmatizer()

"""
Utility to perform word stemming and/or 
lemmatization along with general cleaning.
"""
def process_word(stem, lemma, words, delim):
  # If string contains only new or a space character or is empty, then
  # return empty string.
  if (words == '\n' or words == '' or words == ' '):
    return ""

  # If argument passed is a string or not,
  # Need to return it as the same type.
  str_flag = False
  processed_words = []

  # See if there is need to split the input or not.
  if (type(words) == str and delim is not None):
    words = words.split(delim)
    str_flag = True

  # Perform word stemming and lemmatization together.
  if stem and lemma:
    for word in words:
      if word is not ' ' and word is not '':
        word = stemmer.stem(word)
        word = lemmatizer.lemmatize(word)
        processed_words.append(word)
  
  # Perform either stemming or lemmatization (by-default) only.
  else:
    for word in words:
      if word is not ' ' and word is not '':
        processed_words.append(stemmer.stem(word) if stem else lemmatizer.lemmatize(word))

  # Return as a string if received as a string.
  return "".join(processed_words) if str_flag else processed_words
