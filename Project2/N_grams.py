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
            self.N_grams.append(dict())
            self.N_grams[-1] = POS_Ngram(N, examples, i)

# return POS N grams of each sentence
def POS_Ngram(N, example_set, i):
    N_grams = dict()
    count = 0
    for para in example_set:
        if i == 0: # get first sentence
            tokens = word_tokenize(para.first)
        else: # get ith sentence
            para.order_sentence()
            tokens = word_tokenize(para.ordered_sentences[i-1])
            #tokens = word_tokenize(para.scrambled_sentences[int(para.correct_order[i-1])-1])
        tagset = None
        #print(tokens)
        tokens = _pos_tag(tokens, tagset, tagger)

        tags = [x[1] for x in tokens] # take POS tags only

        n_tags = list(ngrams(tags, N))

        for tag_set in n_tags:
            count += 1
            if tag_set in N_grams:
                N_grams[tag_set] += 1
            else:
                N_grams[tag_set] = 1 # first occurence of tagset
    # Normalize N_gram counts by total number of N grams for this set of sentences
    for ngram, num in N_grams.items():
        N_grams[ngram] = num/count
    return N_grams

def main():
    examples = list()
    filename = 'corpus/SHSAT_train.txt'
    read_examples(examples, filename) # read examples from example file

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
        N_grams[-1] = POS_Ngram(N, examples, i)

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
        for key, value in ngram.items():
            out = str(key) + ' ' + str(value) + '\n'
            f.write(out)
    f.close()
    print('Results written to '+ filename)

if __name__ == "__main__":
    main()
