from __future__ import print_function, division

from Paragraph import Paragraph
import re
# Read in format from scrambledparas.blogspot.com and convert to our format
# Removes whitespace and combines sentences from across newlines

# website format:
# first
# ___(Q) sen1
# ___(R) sen2
# ....
# 12345

# our format
# first
# Q. sen1
# R. sen2
# ...
# 12345


def read_file():
    para_list = list()
    f = open('corpus/train.txt', 'rU')
    num_ans = 0
    end_of_set = False
    ans_pattern = re.compile('\d{5}')
    in_prompt = False
    in_ans = False
    ans_count = 0
    for line in f:
        if line == '\n': # ignore empty line
            in_ans = False
            in_prompt = False
            continue
        if line.startswith('http') or line.startswith('www'): # ignore URL
            continue
        if line.startswith('_____'):
            ans_count += 1
            in_ans = True
            letter = line[line.find("(")+1:line.find(")")] # get letter option
            sentence = line[line.find(")")+1:len(line)-1] # get sentence
            para_list[-1].sentences.append(letter + '.' + sentence + ' ') # add this sentence to the last element
            continue
        if in_prompt:
            para_list[-1].first += line.strip('\n') + ' '
            continue
        if in_ans:
            para_list[-1].sentences[ans_count-1] += line.strip('\n') + ' '
            continue
        if "Answers:" in line:
            end_of_set = True
            continue
        if end_of_set: # add solution
            soln = re.search(ans_pattern, line)
            if not soln:
                # new paragraph start
                end_of_set = False
                ans_count = 0
                #end_of_set = False
                in_prompt = True
                para_list.append(Paragraph())
                para_list[-1].first = line.strip('\n') + ' '
                num_ans += 1
                continue
            soln_string = line[soln.start():soln.end()]
            para_list[len(para_list) - num_ans].order = list(soln_string)
            num_ans -= 1
            continue
        # new paragraph start
        ans_count = 0
        #end_of_set = False
        in_prompt = True
        para_list.append(Paragraph())
        para_list[-1].first = line.strip('\n') + ' '
        num_ans += 1
    return para_list

def print_paras(para_list):
    f = open('SHSAT_train_scrambledparas', 'w+')
    for p in para_list:
        f.write(str(p))
    f.close()


def main():
    para_list = read_file()
    print_paras(para_list)


if __name__ == "__main__":
    main()
