from typing import List

def process_battery(battery_line: str) -> List[int]:
    res = []
    for i in battery_line:
        res.append(int(i))
    return res

def max_voltage(d: List[int]) -> int:
    r = 0
    for i in range(len(d)):
        n = d[i] * 10
        for j in range(i+1, len(d)):
            r = max(r, n + d[j])
    return r

if __name__ == '__main__':
    with open('./input.txt', 'r+') as f:
        batteries = f.read()

    sum = 0
    for bat in batteries.split('\n'):
        data = process_battery(bat.strip())
        sum += max_voltage(data)
    print(sum)