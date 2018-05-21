from manipulate_text import TextManipulator
from unittest import TestCase

class TestTextManipulator(TestCase):

    def test_sentence_split(self):
        example = 'i like food. food is good.'
        instance = TextManipulator(example)
        self.assertEqual(instance.get_sentences(), ['i like food.', 'food is good.'])
        print('Test passed')

    def test_word_split(self):
        example = 'i like food. food is good.'
        instance = TextManipulator(example)
        self.assertEqual(instance.get_words(), [['i', 'like', 'food', '.'],['food', 'is', 'good', '.']])
        print('Test passed')

def main():
    test = TestTextManipulator()
    test.test_sentence_split()
    test.test_word_split()

main()