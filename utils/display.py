import enum
import warnings


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


def print_result(res) -> None:
    warnings.warn(f"Deprecated in favor of `check_result`", DeprecationWarning)
    check_result(res)


def check_result(actual, expected=None):
    print()
    if expected is None or actual == expected:
        print(Color.GREEN("PASS"))
        print("result:", Color.YELLOW(actual))
        print("\n" + "= " * 33 + "\n")
    else:
        print(Color.RED("FAIL"))
        print(f"expected: {Color.YELLOW(expected)}, actual: {Color.YELLOW(actual)}")
        raise SystemExit(1)
