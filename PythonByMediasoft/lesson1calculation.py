firstNumber = int(input('Введи первое число '))
lastNumber = int(input('Введи ещё одно число '))
operation = (input('Операция над числами '))
result = 0
if operation == '+':
    result = firstNumber + lastNumber
    print(f'Вы сложили числа. Результат вычислений: {result}')

elif operation == '-':
    result = firstNumber - lastNumber
    print(f'Вы нашли разность чисел. Результат вычислений: {result}')
elif operation == '*':
    result = firstNumber * lastNumber
    print(f'Вы нашли умножение чисел. Результат вычислений: {result}')
elif operation == '/' and lastNumber != 0:
    result = firstNumber / lastNumber
    print(f'Вы нашли деление чисел. Результат вычислений: {result}')
elif operation == '/' and lastNumber == 0:
     print('Деление на 0 невозможно')
elif operation == '%':
    result = firstNumber % lastNumber
    print(f'Вы нашли остаток от деления. Результат вычислений: {result}')
elif operation == '**':
    result = firstNumber ** lastNumber
    print(f'Вы нашли результ возведения в степень. Результат вычислений: {result}')
else:
    print('Вы что то ввели неправильно :) Повторите')
