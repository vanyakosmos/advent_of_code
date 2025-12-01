import runpy
from pathlib import Path

from utils.loading import YEAR_DAY


def main():
    root = Path(__file__).parent
    scrips = root.glob("????/??/?.py")
    last: Path = sorted(scrips)[-1]
    year = last.parent.parent.name
    day = last.parent.name
    part = last.stem
    YEAR_DAY.set((year, day))
    runpy.run_path(f"{year}/{day}/{part}.py", run_name="__main__")


if __name__ == "__main__":
    main()
