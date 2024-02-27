# ! Combiner считает сумму и количество (30;3), а не среднее. Потму что среднее считает уже Reducer

import sys

(lastkey, sum) = (None, 0)
cntr = 0   # считает одинаковые страницы

for line in sys.stdin:
    (current_key, value) = line.strip().split('\t')
    pure_seconds = (current_key, value)[-1][:-2:] # выбираем только секунды
    #print(pure_seconds)
    (current_key, value) = (current_key, pure_seconds) # собираем чистый кортеж без ;1
    #print(current_key, value)
    
    if lastkey and lastkey != current_key:
        print(lastkey + '\t' + str(round(sum)) + ';' + str(cntr))
        (lastkey, sum) = (current_key, int(value))
        cntr = 1
    else:
        (lastkey, sum) = (current_key, sum + int(value))
        cntr += 1

if lastkey:
    print(lastkey + '\t' + str(round(sum)) + ';' + str(cntr)) # чтобы учесть последние строки