import nltk

def respond(message):
    stemmer = nltk.stem.porter.PorterStemmer()
    tokens = [stemmer.stem(token).lower() for token in nltk.word_tokenize(message)]

    if tokens_in_list(['hi', 'hello', 'hey', 'sup', 'whatsup', 'howdy', 'yo', 'help'], tokens):
        return "Hello! how can I be of assistance to you?"

    if tokens_in_list(['ok','thanks', 'cool', 'thank'], tokens):
        return "You're welcome, my dear"

    if tokens_in_list(['load'], tokens):
        if 'balanc' in tokens:
            return 'ans1'
        elif 'firewal' in tokens:
            return 'ans2'
        elif 'hardware' in tokens:
            return 'ans3'
        elif 'SSD' in tokens:
            return 'ans4'
        elif 'image' in tokens:
            return 'ans5'
        elif 'ip' in tokens:
            return 'ans6'
        elif ['private', 'network'] in tokens:
            return 'ans7'
        elif 'all' in tokens:
            return 'ans8'
        else:
            return 'all info'
    elif tokens_in_list(['price', 'cost', 'pay'], tokens):
        return 'You are paying ${} per month'.format(40)
    elif 'test' in tokens:
        return 'test'
    else:
        return "I couldn't understand you, sorry. "

def tokens_in_list(search_tokens, tokens):
    for t in search_tokens:
        if t in tokens:
            return True
    else:
        return False
