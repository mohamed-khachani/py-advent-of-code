from typing import List, Tuple
from copy import copy

def build_arr(inp: str) -> Tuple[List[int], int]:
    n = inp.index('\n')
    string = inp.replace('\n', '')
    arr = []
    for s in string:
        if s == '@':
            arr.append(1)
        elif s == '.':
            arr.append(0)
    return arr, n


def adjacents(arr: List[int], ident: int, n: int) -> bool:
    i = ident // n
    j = ident % n

    if arr[ident] == 0:
        return 0

    rows = len(arr) // n
    count = 0

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue

            new_i = i + x
            new_j = j + y

            if 0 <= new_i < rows and 0 <= new_j < n:
                count += arr[n * new_i + new_j]

    return count < 4

if __name__ == '__main__':
    with open('./input.txt', 'r+') as f:
        inp = f.read()

    arr, n = build_arr(inp)

    suma = 0
    nuevos = 0
    cont = True

    while cont:
        new_arr = []
        suma_local = 0
        for el in range(0, len(arr)):
            res = adjacents(arr, el, n)
            suma_local += res
            new_arr.append(0 if res else arr[el])

        cont = suma_local > 0
        suma += suma_local
        arr = new_arr

    print(suma)