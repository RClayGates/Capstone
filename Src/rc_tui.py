# imports: std
import os
import sys
from time import perf_counter
# imports: non-std
from rc_logger import src_log

# const
ANSI_ESCAPE = '\x1b'
CONSEQINTRO = ANSI_ESCAPE + '['
CURSOR_HOME = CONSEQINTRO + 'H'
CLEARCUREND = CONSEQINTRO + '0J'
CLEARCURBEG = CONSEQINTRO + '1J'
CLEARSCREEN = CONSEQINTRO + '2J'
CLEARSCRHIS = CONSEQINTRO + '3J'

# main


def main():
    pass

# code blocks


def cursor_posxy(x: int, y: int) -> None:
    sys.stdout.write(CONSEQINTRO + str(y) + ';' + str(x) + 'H')  # or f


def reset_screen() -> None:
    sys.stdout.write(CLEARSCRHIS + CLEARSCREEN + CURSOR_HOME + '\r')


def clear_screen() -> None:
    sys.stdout.write(CONSEQINTRO + '2J')


if __name__ == "__main__":
    start = perf_counter()
    os.chdir(os.path.dirname(__file__))
    main()
    print(f"Program Time= {perf_counter() - start:.2f}")
