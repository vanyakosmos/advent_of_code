import sys
from pathlib import Path

from urllib.request import Request, urlopen


def read_data(full: int) -> list[str]:
    if full:
        data = _load_input_data()
    else:
        example_path = Path(__file__).parent / "example.txt"
        data = example_path.read_text()
    return data.splitlines()


def noop(*args, **kwargs):
    pass


def print_result(res) -> None:
    print("\n\nRESULT:", res)


def _load_input_data() -> str:
    root = Path(__file__).parent
    script_path = Path(sys.argv[0])
    year = script_path.parent.name
    day = script_path.stem.split("_")[1]

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
