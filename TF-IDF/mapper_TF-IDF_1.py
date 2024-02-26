import sys
import re

for line in sys.stdin:
    num_doc = line.strip().split(':')[0]
    words_line = line[line.find(":") + 1 : ]    # строка - после первого символа :
    clean_words_line = re.sub("[^A-Za-z0-9]", " ", words_line)
    words_list = clean_words_line.strip().split()
    for word in words_list:
        print(f"{word}#{num_doc}\t{1}")