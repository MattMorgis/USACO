"""
ID: matthew142
LANG: PYTHON3
TASK: ride
"""


def main():
    input_file = open('ride.in', 'r')
    output_file = open('ride.out', 'w')

    group_name, comet_name = [line.strip() for line in input_file.readlines()]

    return group_name, comet_name


main()
