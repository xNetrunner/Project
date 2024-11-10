# bool - True и False

# == - проверка на равенство переменных
# != - проверка на неравенсто переменных

num1 = int(input('Введите число: ')) # 12

# and - И (*) or - ИЛИ (+)
usl1 = num1 > 10 and num1 % 2 == 0 and num1 < 20 # ...and... True and True and True -> 1 * 1 * 1 = 1 -> True
usl2 = num1 < 10 and num1 % 2 == 0 # ...and... True and False -> 1 * 0 = 0 -> False
print(usl1)
print(usl2)

num1 = int(input('Введите число: ')) # 50, 66
usl3 = num1 % 3 == 0 or num1 > 100 # False + False -> 0 + 0 = 0 -> False
usl4 = num1 % 3 == 0 or num1 > 100 # True + False -> 1 + 0 = 1 -> True
usl5 = num1 % 3 == 0 or num1 > 100 or num1 < 1000 and num1 % 2 == 0
print(usl3)
print(usl4)
print(usl5)

# if условие == True
#    действие 
# elif условие == True
#    действие
# else: действие

num1 = int(input('Введите число: '))

usl1 = num1 > 10 and num1 % 2 ==0
if usl1: # правда / usl1 == False - не правда
    print('Число больше 10 и четное')
elif num1 % 2 != 0:
    print('Число нечетное')
elif num1 == 8:
    print('Вы ввели 8')
else:
    print('Пока')

print('Конец')

usl1 = True
print(not(usl1)) # False
print(not(not(usl1))) # True

# num1, num2 [+,-,*,/,**]