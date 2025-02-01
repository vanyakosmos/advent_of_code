import enum
import sys
from pathlib import Path

from urllib.request import Request, urlopen


RUNNING_EXAMPLE = len(sys.argv) > 1
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def read_data(*examples) -> list[str]:
    if len(sys.argv) == 1:
        data = _load_input_data()
    else:
        index = int(sys.argv[-1]) - 1
        data = examples[index]
    return data.strip(" \n").splitlines()


def noop(*args, **kwargs):
    pass


def show_grid(grid: list[list[str]]):
    for row in grid:
        print(" ".join(row))
    print()


class Color(enum.StrEnum):
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    END = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def __call__(self, v):
        return f"{self}{v}{Color.END}"


def print_result(res) -> None:
    print("\n\nRESULT:", Color.YELLOW(res))


def _load_input_data() -> str:
    root = Path(__file__).parent
    script_path = Path(sys.argv[0])
    year = script_path.parent.parent.name
    day = script_path.parent.name

    cache_dir = root / ".cache"
    cache_file = cache_dir / f"{year}_{day}.txt"
    if cache_file.exists():
        return cache_file.read_text()

    req = Request(f"https://adventofcode.com/{year}/day/{day}/input")
    aoc_session = (root / ".session").read_text()
    req.add_header("Cookie", f"session={aoc_session}")
    response = urlopen(req)
    content = response.read().decode("utf-8")

    cache_dir.mkdir(exist_ok=True)
    cache_file.write_text(content)
    return content
