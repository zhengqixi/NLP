# 2016 ECE 367 Final Project: SHSAT Scrambled Paragraph Solver
##Rebecca Poch and Zhengqi Xi
[Located here!](https://github.com/zhengqixi/NLP/tree/master/Project2)

----
## What is the SHSAT?
from the [NYC gov website](http://schools.nyc.gov/accountability/resources/testing/shsat.htm)

The SHSAT (Specialized High School Admissions Test) taken by  middle schoolers in New York City in hopes of getting into the top high schools in NYC, including Stuyvesant High School, Bronx Science, and Brooklyn Tech. There is one section that gives the students a scrambled paragraph of 5 sentences that must put into the correct order. 


----
## Goal
We aim to create a system that will determine algorithmically correct ordering of sentences that will perform better than chance. (1/5! = 1/120 = 0.833%) 


----
## Methods Used
We implemented a part of speech (POS) Naive Bayes Classifier along with a POS N-Gram model.  The Naive Bayes Classifier acted as our translation model while the N-Gram model served as our language model.  The system was trained by each sentence position (e.g. every first sentence POS tags were averaged).  

In our proposal, we considered using pronoun resolution, but it turned out to be too difficult and time consuming to implement.  The sentence ordering techniques in the papers we linked also turned out not to be useful for our project - chronological ordering based on when articles were published or different document types.


----
## Testing and Training Set
The training data were obtained from (Daniel Gauss: Practice Scrambled Paragraphs)[http://scrambledparas.blogspot.com/]. Scrambled paragraphs were also obtained from SHSAT Practice Booklets. In total, there were about 200 examples.

The test set was composed of sample paragraphs from the official SHSAT handbooks from 2008 to 2015.  There are 33 examples in total.


----
## Usage
Download and unzip the repo 

Navigate to the directory that you downloaded it in

Run in command line (or use a python IDE) 

    python bayes_ngram_tester.py

The output file, results.txt, contain the paragraphs of the test set. The first line is the first given sentence. The first paragraph is the scrambled order. The second paragraph is the predicted order. The last paragraph is the correct ordering.

The command line printout displays microaveraged data (how many first sentences, second sentences, and so on that the system correctly predicted), as well as macroaveraged data (how many sentences were correct out of each 5 sentence paragraph).

    bayes_ngram_tester.py
Calculates probability of a sentence being the nth one using POS Naive Bayes and POS N-grams. 

    Paragraph.py
Data structure to hold sentences and correct ordering. Also print out in a nice format.

    read_examples.py
Read in examples from the specified file.

    N_grams.py
Calculate normalized N gram counts for each nth sentence.

    Naive_train.py
Calculate Naive Bayes probability for each nth sentence for training.


----
## Results 


### 2-Grams

Total Completely Correct: 0

Total Incorrect: 33

Percentage right: 0.0

[4, 5, 3, 8, 5]

### 3-Grams

Total Completely Correct: 0

Total Incorrect: 33

Percentage right: 0.0

[11, 5, 11, 8, 3]

----
## Reflections

Gathering the corpus data and formatting it in a consistent way took much longer than expected. The data came from a mix of online sources and offline sources (using OCR for text extraction). The paragraphs also had to be matched with their answers, which were not on the same page or close to each other.  Given more time, we could try other techniques to compare and improve our results, such as coherence resolution and pronoun resolution.


----
## Special thanks to:
* Johnny Chen, Kangqiao Lei, Mr. Collins for helping provide training set data.
