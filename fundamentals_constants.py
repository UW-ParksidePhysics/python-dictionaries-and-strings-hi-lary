# exercise 6.1
# helppppp

def read_data(filename):
    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()
    constants = {}
    for line in lines:
        words = line.split()
        if line == lines[0] or line == lines[1]:
            pass

        elif len(words[:-1]) == 3:
            constant = float(words[1])
            object = words[0] + ' ' + words[2]
        elif len(words[:-1]) == 2:
            constant = float(words[1])
            object = words[0] + ' ' + words[1]
        else:
            constant = float(words[1])
            object = words[0]

        constants[object] = constant
    infile.close()
    return constants


constants = read_data('constants.txt')
