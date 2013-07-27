import string
import random

def roll_xdy(x, y):
    return sum(random.randint(1, y) for _ in range(x))

def load_language(filename):
    text = open(filename).read()
    text = text.strip()
    text = text.lower()
    text = text.translate(None, string.punctuation)
    return text.split()

def generate_sentence(language):
    words = random.sample(language, roll_xdy(2, 5))
    ending_punctuation = random.choice('.....!?')
    return ' '.join(words).capitalize() + ending_punctuation

def generate_document(language):
    return ' '.join(generate_sentence(language) for _ in range(roll_xdy(3, 3)))

    return ' '.join(sentences)
