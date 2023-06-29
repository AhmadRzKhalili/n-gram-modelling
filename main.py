def read_corpus(corpus_name):
    f = open(corpus_name, "r")
    txt = f.read()

    return txt

def calculate_unigram(txt):
    words = []
    unigrams = []

    import re
    split_words = re.split('\s|\n', txt)

    count_total = len(split_words)
    
    for word in split_words:
        if words.count(word) == 0:

            count_w = split_words.count(word)
            p_w = count_w / count_total
            unigrams.append({word: p_w})
            
            words.append(word)

    return unigrams

def main():
    print(calculate_unigram(read_corpus("corpus.en")))
    

if __name__=="__main__":
	main()
