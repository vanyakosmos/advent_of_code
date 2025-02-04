from collections import defaultdict

from utils.display import print_result
from utils.loading import read_data

e1 = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""


def main():
    links = defaultdict(set)
    for line in read_data(e1):
        a, b = line.split("-")
        links[a].add(b)
        links[a].add(a)
        links[b].add(a)
        links[b].add(b)

    checked = set()

    def t(node: str, visited: set):
        if node in visited:
            return visited
        if len(visited & links[node]) != len(visited):
            return visited
        res = set()
        visited = visited | {node}
        for link in links[node]:
            sub = t(link, visited)
            if len(sub) > len(res):
                res = sub
        return res

    max_lan = max((t(node, set()) for node in links), key=len)
    print_result(",".join(sorted(max_lan)), "co,de,ka,ta")


if __name__ == "__main__":
    main()
