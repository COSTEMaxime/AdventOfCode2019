def main():
    with open('input8.txt') as file:
        data = file.readlines()[0]

    widthPx = 25
    heightPx = 6
    layerSize = widthPx * heightPx
    layersCount = len(data) // layerSize

    # Part 1
    layers = [data[x * layerSize:(x + 1) * layerSize] for x in range(layersCount)]
    layer = (min(layers, key=lambda x: x.count('0')))
    print(layer.count('1') * layer.count('2'))

    # Part 2
    for x in range(layerSize):
        pixel = None
        for layer in reversed(layers):
            if layer[x] == '0':
                pixel = ' '
            elif layer[x] == '1':
                pixel = u'\u2591'

        if x % widthPx == 0:
            print()
        print(pixel, end='')


if _name_ == '_main_':
    main()