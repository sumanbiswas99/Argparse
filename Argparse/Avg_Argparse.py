import argparse

# Initializing Parser
parser = argparse.ArgumentParser()

# Adding Arguments
parser.add_argument('integers',
                    type=float,
                    metavar='N',
                    nargs='+',
                    help='an list of integer for the accumulator')

parser.add_argument('sum',
                    action='store_const',
                    const=sum
                    )

parser.add_argument('len',
                    action='store_const',
                    const=len)


args = parser.parse_args()

add = args.sum(args.integers)
length = args.len(args.integers)
avg = add / length
print(avg)