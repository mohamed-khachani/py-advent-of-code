
from typing import List

def process_battery(battery_line: str) -> List[int]:
    res = []
    for i in battery_line:
        res.append(int(i))
    return res

def max_voltage(d: List[int]) -> int:
    r = 0
    start = 0
    k = 12

    for i in range(k):
        end = len(d) - (k - i) + 1

        maximum = max(d[start:end])
        index = d.index(maximum, start, end)

        r = r * 10 + maximum
        start = index + 1

    return r

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        batteries = f.read()

    total = 0
    for bat in batteries.splitlines():
        if not bat.strip():
            continue

        data = process_battery(bat.strip())
        total += max_voltage(data)

    print(total)
