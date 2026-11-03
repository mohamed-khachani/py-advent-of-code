from typing import List

def suma(data: List[int]):
    sum = 0
    for d in data:
        sum += d
    return sum

def multiply(data: List[int]):
    sum = 1
    for d in data:
        sum *= d
    return sum

if __name__ == '__main__':
#     entrada = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   + """
    entrada = open('./input.txt', 'r+').read().strip()

    lines = entrada.split('\n')

    matrix = []
    for i, line in enumerate(lines):
        if i == len(lines)-1:
            continue

        raw = ' '.join(line.strip().split()).split(' ')
        print('raw', raw)

        if len(matrix) == 0:
            matrix = [ [ ] for _ in range(0, len(raw)) ]

        for j in range(0, len(raw)):
            matrix[j].append(int(raw[j]))
        

    ops = ' '.join(lines[-1].strip().split()).split(' ')
    res = 0

    print(matrix)

    for i, op in enumerate(ops):
        if op == '+':
            res += suma(matrix[i])
        elif op == '*':
            res += multiply(matrix[i])
    

    print(res)