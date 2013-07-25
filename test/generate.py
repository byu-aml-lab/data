import string
import random

ending_punctuation_data = '......!?' # make period much more common

def roll_xdy(x, y):
    return sum(random.randint(1, y) for _ in range(x))

def load_language(filename):
    text = open(filename).read()
    text = text.strip()
    text = text.lower()
    text = text.translate(None, string.punctuation)
    return text.split()

def generate_sentence(language):
    # Copy language since we'll sample without replacement.
    language = list(language)

    sampled_words = []

    for _ in range(roll_xdy(2, 5)):
        word = random.choice(language)
        language.remove(word)
        sampled_words.append(word)

    end_punctionation = random.choice(ending_punctuation_data)
    return ' '.join(sampled_words).capitalize() + end_punctionation

def generate_document(language):
    sentences = []

    for _ in range(roll_xdy(3, 3)):
        sentences.append(generate_sentence(language))

    return ' '.join(sentences)
