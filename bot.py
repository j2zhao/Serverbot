import nltk

def respond(message):
    stemmer = nltk.stem.porter.PorterStemmer()
    tokens = [stemmer.stem(token) for token in nltk.word_tokenize(message)]
    
    if 'price' in tokens:
        return 'You are paying $xxx per month'
    else:
        return tokens[0]