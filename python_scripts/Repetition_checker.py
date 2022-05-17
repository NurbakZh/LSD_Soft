import collections
from nltk import word_tokenize
import docx2txt


def get_sentences(essay):
    result = []
    word_splitted = word_tokenize(essay)
    for ws in word_splitted:
        if (ws.isalnum()):
            result.append(ws)
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
    result = get_sentences(essay)
    lr = list(map(lambda x: x.lower(), result))
    counter = {i: lr.count(i) for i in lr}
    return collections.Counter(counter)

print(get_word_stats().most_common(20))
