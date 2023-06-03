#1
def celebrate1(s, p, m):
    if s + p < m:
        print('Да')
    else:
        print('Нет')

s = float(input("Стоимость подписки: "))
p = float(input("Стоимость пиццы: "))
m = float(input("Зарплата Васи: "))

celebrate1()


#2
def celebrate2(sub, pizza, salary):
    if sub + pizza <= salary:
        return "Да"
    else:
        return "Нет"

sub = float(input("Стоимость подписки: "))
pizza = float(input("Стоимость пиццы: "))
salary = float(input("Зарплата Васи: "))

result = celebrate2(sub, pizza, salary)
print(result)


#3
def celebrate3(s, p, m):
    return s + p <= m

subs = float(input("Стоимость подписки: "))
pizzaa = float(input("Стоимость пиццы: "))
vasya_salary = float(input("Зарплата Васи: "))

result = celebrate3(subs, pizzaa, vasya_salary)

if result:
    print("Да")
else:
    print("Нет")