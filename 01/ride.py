"""
ID: matthew142
LANG: PYTHON3
TASK: ride
"""


def main():
    with open('ride.in', 'r') as input_file:
        group_name, comet_name = [line.strip()
                                  for line in input_file.readlines()]

    return group_name, comet_name


main()
