import re

import pandas

def read_corpus(corpus_name):
    f = open(corpus_name, "r")
    txt = f.read()

    return txt

def tag_scentences(txt):
    lines = txt.splitlines()
    lines = ["<s> " + line + " </s>" for line in lines]
    return lines

def calculate_unigram(txt):
    unigrams_list = []
    P_w_list = []

    split_words = re.split('\s|\n', txt)

    count_total = len(split_words)
    
    for word in split_words:
        if unigrams_list.count(word) == 0:

            count_w = split_words.count(word)
            p_w = count_w / count_total

            unigrams_list.append(word)
            P_w_list.append(p_w)

    return {"Unigram": unigrams_list, "P_w": P_w_list}

def calculate_bigram(txt):
    bigrmas_list = []
    P_w_list = []
    
    scentences = tag_scentences(txt)

    for scentence in scentences:

        split_words = re.split('\s', scentence)
        
        for i in range(1, len(split_words)):
            bigram = split_words[i - 1] + " " + split_words[i]

            if bigrmas_list.count(bigram) == 0:
                
                count_bigram = sum(len(re.findall(bigram, s)) for s in scentences)
                
                count_prev_w = 0
                for s in scentences:
                    words = re.split('\s', s)
                    count_prev_w += words.count(split_words[i - 1])

                P_w = count_bigram / count_prev_w

                if count_bigram != 0:
                    bigrmas_list.append(bigram)
                    P_w_list.append(P_w)

    return {"Bigram": bigrmas_list, "P_w": P_w_list}




def main():
    unigrams = calculate_unigram(read_corpus("corpus.en"))
    print(pandas.DataFrame(unigrams))

    print("-------------------------")

    bigrams = calculate_bigram(read_corpus("corpus.en"))
    print(pandas.DataFrame(bigrams))
    

if __name__=="__main__":
	main()
