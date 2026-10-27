def convert_opration(op: str):
    return int(op[1:]) *  (-1 if op.startswith('L') else 1)

def operate(current: int, operation: str):
    return (current + convert_opration(operation)) % 100

if __name__ == '__main__':
    with open('./input.txt', 'r+') as f:
        operations = f.readlines()
    current = 50
    zeroes = 0
    for operation in operations:
        current = operate(current, operation)
        if current == 0:
            zeroes += 1
    print(zeroes)
