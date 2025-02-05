import contextvars
import sys
from pathlib import Path
from urllib.request import Request, urlopen

YEAR_DAY = contextvars.ContextVar("year,day")
RUNNING_EXAMPLE = len(sys.argv) > 1


def read_data(*examples) -> list[str]:
    if len(sys.argv) == 1:
        data = _load_input_data()
    else:
        index = int(sys.argv[-1]) - 1
        data = examples[index]
    lines = data.strip(" \n").splitlines()
    print(f"input length: {len(lines)}\n")
    return lines


def split_lines(lines: list[str]):
    buff = []
    for line in lines:
        if line:
            buff.append(line)
        else:
            yield buff
            buff = []
    yield buff


def _get_meta() -> tuple[str, str]:
    if YEAR_DAY.get(None):
        return YEAR_DAY.get()
    else:
        script_path = Path(sys.argv[0])
        year = script_path.parent.parent.name
        day = script_path.parent.name
        return year, day


def _load_input_data() -> str:
    root = Path(__file__).parent.parent
    year, day = _get_meta()

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
