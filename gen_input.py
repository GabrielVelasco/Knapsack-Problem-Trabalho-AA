import random

def gen_input_size(n):
    # given size 'n', generate 'weights' and 'values' arrays with 'n' items (random)

    # where
    # 2 <= weight[i] <= 50
    # 2 <= value[i] <= 50

    weights = []
    values = []

    for i in range(n):
        randomWeight = random.randint(2, 50)
        weights.append(randomWeight)

        randomValue = random.randint(2, 50)
        values.append(randomValue)

    with open('input.txt', 'w') as file:
        print("weights = ", weights, file=file)
        print("values = ", values, file=file)