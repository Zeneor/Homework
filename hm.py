#Homework 5
#1
input_str = input("Введите три целых числа через пробел: ")

numbers = input_str.split()
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

if a + b > c and a + c > b and b + c > a:
    result = True
else:
    result = False

print(result)

#2
a = int(input('Введите число: '))

if a / 2:
    result = True
else:
    result = False

print(result)

#3
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

if a + b > c:
    result = True
else:
    result = False

print(result)

#4
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

if a > b:
    print(True)
else:
    print(False)




#Homework 4
#1
n = [num for num in range(1001)]
sq = [num ** 2 for num in n]

print(n)
print(sq)

#2
username = input('Введите логин: ')
password = input('Введите пароль: ')

if username == 'user' and password == 'qwerty':
    print('Authentication completed')
else:
    print('Invalid login or password')

#3
a = float(input("Insert amount in KZT: "))
print("Choose currency:")
print("[1] USD")
print("[2] EUR")
print("[3] RUB")
currency_choice = int(input())

if currency_choice == 1:
    converted_amount = a / 420
    currency_name = "USD"
elif currency_choice == 2:
    converted_amount = a / 510
    currency_name = "EUR"
elif currency_choice == 3:
    converted_amount = a / 5.8
    currency_name = "RUB"
else:
    print("Invalid currency choice")

print(f"{converted_amount:.2f} {currency_name}")