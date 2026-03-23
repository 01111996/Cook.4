# Задание 1 (только открываю файл, в котором уже есть меню и кол-во ингр., добавила функцию with)
f = open('cook.txt')
print(type(f))
cook_book = {}
with open('cook.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish not in cook:
            continue
        for ingredient in cook[dish]:
            name = ingredients['ingredients_name']
            amount = ingredients['quantity'] * persons
            pieces = ingredients['pieces']
            if name in shop_list:
                shop_list[name]['quantity'] += amount
            else:
                shop_list[name] = {
                    'pieces': pieces,
                    'quantity': amount
                }
    return shop_list

    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задание 3 
file_names = ['1.txt', '2.txt']
files_data = []
for file_name in file_names:
    with open(file_name, 'r') as f:
        lines = f.readlines()
    files_data.append((file_name, lines))
files_data.sort(key=lambda x: len(x[1]))
with open('result.txt', 'w') as result:
    for file_name, lines in files_data:
        result.write(file_name + '\n')
        result.write(str(len(lines)) + '\n')
        result.writelines(lines)
        if lines and not lines[-1].endswith('\n'):
            result.write('\n')
