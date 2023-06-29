import re

from IPython.display import display
import pandas

def read_corpus(corpus_name):
    f = open(corpus_name, "r")
    txt = f.read()

    return txt

def calculate_unigram(txt):
    words_list = []
    P_w_list = []

    split_words = re.split('\s|\n', txt)

    count_total = len(split_words)
    
    for word in split_words:
        if words_list.count(word) == 0:

            count_w = split_words.count(word)
            p_w = count_w / count_total

            words_list.append(word)
            P_w_list.append(p_w)

    return {"Word": words_list, "P_w": P_w_list}

def main():
    unigrams = calculate_unigram(read_corpus("corpus.en"))
    print(pandas.DataFrame(unigrams))
    

if __name__=="__main__":
	main()
