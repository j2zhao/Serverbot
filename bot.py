import nltk

class Bot(object):
    def __init__(self):
        self.stemmer = nltk.stem.porter.PorterStemmer()

    def respond(self, message):
        tokens = [self.stemmer.stem(token) for token in nltk.word_tokenize(message)]
        
        if 'price' in tokens:
            return 'You are paying $xxx per month'
        else:
            return tokens[0]