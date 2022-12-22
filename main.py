from compiler.compiler import *

if __name__ == "__main__":
    file = open('code.txt', 'r')
    input_expression = file.read()

    res, error = run(input_expression)

    if error:
        print(error)
    else:
        if res:
            print(res)
        else:
            print('Build successful.')
