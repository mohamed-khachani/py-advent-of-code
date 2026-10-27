from typing import Tuple

def convert_opration(op: str) -> int:
    return int(op[1:]) *  (-1 if op.startswith('L') else 1)

def operate(current: int, operation: str) -> Tuple[int, int]:
    movement = convert_opration(operation)
    new_current = (current + movement) % 100

    if movement > 0:
        zeroes = (current + movement) // 100
    else:
        zeroes = (movement * -1 + (100 - current) % 100) // 100

    return new_current, zeroes

if __name__ == '__main__':
    with open('./input.txt', 'r+') as f:
        operations = f.readlines()
    # operations = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    current = 50
    zeroes = 0
    for operation in operations:
        current, addition = operate(current, operation)
        zeroes += addition
    print(zeroes)
