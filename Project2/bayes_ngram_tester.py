from Paragraph import Paragraph
from N_grams import N_grams_training, POS_Ngram
from Naive_train import Naive_Bayes
from read_examples import read_examples
from math import log10

#N = 2 # N-grams

def main():
    # User input for N
    N = 0 # N-grams
    while True:
      try:
         N = int(input("Enter N: "))
      except ValueError:
         print("Not an integer!")
         continue
      else:
         break

    # TRAINING DATA
    train_paragraphs = list() # hold training Paragraphs
    filename_train = 'corpus/SHSAT_train.txt'
    read_examples(train_paragraphs, filename_train)
    n_grams_train = N_grams_training(N, train_paragraphs) # N grams from training set

    naive_bayes_model = Naive_Bayes(5) # Naive Bayes probabilities from training set
    for example in train_paragraphs:
        example.order_sentence()
        naive_bayes_model.add_token(example)
    naive_bayes_model.train()
    # both have lists of dictionaries, where the position in the list corresponds to the sentence

    # TEST DATA
    test_paragraphs = list() # hold test Paragraphs
    filename_test = 'corpus/SHSAT_test.txt'
    read_examples(test_paragraphs, filename_test)

    f = open("results2.txt", "w+")

    for k in range(len(test_paragraphs)):
        # determine sentence 1, 2, 3, 4, 5
        current_paragraph = test_paragraphs[k]
        ordering_scores = list()
        for i in range(5): # iterate through position possibilities
            sentence_scores = list() # keep scores for each pos for each sentence
            para = list()
            para.append(current_paragraph)
            para_POS = POS_Ngram(1, para, i+1) # dict: POS tags for each word
            for j in range(5): # iterate through sentence possibilities
                n_grams_test = POS_Ngram(N, para, j+1) # dict: N grams of this sentence
                current_score = 0
                for pos_test_ngram, score in n_grams_test.items(): # iterate through POS N grams of test sentence
                    current_score += score * log10( n_grams_train.N_grams[i+1].get( pos_test_ngram, 1 ) )  # calculate log likelyhood of N gram in test set occuring
                for pos_test_bayes, score in para_POS.items():
                    current_score += score * log10( naive_bayes_model.token_probability[i].get( pos_test_bayes, 1 ) )
                #sentence_scores.append( ( current_score, para[j] )
                sentence_scores.append( current_score )
            #f.write(str(sentence_scores) + '\n')
            ordering_scores.append(sentence_scores)
        #f.write('\n\n')

        for m in range(len(ordering_scores)): # iterate through sentence orders
            nth_sentence = ordering_scores[m]
            for i in range(len(nth_sentence)): # iterate through choice possibilities
                if len(current_paragraph.predicted_order) == 0:
                    choice = nth_sentence.index(min(nth_sentence))
                else:
                    already_chosen = current_paragraph.predicted_order[-1] # last one added
                    for j in range(i,5):
                        ordering_scores[j][already_chosen] = 0 # set to 0, this sentence already chosen
                choice = nth_sentence.index(min(nth_sentence))
                #print(choice)
                current_paragraph.predicted_order.append(choice)

        current_paragraph.order_sentence()
        f.write(str(current_paragraph))



if __name__ == "__main__":
    main()
