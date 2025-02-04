from utils.display import print_result
from utils.loading import read_data

e1 = """
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
    res = 0
    for line in read_data(e1):
        secret = int(line)
        orig_secret = secret
        for i in range(2000):
            secret = next_num(secret)
        print(f"{orig_secret}: {secret}")
        res += secret
    print_result(res)


if __name__ == "__main__":
    main()
