Number1 = int(input('Ведіть 1 число : '))
Number2 = int(input('Ведіть 2 число : '))

action = int(input('Яку операцію ви хочете виконати? \n 1 + \n 2 - \n 3 / \n 4 * \n'))

if action == 1:
    r = Number1 + Number2
    Plus = '+'
    t = Plus
if action == 2:
    r = Number1 - Number2
    Minus = '-'
    t = Minus
if action == 3:
    r = float(Number1 / Number2)
    Division = '/'
    t = Division
if action == 4:
    r = Number1 * Number2
    Multiplication = '*'
    t = Multiplication
print ('Результат : = ',r)
