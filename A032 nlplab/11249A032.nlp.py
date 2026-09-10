from nltk.stem import WordNetLemmatizer
lemmatizier=WordNetLemmatizer()
print(lemmatizier.lemmatize("cats"))
print(lemmatizier.lemmatize("cacti"))
print(lemmatizier.lemmatize("geese"))
print(lemmatizier.lemmatize("rocks"))
print(lemmatizier.lemmatize("python"))
