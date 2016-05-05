from __future__ import print_function, division

from Paragraph import Paragraph

def read_examples(examples):
    #f = openFile("Enter training document file name: ")
    f = open('corpus/SHSAT_train.txt', 'rU')
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
