from typing import List

def suma(data: List[int]):
    total = 0
    for d in data:
        total += d
    return total

def multiply(data: List[int]):
    total = 1
    for d in data:
        total *= d
    return total


if __name__ == '__main__':
#     entrada = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """

    entrada = open('./input.txt', 'r').read().rstrip('\n')

    lines = entrada.split('\n')

    width = max(len(line) for line in lines)
    lines = [line.ljust(width) for line in lines]

    matrix = []
    numbers = []

    for j in range(width - 1, -1, -1):

        number = ''
        for i in range(len(lines) - 1):
            if lines[i][j] != ' ':
                number += lines[i][j]

        if number != '':
            numbers.append(int(number))

        else:
            if numbers:
                matrix.append(numbers)
                numbers = []

    if numbers:
        matrix.append(numbers)

    ops = lines[-1].split()
    ops.reverse()

    res = 0

    for i, op in enumerate(ops):
        if op == '+':
            res += suma(matrix[i])
        elif op == '*':
            res += multiply(matrix[i])

    print(matrix)
    print(res)
