import sys
import re 

cntr = 0
for line in sys.stdin:
    node = line.strip().split('\t')[0]
    distance = line.strip().split('\t')[1]
    out_nodes = line.strip().split('\t')[2]
    print(f"{node}\t{distance}\t{out_nodes}")
    if distance != 'INF':
        cntr = int(distance) + 1
    clean_out_nodes = re.sub("[{}]", "", out_nodes)
    list_out_nodes = clean_out_nodes.split(',')
    list_out_nodes = [i for i in list_out_nodes if i]  # удалить пустые строки из списка
    if len(list_out_nodes) > 0:
        for out_node in list_out_nodes:
            if distance != 'INF':
                print(f"{out_node}\t{cntr}\t{{}}")
            else:
                print(f"{out_node}\t{distance}\t{{}}")