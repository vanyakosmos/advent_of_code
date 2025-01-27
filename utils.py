from pathlib import Path


def read_data(full: int) -> list[str]:
    root = Path(__file__).parent
    if full:
        path = root / "input.txt"
    else:
        path = root / "example.txt"
    return path.read_text().splitlines()


def print_result(res) -> None:
    print("\n\nRESULT:", res)
