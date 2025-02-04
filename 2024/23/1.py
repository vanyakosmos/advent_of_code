from collections import defaultdict
from pprint import pprint

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
        links[b].add(a)

    trios = set()
    for a, bs in links.items():
        for b in bs:
            thirds = bs & links[b]
            for third in thirds:
                trios.add(tuple(sorted([a, b, third])))

    trios = [t3 for t3 in trios if any(t[0] == "t" for t in t3)]

    print_result(len(trios), 7)


if __name__ == "__main__":
    main()
