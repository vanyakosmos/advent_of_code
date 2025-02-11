import networkx as nx

from utils.display import check_result
from utils.loading import read_data

e1 = """
ka-co
ta-co
de-co
ta-ka
de-ta
ka-de
"""


def main(data=None):
    lines = read_data(data)
    edges = [line.split("-") for line in lines]

    g = nx.Graph()
    g.add_edges_from(edges)

    clusters = list(nx.find_cliques(g))
    clusters.sort(key=len, reverse=True)

    return ",".join(sorted(clusters[0]))


if __name__ == "__main__":
    check_result(main(e1), "co,de,ka,ta")
    check_result(main())
