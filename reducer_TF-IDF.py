import sys


words_dict = {}
for line in sys.stdin:
    key = line.strip().split('\t')[0]
    value = line.strip().split('\t')[1]
    if key not in words_dict: 
        words_dict[key] = int(value)
    else:
        words_dict[key] += 1
for key in words_dict:
    word = key.split('#')[0]
    num_doc = key.split('#')[1]
    quantity = words_dict[key]
    print(f"{word}\t{num_doc}\t{quantity}")