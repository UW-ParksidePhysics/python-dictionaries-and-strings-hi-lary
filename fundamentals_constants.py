# exercise 6.1

def read_data(filename):
    infile = open(filename, 'r').readlines()[2:-1]
    constants = {}
    for line in infile:
        words = line.split()
        constant = float(words[-2])
        if len(words[:-2]) == 3:
            object = words[0] + ' ' + words[1] + ' ' + words[2]
        elif len(words[:-2]) == 2:
            object = words[0] + ' ' + words[1]
        else:
            object = words[0]
        constants[object] = constant
    return constants


constants = read_data('constants.txt')
for object, constant in constants.items():
    print(f'{object}, {constant}')
