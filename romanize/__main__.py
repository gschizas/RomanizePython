# -*- coding: utf-8 -*-
from __future__ import print_function
from romanize import romanize


def main():
    import sys

    if len(sys.argv) > 1:
        print(romanize(' '.join(sys.argv[1:])))
    else:
        words = sys.stdin.read()
        print(romanize(words))


if __name__ == "__main__":
    main()
