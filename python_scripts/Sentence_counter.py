import collections
from nltk import word_tokenize
import docx2txt


def get_sentences(essay):
    result = []
    some = ""
    for ws in essay:
        if(ws == '.'):
            result.append(some)
            some = ""
        else:
            if(ws!='\n'):
                some += ws
    return result


def get_word_stats():
    name = input("Please enter name of the file with format(f.e. txt.txt):\n")
    try:
        if("docx" in name):
            essay = docx2txt.process(name)
        else:
            f = open(name)
            essay = f.read()
    except FileNotFoundError:
        print("there is no such file in directory")
        exit()
    commas = 0
    words = 0
    result = get_sentences(essay)
    dictionary = {}
    for i in range(len(result)):
        result[i] = result[i].replace(',', ' comma')
        wordss = result[i].split()
        for j in range(len(wordss)):
            if(wordss[j]=='comma'):
                commas += 1
            else:
                words += 1
        small_dict = {}
        small_dict['commas'] = commas
        small_dict['words'] = words
        words = 0
        commas = 0
        dictionary['sentencte'+str(i+1)+''] = small_dict
    ordered = collections.OrderedDict(sorted(dictionary.items(), key=lambda i: i[1]['commas'], reverse=True))
    for keys,values in ordered.items():
        print(keys)
        print(values)

get_word_stats()