import sys


word_list = []
tuple_list = []

for line in sys.stdin:
    word = line.strip().split('\t')[0]
    info = line.strip().split('\t')[1]
    num_doc = info.split(';')[0]
    quantity = info.split(';')[1]
    w, d, q = word, num_doc, quantity   # создаем кортеж с инфо для каждого слова
    print((w, d, q))
    word_list.append(word)
    tuple_list.append((w, d, q))

print(word_list)
print(tuple_list)

for item in tuple_list:
    for elem in set(word_list):
        if item[0] == elem:
            print(f"{item[0]}#{item[1]}\t{item[2]}\t{word_list.count(elem)}")