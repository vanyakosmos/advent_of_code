import enum

from .loading import RUNNING_EXAMPLE


def noop(*args, **kwargs):
    pass


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


def print_result(res, expected=None) -> None:
    print("\n")
    if expected is not None and RUNNING_EXAMPLE:
        print(Color.GREEN("PASS") if res == expected else Color.RED("FAIL"))
        print(f"expected: {Color.YELLOW(expected)}, actual: {Color.YELLOW(res)}")
    else:
        print("result:", Color.YELLOW(res))
