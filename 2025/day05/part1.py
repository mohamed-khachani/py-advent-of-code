
def check(ranges: list[tuple[int, int]], val: int) -> bool:
    return any(start <= val <= end for start, end in ranges)


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        ranges_input, values_input = f.read().strip().split('\n\n')

    ranges = [
        tuple(map(int, line.split('-')))
        for line in ranges_input.splitlines()
    ]

    values = [
        int(line)
        for line in values_input.splitlines()
    ]

    suma = sum(check(ranges, val) for val in values)

    print(suma)
