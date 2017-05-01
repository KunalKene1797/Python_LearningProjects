print('What is your Name?')
name = input()
print('How many times would you like to Calculate?')
e = int(input())
count = 0
while count < e:
    count += 1
    print('Hello!', name, 'What operation would you like to perform?')
    print('1 -> Addition')
    print('2 -> Subtraction')
    print('3 -> Multiplication')
    print('4 -> Division')
    c = int(input())
    if c == 1:
        print('Please enter 2 number')
        num1 = float(input())
        num2 = float(input())
        num = (num1 + num2)
        print('the solution is', num)
    if c == 2:
        print('Please enter 2 number')
        num1 = float(input())
        num2 = float(input())
        num = (num1 - num2)
        print('the solution is', num)
    if c == 3:
        print('Please enter 2 number')
        num1 = float(input())
        num2 = float(input())
        num = (num1 * num2)
        print('the solution is', num)
    if c == 4:
        print('Please enter 2 number')
        num1 = float(input())
        num2 = float(input())
        num = (num1 / num2)
        print('the solution is', num)
print('Press Any Key To Kill The Program')
input()

