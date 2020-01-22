import random


def generate_code(length):
    code = ''
    for i in range(length):
        code += str(random.randint(0, 9))
    return code
