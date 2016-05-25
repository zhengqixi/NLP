from __future__ import print_function, division

from Paragraph import Paragraph
import codecs as codecs
def read_examples(examples, filename):
    f = open(filename, 'rU')
    count = 0
    for line in f:
        if (line == '\n'): # new example
            examples.append(Paragraph())
        elif (count == 0):
            count += 1
            examples[-1].set_first(line)
        elif (count == 6): # end of example - read in correct ordering
            count = 0
            examples[-1].set_correct_order(line)
        else: # read in sentence
            count += 1
            examples[-1].add_sentence(line)
    f.close()

# read in training file and print out for debugging
# number of examples
# for each paragraph - first sentence, scrambled sentences, unscrambled, and correct ordering
def main():
    examples = list()
    filename = 'corpus/SHSAT_train.txt'
    read_examples(examples, filename)
    for paragraph in examples:
        paragraph.order_sentence()
    print(str(examples))

if __name__ == "__main__":
    main()
