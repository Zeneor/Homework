n = [num for num in range(1001)]
sq = [num ** 2 for num in n]

print(n)
print(sq)



username = input('Введите логин: ')
password = input('Введите пароль: ')

if username == 'user' and password == 'qwerty':
    print('Authentication completed')
else:
    print('Invalid login or password')



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