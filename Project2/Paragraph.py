from __future__ import print_function, division

class Paragraph:
    def __init__(self):
        self.first = "" # first sentence (String)
        self.scrambled_sentences = list() # scrambled sentences (list of String)
        self.correct_order = list() # correct ordering of sentences (list of Int)
        self.predicted_order = list()
        self.ordered_sentences = list()

    def set_first(self, first): # save first sentence
        self.first = first

    def set_correct_order(self, order): # set correct ordering, stripping newline
        self.correct_order = list(order.strip('\n'))

    def set_predicted_order(self, order):
        self.predicted_order = list(order.strip('\n'))

    def add_sentence(self, sen): # add sentence to list, stripping newline and letter designation
        self.scrambled_sentences.append(sen.strip('\n')[3:])

    def order_sentence(self):
        #if not self.predicted_order or not self.scrambled_sentences:
        #        print('Please set predicted order and scrambled sentences')
        #        return False
        self.ordered_sentences = [sentence for order, sentence in sorted(zip(self.correct_order, self.scrambled_sentences))]

    def order_predicted(self):
        self.ordered_sentences = [sentence for order, sentence in sorted(zip(self.predicted_order, self.scrambled_sentences))]

    def __str__(self):
        #sentences = ""
        #order = ""
        #for i in range(len(self.sentences)):
        #    sentences += self.sentences[i] + '\n'
        #for i in range(len(self.order)):
        #    order += self.order[i]
        #
        #return '\n' + self.first + '\n' + sentences + order + '\n'

        sentences = ""
        order = ""
        correct_sentences = ""
        predicted_sen = ""
        for i in range(len(self.scrambled_sentences)):
            sentences += self.scrambled_sentences[i] + '\n'
            correct_sentences += self.ordered_sentences[i] + '\n'

        if(len(self.predicted_order) > 0):
            self.order_predicted()
            #self.ordered_sentences = [sentence for order, sentence in sorted(zip(self.predicted_order, self.scrambled_sentences))]
            for i in range(len(self.ordered_sentences)):
                predicted_sen += self.ordered_sentences[i] + '\n'


        for i in range(len(self.correct_order)):
            order += self.correct_order[i]
        return '\n' + self.first + '\n' + 'Original Scrambled Order: \n \n' +  sentences + '\n' + 'Predicted Order: \n \n' + predicted_sen + '\n'+ 'Correct Order: \n \n' + correct_sentences + '\n'

    def __repr__(self):
        sentences = ""
        order = ""
        correct_sentences = ""
        for i in range(len(self.scrambled_sentences)):
            sentences += self.scrambled_sentences[i] + '\n'
            correct_sentences += self.ordered_sentences[i] + '\n'
        for i in range(len(self.correct_order)):
            order += self.correct_order[i]
        return '\n' + self.first + '\n' + sentences + '\n' + correct_sentences +  order + '\n'
