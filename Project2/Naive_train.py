from nltk import word_tokenize
from read_examples import read_examples
from nltk.tag import _pos_tag
from nltk.tag.perceptron import PerceptronTagger
from math import log10

import Paragraph

class Naive_Bayes:

    def __init__(self, n):
        self.token_probability= list()
        self.tokens = list()
        for i in range(0, n):
            self.tokens.append(list())
            self.token_probability.append(dict())

        self.tagger = PerceptronTagger()


    def add_token(self, paragraph):
        sentences = paragraph.scrambled_sentences
        for sentence,token in zip(sentences,self.tokens):
            pos_tokens = _pos_tag(word_tokenize(sentence), None, self.tagger)
            pos_tokens = [x[1] for x in pos_tokens]
            token.extend(pos_tokens)


    def train(self):
        for tokens, dictionary in zip(self.tokens, self.token_probability):
            for token in tokens:
                if token in dictionary:
                    dictionary[token] += 1
                else:
                    dictionary[token] = 1
            size = len(tokens)
            for token, count in dictionary.items():
                dictionary[token] = count/size



def main():
    examples = list()
    read_examples(examples)
    test = Naive_Bayes(5)
    for example in examples:
        example.order_sentence()
        test.add_token(example)
    test.train()
    print(test.token_probability)

if __name__ == "__main__":
    main()
