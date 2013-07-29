#!/usr/bin/env python

import string
import random
import os

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

def mix_language(base, intruder, rate):
    intrude_length = int(len(base) * rate / (1 - rate))
    return base + random.sample(intruder, intrude_length)

def generate_category(language, size):
    return [generate_document(language) for _ in range(size)]

def generate_corpus(languages, corpus_size):
    sub_size = corpus_size // len(languages)
    return [generate_category(language, sub_size) for language in languages]

def write_corpus(categories, prefix, names=None):
    if names is None:
        names = [str(i) for i in range(len(categories))]
    for name, category in zip(names, categories):
        root = os.path.join(prefix, name)
        try:
            os.makedirs(root)
        except OSError as e:
            print e
            pass

        for i, document in enumerate(category):
            path = os.path.join(root, '{}-{}.txt'.format(name, i))
            with open(path, 'w') as out:
                out.write(document)

def main():
    train_root = os.path.join(os.path.dirname(__file__), 'training')
    latin = load_language(os.path.join(train_root, 'full-latin'))
    english = load_language(os.path.join(train_root, 'full-english'))
    latin_mix = mix_language(latin, english, .3)
    english_mix = mix_language(english, latin, .3)

    languages = [latin, english, latin_mix, english_mix]

    corpus = generate_corpus(languages, 20)
    write_corpus(corpus, os.path.join(train_root, '../data'))

if __name__ == '__main__':
    main()
