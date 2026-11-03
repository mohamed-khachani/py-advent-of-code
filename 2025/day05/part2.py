
if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        ranges_input = f.read().strip().split('\n\n')[0]

    ranges = []

    for rn in ranges_input.split('\n'):
        start, end = map(int, rn.split('-'))
        ranges.append((start, end))

    ranges.sort()

    suma = 0
    last_end = -1

    for start, end in ranges:
        if start > last_end:
            suma += end - start + 1
        elif end > last_end:
            suma += end - last_end

        last_end = max(last_end, end)

    print(suma)
