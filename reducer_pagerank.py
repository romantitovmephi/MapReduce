import sys


dict_nodes = {}
for line in sys.stdin:
    key = line.strip().split('\t')[0]
    p = float(line.strip().split('\t')[1])
    p = float("%.3f" % p)
    out_nodes = line.strip().split('\t')[2]
    value = []
    value.append(p)
    value.append(out_nodes)
    if key not in dict_nodes:
        if out_nodes == '{}':
            dict_nodes[key] = value
        else:
            dict_nodes[key] = value   # для случая, когда на страницу нет ссылок с других страниц совсем
            dict_nodes[key][0] = 0    # р = 0, если пришел непустой список смежных вершин         
    elif key in dict_nodes and out_nodes == '{}':
        dict_nodes[key][0] += p
    elif key in dict_nodes and out_nodes != '{}':
        dict_nodes[key][1] = out_nodes
for key in dict_nodes:
    dict_nodes[key][0] = "%.3f" % dict_nodes[key][0]
    print(f"{key}\t{dict_nodes[key][0]}\t{dict_nodes[key][1]}")