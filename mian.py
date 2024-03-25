import os
# Функция, создающая кулинарную книгу.
def create_cook_book():
    with open('recipes.txt', encoding='utf-8') as imput_file:
        cook_book = {}
        dict_key = ''
        for line in imput_file:
            line = line.strip()
            if line.isdigit():
                continue
            elif line and '|' not in line:
                dict_key = line
                ingridients_list = []
            elif line and '|' in line:
                name, amount, units = line.split(" | ")
                ingridients_list.append(dict(ingredient_name=name, quantity=int(amount), measure=units))
                cook_book.setdefault(dict_key, ingridients_list)
    return cook_book
# Функция, собирающая список покупок.
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    new_cook_book = create_cook_book()
    new_dict = {}
    for dish in dishes:
        if dish in new_cook_book.keys():
            for ingredient in new_cook_book[dish]:
                multiply_ingridients = ingredient['quantity'] * person_count
                new_dict = dict({'measure':ingredient['measure'],'quantity':multiply_ingridients})
                shop_list.setdefault(ingredient['ingredient_name'], new_dict)
    print(shop_list)
print(create_cook_book())
get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 100)
# Работа с файлами, сортировка текста по количеству строк.
def sort_files():
    with open('1.txt','r', encoding= 'utf-8') as file_1, \
        open('2.txt','r', encoding= 'utf-8') as file_2, \
        open('3.txt','r', encoding= 'utf-8') as file_3:
        data_1 = file_1.readlines()
        data_2 = file_2.readlines()
        data_3 = file_3.readlines()
        all_text_list = [['\n' + file_1.name + '\n', str(len(data_1)) + '\n'] + data_1, ['\n' +file_2.name + '\n',str(len(data_2)) + '\n'] + data_2, ['\n' + file_3.name + '\n',str(len(data_3)) + '\n'] + data_3]
        sorted_text_list = sum(sorted(all_text_list, key=len, reverse = True), [])
        final_list = ''.join(sorted_text_list)
    return(final_list[1:-1])
# Запись в файл 'sorted.txt'
with open('sorted.txt','w', encoding= 'utf-8') as file_4:
    file_4.write(sort_files())
    