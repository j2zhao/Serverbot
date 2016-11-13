import nltk
import 1a1client.py

def respond(message):
    stemmer = nltk.stem.porter.PorterStemmer()
    tokens = [stemmer.stem(token).lower() for token in nltk.word_tokenize(message)]

    if tokens_in_list(['hi', 'hello', 'hey', 'sup', 'whatsup', 'howdy', 'yo', 'hello Chatterbox', 'help', 'can you help me?'], tokens):
        return "Hello! How can I be of assistance to you?"

    if tokens_in_list(['ok','thanks', 'cool'], tokens):
        return "Anything else I can help you with?"

    if tokens_in_list(['server'], tokens):
        if 'name' in tokens:
            return 'The server name is ' + getServerNames()
        elif 'id' in tokens:
            return 'ans2'
        elif 'status' in tokens:
            return 'ans3'
        elif 'HDD' in tokens:
            return 'ans4'
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
