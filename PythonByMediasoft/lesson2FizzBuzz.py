# Дискрипшн.
# Условия задачи:
# вывод на экран чисел от 1 до 100(включительно);
# при num % 3 == 0 выводит слово Fizz;
# при num % 5 == 0 выводит слово Buzz;
# при num % 3 == 0 and num % 5 == 0 выводит FizzBuzz;
# Можно выполнить при помощи print - самый короткий способ решения:
# print('1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz')


# расчет с заранее известным числом 100:
for num100 in range(1, 101):
    if num100 % 3 == 0 and num100 % 5 == 0:
        print('FizzBuzz')
    elif num100 % 3 == 0:
        print('Fizz')
    elif num100 % 5 == 0:
        print('Buzz')
    else:
        print(num100)


# Но, если в дальнейшем пользователь захочет посмотреть сам другие числа, например до 1 000
# try:
#     num = int(input('Введите натуральное, не дробное число до 1 000 включительно\n'))
#     for num_in_string in range(1, num + 1):
#         if num < 1: # ограничение на Бигинт (-бесконечность)
#             print('Вы напечатали число меньше 1, поэтому программа считать не будет :)\nПопробуйте ещё раз!')
#             break
#         elif num > 1000: # ограничение на Бигинт (+бесконечность)
#             print('Вы напечатали число больше 1 000! \nПопробуйте ещё раз!')
#             break
#         elif num_in_string % 3 == 0 and num_in_string % 5 == 0:
#             print('FizzBuzz')
#         elif num_in_string % 3 == 0:
#             print('Fizz')
#         elif num_in_string % 5 == 0:
#             print('Buzz')
#         else:
#             print(num_in_string)
#
# except ValueError:
#     print('Это число с плавающей запятой! Попробуйте, еще раз!')
