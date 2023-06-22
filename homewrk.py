import requests

#1
# def get_todo(todo_id):
#     url = f'https://jsonplaceholder.typicode.com/todos/{todo_id}'
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         todo = response.json()
#         return todo
#     else:
#         return None
#
# def write_todo(todo, json):
#     with open(json, "w") as file:
#         file.write(str(todo))
#
# todo_id = input("Введите номер todo: ")
# todo = get_todo(todo_id)
#
# if todo is not None:
#     json = f"{todo['id']}.json"
#     write_todo(todo, json)
#     print(f"Записан файл: {json}")
# else:
#     print("Не удалось загрузить todo.")



#2
# def plus_two(number):
#     try:
#         result = 2 + number
#         print(result)
#     except TypeError:
#         print("Ожидаемый тип данных — число!")
#
# plus_two(1)
# plus_two("12")

#3
# def access_array(array, index):
#     try:
#         element = array[index]
#         print("Элемент:", element)
#     except IndexError:
#         print("Индекс выходит за границы массива!")
#
#
# array = [1, 2, 3, 4, 5]
#
# access_array(array, 1)
# access_array(array, 7)



