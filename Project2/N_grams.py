from __future__ import print_function, division

from Paragraph import Paragraph
from read_examples import read_examples

import nltk
from nltk import word_tokenize, ngrams

from nltk.tag.perceptron import PerceptronTagger
tagger = PerceptronTagger()

#N = 3 # N-grams

# return POS N grams of each sentence
def POS_Ngram(N, example_set, N_grams, i):
    for para in example_set:
        if( i < 3 ):
            tokens = nltk.word_tokenize(para.sentences[i])
        else:
            tokens = nltk.word_tokenize(para.first)
        #tokens = nltk.pos_tag(tokens)
        tagset = None
        tokens = nltk.tag._pos_tag(tokens, tagset, tagger)
        #print(tokens)
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

    N_grams = dict() # dictionary to hold unique N gram POS tags and each count
    for i in range(4):
        POS_Ngram(N, examples, N_grams, i)

    #print(N_grams)
    if N == 3:
        filename = 'output-trigrams.txt'
    elif N == 2:
        filename = 'output-bigrams.txt'
    else:
        filename = 'output-'+ str(N) + 'grams.txt'

    f = open(filename, 'w+')
    for key, value in N_grams.iteritems():
        out = str(key) + ' ' + str(value) + '\n'
        f.write(out)
    f.close()
    print('Results written to '+ filename)

if __name__ == "__main__":
    main()
