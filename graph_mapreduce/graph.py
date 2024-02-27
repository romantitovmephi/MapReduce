# поиск кратчайшего пути в графе
import networkx as nx
import sys

graph_list = []
cntr = 0
for line in sys.stdin:
    if cntr == 0:
        nodes = line.strip().split()[0]
        cntr_max = int(line.strip().split()[1])
    elif 1 <= cntr <= cntr_max:
        out_node = line.strip().split()[0]
        in_node = line.strip().split()[1]
        weight = int(line.strip().split()[2])
        (out_n, in_n, w) = (out_node, in_node, weight)
        graph_list.append((out_n, in_n, w))
    elif cntr == cntr_max + 1:
        start_node = line.strip().split()[0]
        end_node = line.strip().split()[1]
    cntr += 1
           
G = nx.DiGraph()
G.add_weighted_edges_from(graph_list)
try:
    print(nx.shortest_path_length(G, start_node, end_node, weight='weight'))
except:
    print(-1)