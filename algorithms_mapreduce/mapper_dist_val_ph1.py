import sys

for line in sys.stdin:
    numb, categories = line.strip().split('\t')
    #print(type(categories))
    category_list = categories.strip().split(',')
    #print(category_list)
    for category in category_list:
        print(f"{numb},{category}\t{1}")