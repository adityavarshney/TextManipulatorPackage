from nltk.tokenize import word_tokenize, sent_tokenize


class TextManipulator():
    def __init__(self, text):
        self.text = text
        self.sentences = sent_tokenize(text)
        self.words = [word_tokenize(i) for i in self.sentences]

    def get_sentences(self):
        return self.sentences

    def get_words(self):
        return self.words
