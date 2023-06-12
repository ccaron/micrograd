import sys
from micrograd import Value
from utils import render

def main() -> int:
    a = Value(1.0, label='a')
    c = a + 3.1 + Value(5.5, label='d')
    render(c)
    return 0

if __name__ == '__main__':
    sys.exit(main())
