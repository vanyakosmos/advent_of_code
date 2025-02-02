import importlib
from pathlib import Path

from utils.loading import YEAR_DAY


def main():
    root = Path(__file__).parent
    scrips = root.glob("????/??/?.py")
    last: Path = sorted(scrips)[-1]
    year = last.parent.parent.name
    day = last.parent.name
    part = last.stem
    module = importlib.import_module(f"{year}.{day}.{part}")
    YEAR_DAY.set((year, day))
    module.main()


if __name__ == "__main__":
    main()
