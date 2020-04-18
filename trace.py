import argparse

from Trace import Trace


def main():
    parser = argparse.ArgumentParser(description="Show trace")
    parser.add_argument("address", type=str, help="IP or domain name")
    args = parser.parse_args()
    tr = Trace(args.address)
    tr.print_trace()


if __name__ == "__main__":
    main()
