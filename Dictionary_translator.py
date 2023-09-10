from collections import OrderedDict

def creat_dictionary():
    dictionary = {} ##dict
    n = int(input()) ##number of words
    for i in range(n):  #for each word, itself and its meaning is saved in a dict.
        input_string = input()
        word, meaning = input_string.split()
        dictionary[word] = meaning 
        ordered_dictionary = OrderedDict(sorted(dictionary.items()))
    return ordered_dictionary
    
def translate_sentence(dictonary): ## this function cuts the sentence into words, then for each one
    sentence = input()             ## puts the translation instead of the word.
    translated_sentence = ""       ## if there is no translation, word remains the same.
    words = sentence.split()
    for word in words:
        if word in dictonary:
            translated_sentence += dictonary[word] + " "
        else:
            translated_sentence += word + " "
    print(translated_sentence.strip())

dictonary = creat_dictionary()
translate_sentence(dictonary)
