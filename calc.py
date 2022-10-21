def operation(f, s, opt):
    while True:
        if opt == '+':
            res = f+s
            print(f'{f}{opt}{s} = {res}')
            return res
            

        if opt == '-':
            res = f-s
            print(f'{f}{opt}{s} = {res}')
            return res
            

        if opt == '*':
            res = f*s
            print(f'{f}{opt}{s} = {res}')
            return res
            

        if opt == '/':
            res = f/s
            print(f'{f}{opt}{s} = {res}')
            return res
            

        if opt == '//':
            res = f//s
            print(f'{f}{opt}{s} = {res}')
            return res
            

        if opt == '%' or opt == 'mod':
            res = f%s
            print(f'{f}{opt}{s} = {res}')
            return res
            

        if opt == '**':
            res = f**s
            print(f'{f}{opt}{s} = {res}')
            return res
            

        else:
            print("Operation is not listed!")
            opt = input("Enter a valid operation: ")



f = int(input("Enter the first number: "))

while True:
    s = input("Enter the other number (type the letter \"s\" to stop): ")
    if s == 's':
        print("Done")
        break
    s = int(s)
    opt = input("Type in the operation(+, -, *, /, //, %, mod, **): ")
    f = operation(f, s, opt)

        

