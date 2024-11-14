
result = 5 + 10 # сложение
result2 = 10 -5 # вычитание
result3 = 5 * 5 # умножение
result4 = 5 / 2 # деление вернет float
print(result4, type(result4))
result5 = 5 // 2 # деление вернет int - целое число
print(result5, type(result5))
result6 = 5 % 2 # деление вернет int - остаток
print(result6, type(result6))
result7 = 5 ** 3 # возведение в степень
print(result7, type(result7))

num1 = -142
print(abs(num1))
#abs_num = abs(num1)
#print(abs_num)

num1 = "Hello"
print(num1)
num1 = False
print(num1)

# str - str() float - float() int - int()
num2 = 25
num2 = str(num2) # '25'
num3 = float(num2)
print(num2, type(num2))
print(num3, type(num3))

num4 = int(input('Ведите число 1: '))
num5 = int(input('Ведите число 2: '))
print(num4 + num5, "Сложили числа")