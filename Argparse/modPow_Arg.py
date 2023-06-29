import argparse
import logging
import math


logging.basicConfig(filename='mod.log'
                    , filemode='w'
                    , format='%(filename)s:%(message)s')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Using the MOD function')

    parser.add_argument('--num1'
                        , type=int
                        , metavar='N1'
                        , help='First Input')

    parser.add_argument('--num2'
                        , type=int
                        , metavar='N2'
                        , help='Second Input')

    parser.add_argument('--num3'
                        , type=int
                        , metavar='N3'
                        , help='Third Input')

    args = parser.parse_args()

    try:
        print(pow(args.num1, args.num2))
        print(pow(args.num1, args.num2, args.num3))

    except RuntimeError:
        print('Error')