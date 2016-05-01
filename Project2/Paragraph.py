from __future__ import print_function, division

def read_examples(examples):
    #f = openFile("Enter training document file name: ")
    f = open('NLP/Project2/corpus/SHSAT_train.txt', 'rU')
    N = f.readline() # Read in total number of examples in this file
    count = 0;
    for line in f:
        if (line == '\n'): # new example
            examples.append(Paragraph())
        elif (count == 0):
            count += 1
            examples[-1].set_first(line)
        elif (count == 6): # end of example - read in correct ordering
            count = 0
            examples[-1].set_order(line)
        else: # read in sentence
            count += 1
            examples[-1].add_sentence(line)
    f.close()
    return N

class Paragraph:
    def __init__(self):
        self.first = "" # first sentence (String)
        self.sentences = list() # scrambled sentences (list of String)
        self.order = list() # correct ordering of sentences (list of Int)
    def set_first(self, first): # save first sentence
        self.first = first;
    def set_order(self, order): # set correct ordering, stripping newline
        self.order = list(order.strip('\n'))
    def add_sentence(self, sen): # add sentence to list, stripping newline and letter designation
        self.sentences.append(sen.strip('\n')[3:])
    def __str__(self):
        return '\n' + self.first + str(self.sentences) + '\n' + str(self.order) + '\n'
    def __repr__(self):
        return '\n' + self.first + str(self.sentences) + '\n' + str(self.order) + '\n'

# read in training file and print out for debugging
# number of examples
# for each paragraph - first sentence, scrambled sentences, and correct ordering
def main():
    examples = list()
    N = read_examples(examples)
    print(N)
    print(str(examples))

if __name__ == "__main__":
    main()
