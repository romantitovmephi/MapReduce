import sys

category_list =[]

for line in sys.stdin:
    if line.strip().split('\t')[0] not in category_list:     # отрезаем по табу, берем первый (0) кусок
        category_list.append(line.strip().split('\t')[0])
        print(line.strip().split('\t')[0])