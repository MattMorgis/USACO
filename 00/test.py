"""
ID: matthew142
LANG: PYTHON3
TASK: test
"""

inputFile = open('test.in', 'r')
outputFile = open('test.out', 'w')

x, y = map(int, inputFile.readline().split())
sum = x + y

outputFile.write(str(sum) + '\n')
outputFile.close()
