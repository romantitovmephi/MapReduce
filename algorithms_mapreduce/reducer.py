# reducer

import sys

(lastkey, sum) = (None, 0)
cntr = 0   # считает одинаковые страницы

for line in sys.stdin:
    (current_key, value) = line.strip().split('\t')
    if lastkey and lastkey != current_key:
        print(lastkey + '\t' + str(round(sum/cntr)))
        (lastkey, sum) = (current_key, int(value))
        cntr = 1
    else:
        (lastkey, sum) = (current_key, sum + int(value))
        cntr += 1

if lastkey:
    print(lastkey + '\t' + str(round(sum/cntr))) # чтобы учесть последние строки