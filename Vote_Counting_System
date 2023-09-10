from collections import OrderedDict
word_count = {} ##dict

n = int(input()) ##number of inputs (total votes)


for i in range(n):
    word = input()
    word_count[word] = word_count.get(word,0) + 1 

ordered_word_count = OrderedDict(sorted(word_count.items()))

for word, count in ordered_word_count.items(): ## the code iterates through the key-value pairs 
    print(word, count)                         ## in the ordered_word_count dictionary and prints 
                                               ## the word followed by its count. 
