import sys

cate_list = []
cate_dict = {}

for line in sys.stdin:
    if line.replace("\t", "").strip() not in cate_list:   
        cate_list.append(line.replace("\t", "").strip())
#print(cate_list)

for numb_cate in cate_list:
    if numb_cate[1] not in cate_dict:
        cate_dict[numb_cate[1]] = 1
    else:
        cate_dict[numb_cate[1]] += 1
        
for cate in cate_dict:
    print(f"{cate}\t{int(cate_dict[cate])}")

'''
# более быстрая версия
import sys
from collections import defaultdict
d = defaultdict(int)
last = (None, None)
for line in sys.stdin:
    DataString = ""
    (val, key) = line.strip().split("\t")
    if (val, key) != last:
            d[key] += 1
            last = (val, key)
for key, val in d.items():
    print(key, val, sep = "\t")


'''