from Paragraph import Paragraph
from N_grams import N_grams_training, POS_Ngram
from Naive_train import Naive_Bayes
from read_examples import read_examples
from math import log10

N = 3 # N-grams

def main():
    # TRAINING DATA
    train_paragraphs = list() # hold training Paragraphs
    filename_train = 'corpus/SHSAT_train.txt'
    read_examples(train_paragraphs, filename_train)
    n_grams_train = N_grams_training(N, train_paragraphs) # N grams from training set
    token_probability = Naive_Bayes(N) # Naive Bayes probabilities from training set
    # both have lists of dictionaries, where the position in the list corresponds to the sentence

    # TEST DATA
    test_paragraphs = list() # hold test Paragraphs
    filename_test = 'corpus/SHSAT_train.txt'
    read_examples(test_paragraphs, filename_test)

    #for para in test_paragraphs:
        # determine sentence 1, 2, 3, 4, 5

    for i in range(5): # iterate through position possibilities
        sentence_scores = list() # keep scores for each pos for each sentence
        para = list()
        para.append(test_paragraphs[1])
        para_POS = POS_Ngram(1, para, i+1) # dict: POS tags for each word
        for j in range(5): # iterate through sentence possibilities
            n_grams_test = POS_Ngram(N, para, j+1) # dict: N grams of this sentence
            current_score = 0
            for pos_test_ngram, score in n_grams_test.items(): # iterate through POS N grams of test sentence
                current_score += score * log10( n_grams_train.N_grams[i+1].get( pos_test_ngram, 1 ) )  # calculate log likelyhood of N gram in test set occuring
            #for pos_test_bayes, score in para_POS.items():
            #   current_score += log10( token_probability(i).get( pos_test_bayes, 1 ) )
            sentence_scores.append(current_score)
        print(sentence_scores)


if __name__ == "__main__":
    main()
