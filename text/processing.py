import string
import unicodedata


def unaccent(text):
    nkfd_form = unicodedata.normalize('NFKD', text)
    return u''.join([c for c in nkfd_form if not unicodedata.combining(c)])


def deponctuate(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def tokenize(text):
    text = text.replace('\n', ' ').replace('\r', '').lower()
    tokens = [token for token in text.split(' ') if token]
    return ' '.join(tokens), len(tokens)