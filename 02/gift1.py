"""
ID: matthew142
LANG: PYTHON3
TASK: gift1
"""


def main():
    with open('gift1.in', 'r') as input_file:
        lines = [line.strip() for line in input_file.readlines()]
    return ''.join(lines)


with open('gift1.out', 'w') as output_file:
    output_file.write(main()+'\n')
