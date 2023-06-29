import argparse
import cmath
import logging


logging.basicConfig(filename='Math_1.log'
                    , filemode='w'
                    , format='%(filename)s:%(message)s')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Conversion of Complex number to Polar')
    parser.add_argument('Complex_Num'
                        , type=complex)

    args = parser.parse_args()

    try:
        num = complex(args.Complex_Num)
        r, a = cmath.polar(num)
        print(r, a, sep='\n')
        logging.info(r, a)

    except TypeError:
        print("Error")
        

