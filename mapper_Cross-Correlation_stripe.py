import sys
import re

for line in sys.stdin:
    elem_list = line.strip().split()
    for elem in elem_list:
        elem_dict = {}           # будут подсчитаны пары и их количество
        for item in elem_list:
            if item != elem:
                elem_dict[item] = elem_list.count(item)
        dict_for_print = re.sub("[{|}|'| ]","",str(elem_dict))     # удаляем лишнее из словаря (преоб-н в строку)
        print(f"{elem}\t{dict_for_print}")