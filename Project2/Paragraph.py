from __future__ import print_function, division

class Paragraph:
    def __init__(self):
        self.first = "" # first sentence (String)
        self.sentences = list() # scrambled sentences (list of String)
        self.order = list() # correct ordering of sentences (list of Int)
    def set_first(self, first): # save first sentence
        self.first = first
    def set_order(self, order): # set correct ordering, stripping newline
        self.order = list(order.strip('\n'))
    def add_sentence(self, sen): # add sentence to list, stripping newline and letter designation
        self.sentences.append(sen.strip('\n')[3:])
    def __str__(self):
        sentences = ""
        order = ""
        for i in range(len(self.sentences)):
            sentences += self.sentences[i] + '\n'
        for i in range(len(self.order)):
            order += self.order[i]
        return '\n' + self.first + '\n' + sentences + order + '\n'
    def __repr__(self):
        sentences = ""
        order = ""
        for i in range(len(self.sentences)):
            sentences += self.sentences[i] + '\n'
        for i in range(len(self.order)):
            order += self.order[i]
        return '\n' + self.first + '\n' + sentences + order + '\n'
