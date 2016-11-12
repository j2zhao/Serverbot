import nltk

def respond(message):
    stemmer = nltk.stem.porter.PorterStemmer()
    tokens = [stemmer.stem(token).lower() for token in nltk.word_tokenize(message)]

    if tokens_in_list(['load'], tokens):
        if 'balenc' in tokens:
            return 'ans1'
        elif 'firewal':
            return 'ans2'
    elif tokens_in_list(['price', 'cost', 'pay'], tokens):
        return 'You are paying ${} per month'.format(40)
    elif 'test' in tokens:
        return 'test'
    else:
        return "I couldn't understand you, sorry."

def tokens_in_list(search_tokens, tokens):
    for t in search_tokens:
        if t in tokens:
            return True
    else:
        return False
