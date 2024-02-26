import sys


for line in sys.stdin:
    word = line.strip().split('\t')[0]
    num_doc = line.strip().split('\t')[1]
    quantity = line.strip().split('\t')[2]
    print(f"{word}\t{num_doc};{quantity};{1}")