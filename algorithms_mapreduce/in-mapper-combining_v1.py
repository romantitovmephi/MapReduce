import sys
from collections import Counter     

map_list_for_dicts = []

for line in sys.stdin:            # для каждой строки ввода
    result_dict = {}
    for word in line.strip().split(' '):    # для каждого слова в строке
        map_dict = {word: 1}                # создаем словарь со значение 1
        map_list_for_dicts.append(map_dict)
    #print(map_list_for_dicts)
    # счетчиком - считаем все значения по одинаковым ключам в списке словарей
    result_dict = Counter()
    for every_dict in map_list_for_dicts:
        result_dict.update(every_dict)
    #print(result_dict)
    '''
    for dictionary in map_list_for_dicts:     # без счетчика - считаем все значения по одинаковым ключам в списке словарей
        for key in dictionary:
            try:
                result_dict[key] += dictionary[key]
            except KeyError:  
                result_dict[key] = dictionary[key]
    #print(result_dict)
    '''
    for every_key in result_dict: 
        print(str(every_key)  + '\t' + str(result_dict[every_key]))   # выводим слово и то, сколько раз оно встретилось в строке
    map_list_for_dicts.clear()    # чистим список для следующей строки