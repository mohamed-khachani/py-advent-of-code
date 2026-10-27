from typing import List

def handle_range(start: int, end: int) -> List[int]:
    suma = 0
    for i in range(start, end+1):
        string = str(i)
        if len(string) % 2 != 0:
            continue

        if string[:len(string)//2] == string[len(string)//2:]:
            suma += i

    return suma


if __name__ == '__main__':
#     inp = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124""".replace('\n', '')
#     ranges = inp.split(',')
    with open('./input.txt', 'r+') as f:
        ranges = f.read().replace('\n', '').split(',')

    suma = 0
    for ran in ranges:
        nums = ran.split('-')
        suma += handle_range(int(nums[0]), int(nums[1]))
    print(suma)
