"""
ID: matthew142
LANG: PYTHON3
TASK: gift1
"""


def main():
    with open('gift1.in', 'r') as input_file:
        lines = [line.strip() for line in input_file.readlines()]

    number_of_people = int(lines[0])

    people = lines[1:number_of_people+1]

    transactions = lines[number_of_people+1:]

    ledger = [{'name': person, 'amount': 0} for person in people]

    return ledger


with open('gift1.out', 'w') as output_file:
    output_file.write(str(main())+'\n')
