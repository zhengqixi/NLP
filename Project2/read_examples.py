from __future__ import print_function, division

from Paragraph import Paragraph
import codecs as codecs
def read_examples(examples):
    #f = openFile("Enter training document file name: ")
    f = open('corpus/SHSAT_train.txt', 'rU')
    #f = codecs.open('corpus/SHSAT_train.txt', encoding='utf-8', errors='replace')
    count = 0
    for line in f:
        if (line == '\n'): # new example
            examples.append(Paragraph())
        elif (count == 0):
            count += 1
            examples[-1].set_first(line.decode("ascii", "ignore"))
        elif (count == 6): # end of example - read in correct ordering
            count = 0
            examples[-1].set_correct_order(line.decode("ascii", "ignore"))
        else: # read in sentence
            count += 1
            examples[-1].add_sentence(line.decode("ascii", "ignore"))
    f.close()

# read in training file and print out for debugging
# number of examples
# for each paragraph - first sentence, scrambled sentences, unscrambled, and correct ordering
def main():
    examples = list()
    read_examples(examples)
    for paragraph in examples:
        paragraph.order_sentence()
    print(str(examples))

if __name__ == "__main__":
    main()
