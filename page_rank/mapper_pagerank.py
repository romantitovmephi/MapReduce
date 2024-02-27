import sys
import re


for line in sys.stdin:
    print(line.strip())
    PageRank = float(line.strip().split('\t')[1])
    out_nodes = line.strip().split('\t')[2]
    list_out_nodes = re.sub("[{}]", "", out_nodes).split(',')
    p = float(round(PageRank / len(list_out_nodes), 3))
    p = "%.3f" % p
    for node in list_out_nodes:
        print(f"{node}\t{p}\t{{}}")