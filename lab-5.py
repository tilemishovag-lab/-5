contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]

def create(name, phone):
    new_contact = {'name': name, 'phone': phone}
    contacts.append(new_contact)
    print(f"Контакт '{name}' добавлен.")

def edit(name, new_phone):
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = new_phone
            print(f"Номер контакта '{name}' изменен на {new_phone}.")
            return
    print(f"Контакт '{name}' не найден.")

def delete(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"Контакт '{name}' удален.")
            return
    print(f"Контакт '{name}' не найден.")




ten = []
for i in range(1, 11):
    ten.append(i)

evens = []
for num in ten:
    if num % 2 == 0:
        evens.append(num)

squares = []
for num in evens:
    squares.append(num ** 2)

print("Список ten:", ten)
print("Список evens:", evens)
print("Квадраты чисел из evens:", squares)
print("-" * 50)

def get_by_index(lst=ten):
    while True:
        user_input = input("Введите индекс (или 'exit' для выхода): ")
        
        # Выход из бесконечного цикла
        if user_input.lower() == 'exit':
            print("Выход из программы.")
            break
            
        try:
            index = int(user_input)
            print(f"Элемент под индексом {index}: {lst[index]}")
            
        except ValueError:
            print("Ошибка: нужно ввести целое число или слово 'exit'!")
            
        except IndexError:
            # Границы актуальных индексов списка
            min_idx = -len(lst)
            max_idx = len(lst) - 1
            print(f"Ошибка: неверный индекс! Допустимые индексы для ввода: от {min_idx} до {max_idx}.")

get_by_index()