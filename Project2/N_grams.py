from __future__ import print_function, division

from Paragraph import Paragraph
from read_examples import read_examples

from nltk import word_tokenize, ngrams

from nltk.tag.perceptron import PerceptronTagger
from nltk.tag import _pos_tag
tagger = PerceptronTagger()

class N_grams_training:
    def __init__(self, N, examples): # N is N-grams, examples is a list of Paragraphs
        self.N_grams = list() # list of dictionaries to hold unique N gram POS tags and each count, per sentence
        for i in range(6): # 0 is for the first sentence, 1 to 5 are for order indexing
            N_grams.append(dict())
            POS_Ngram(N, examples, self.N_grams[-1], i)

# return POS N grams of each sentence
def POS_Ngram(N, example_set, N_grams, i):

    for para in example_set:
        if i == 0: # get first sentence
            tokens = word_tokenize(para.first)
        else: # get ith sentence
            tokens = word_tokenize(para.scrambled_sentences[int(para.correct_order[i-1])-1])
        tagset = None
        tokens = _pos_tag(tokens, tagset, tagger)

        tags = [x[1] for x in tokens] # take POS tags only

        n_tags = list(ngrams(tags, N))

        for tag_set in n_tags:
            if tag_set in N_grams:
                N_grams[tag_set] += 1
            else:
                N_grams[tag_set] = 1 # first occurence of tagset
    return N_grams

def main():
    examples = list()
    read_examples(examples) # read examples from example file

    N = 0 # N-grams
    while True:
      try:
         N = int(input("Enter N: "))
      except ValueError:
         print("Not an integer!")
         continue
      else:
         break

    N_grams = list() # list of dictionaries to hold unique N gram POS tags and each count, per sentence
    for i in range(6): # 0 is for the first sentence, 1 to 5 are for order indexing
        N_grams.append(dict())
        POS_Ngram(N, examples, N_grams[-1], i)

    #print(N_grams)
    if N == 3:
        filename = 'output-trigrams.txt'
    elif N == 2:
        filename = 'output-bigrams.txt'
    else:
        filename = 'output-'+ str(N) + 'grams.txt'

    f = open(filename, 'w+')
    count = 0
    for ngram in N_grams:
        f.write("list " + str(count) + '\n')
        count += 1
        for key, value in ngram.iteritems():
            out = str(key) + ' ' + str(value) + '\n'
            f.write(out)
    f.close()
    print('Results written to '+ filename)

if __name__ == "__main__":
    main()
