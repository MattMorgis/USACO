"""
ID: matthew142
LANG: PYTHON3
TASK: ride
"""
from functools import reduce
from string import ascii_uppercase


def get_names_from_input_file(file):
    with open(file, 'r') as input_file:
        group_name, comet_name = [line.strip().upper()
                                  for line in input_file.readlines()]
    return group_name, comet_name


def get_chars_for_name(name):
    return list(name)


def map_chars_to_ints(chars):
    return [list(ascii_uppercase).index(
        char) + 1 for char in chars]


def multiply_ints(ints):
    return reduce((lambda x, y: x * y), ints)


def main():
    input_file = 'ride.in'

    group_name, comet_name = get_names_from_input_file(input_file)

    group_chars = get_chars_for_name(group_name)
    comet_chars = get_chars_for_name(comet_name)

    group_ints = map_chars_to_ints(group_chars)
    comet_ints = map_chars_to_ints(comet_chars)

    group_product = multiply_ints(group_ints)
    comet_product = multiply_ints(comet_ints)

    group_mod = group_product % 47
    comet_mod = comet_product % 47

    return 'GO' if group_mod == comet_mod else 'STAY'


with open('ride.out', 'w') as output_file:
    output_file.write(main()+'\n')
