import sys

dict_graph = {}
for line in sys.stdin:
    key = line.strip().split('\t')[0]
    if line.strip().split('\t')[1] != 'INF':
        distance = int(line.strip().split('\t')[1])
    else:
        distance = float('inf')
    out_nodes = line.strip().split('\t')[2]
    value = []
    value.append(distance)
    value.append(out_nodes)
    if key not in dict_graph:
        dict_graph[key] = value
    else:
        if distance < dict_graph[key][0] and len(dict_graph[key][1]) < len(out_nodes):
            dict_graph[key][0] = distance
            dict_graph[key][1] = out_nodes
        elif distance >= dict_graph[key][0] and len(dict_graph[key][1]) < len(out_nodes):
            dict_graph[key][1] = out_nodes               
for key in dict_graph:
    print(f"{key}\t{str(dict_graph[key][0]).upper()}\t{dict_graph[key][1]}")


# 1    0    {2,3,4,5}
# 1    1    {}

# 5    2    {}
# 5    INF	{9,10}
# -----------
# 5    2    {9,10}

# 3 1 {}
# 3 2 {}
# 3 2 {4,5}
# ---------
# 3 1 {4,5}