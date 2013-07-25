import string
import random

def load_language(filename):
    text = open(filename).read()
    text = text.strip()
    text = text.lower()
    text = text.translate(None, string.punctuation)
    return text.split()

def generate_sentence(language, size):
    language = list(language) # since we'll sample without replacement
    sentence = []

    for _ in range(size):
        word = random.choice(language)
        language.remove(word)
        sentence.append(word)

    return ' '.join(sentence).capitalize() + random.choice('...!?')
