import math

def main():
    reactions = {
        'ORE': {'available': 0}
    }
    with open('input14.txt') as file:
        for line in file.readlines():
            input_, output_ = line.strip().split(' => ')

            reactions[output_.split(' ')[1]] = {
                'input': [[int(x.split(' ')[0]), x.split(' ')[1]] for x in input_.split(', ')],
                'output': [int(output_.split(' ')[0]), output_.split(' ')[1]],
                'available': 0
            }

    print(getOreCount(reactions.copy(), 'FUEL'))

    oreCount = 1000000000000
    fuelCount = 0

    while True:
        oreCount -= getOreCount(reactions, 'FUEL')
        if fuelCount % 10000 == 0:
            print(fuelCount)
        if oreCount < 0:
            break
        fuelCount += 1
    
    print(fuelCount - 1)

def getOreCount(reactions, desiredOutput):
    count = 0
    for input_ in reactions[desiredOutput]['input']:
        while(reactions[input_[1]]['available'] < input_[0]):
            if input_[1] == 'ORE':
                return input_[0]
            else:
                count += getOreCount(reactions, input_[1])
                reactions[input_[1]]['available'] += reactions[input_[1]]['output'][0]

        reactions[input_[1]]['available'] -= input_[0]

    return count

if __name__ == "__main__":
    main()