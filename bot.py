import nltk
import oneclient

def respond(message):
    stemmer = nltk.stem.porter.PorterStemmer()
    tokens = [stemmer.stem(token).lower() for token in nltk.word_tokenize(message)]
    
    if tokens_in_list(['hi', 'hello', 'hey', 'sup', 'whatsup', 'howdy', 'yo', 'help'], tokens):
        return "Hello! How can I be of assistance to you?"
    elif tokens_in_list(['ok', 'thanks', 'cool', 'thank'], tokens):
        return "You're welcome, my dear. Anything else I can help you with?"
    elif tokens_in_list(['server'], tokens):
        if 'name' in tokens:
            return 'The server names are: ' + ', '.join(oneclient.getServerNames())
        elif 'id' in tokens or 'ids' in tokens:
            return 'The server IDs are: ' + ', '.join(oneclient.getServerIDs())
        elif 'status' in tokens:
            return 'The server status is: '
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
