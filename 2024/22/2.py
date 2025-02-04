from collections import defaultdict

from utils.display import print_result
from utils.loading import read_data

e1 = """
123
"""

e2 = """
1
10
100
2024
"""


def next_num(secret: int):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216
    return secret


def main():
    full_prices_map = defaultdict(int)

    for line in read_data(e1, e2):
        secret = int(line)
        prices = []
        diffs = []
        for i in range(2000):
            next_secret = next_num(secret)
            price = next_secret % 10
            diff = next_secret % 10 - secret % 10
            prices.append(price)
            diffs.append(diff)
            secret = next_secret

        prices_map = defaultdict(int)
        for i in range(3, len(diffs)):
            key = tuple(diffs[i - 3 : i + 1])
            price = prices[i]
            if key not in prices_map:
                prices_map[key] = price

        for key, value in prices_map.items():
            full_prices_map[key] += value

    key, price = max(full_prices_map.items(), key=lambda x: x[1])
    print_result(price)


if __name__ == "__main__":
    main()
