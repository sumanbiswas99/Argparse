import argparse
import sys


def calc(args):

    if args.year % 400 == 0:
        return "Leap Year"

    elif args.year % 100 == 0:
        return "Not a Leap Year"

    elif args.year % 4 == 0:
        return "Leap Year"

    else:
        return "Not a leap Year"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="To check whether the year is Leap year or not")

    parser.add_argument('--year'
                        , type=int
                        , metavar='Y'
                        , help='Input Year')

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))