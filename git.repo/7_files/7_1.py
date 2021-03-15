from pprint import pprint


def read_book(file='recipes.txt'):
    from pprint import pprint

    with open(file, mode="r", encoding='UTF-8') as f:
        data = f.read().splitlines()

    cool_book = {}
    i = 0
    test = []
    while i <= len(data):
        step = int(data[i + 1])
        cur_list_ind = []
        for each in range(i + 2, i + step + 2):
            dict_ind = {}
            ind = data[each].split('|')
            dict_ind['ingredient_name'] = ind[0]
            dict_ind['quantity'] = ind[1]
            dict_ind['measure'] = ind[2]
            cur_list_ind.append(dict_ind)
        cool_book[data[i]] = cur_list_ind
        i = i + 3 + step

    return cool_book


pprint(read_book())


def get_shop_list_by_dishes(dishes, person_count):
    result_dish = {}
    book = read_book()
    for dish in dishes:
        if dish in book:
            for each_ind in book[dish]:
                if each_ind['ingredient_name'] in result_dish:
                    temp_quantity =result_dish[each_ind['ingredient_name']]['quantity']
                    result_dish[each_ind['ingredient_name']] ={'measure':each_ind['measure'],'quantity':(int(each_ind['quantity'])*int(person_count))+int(temp_quantity) }
                else:
                    result_dish[each_ind['ingredient_name']] = {'measure': each_ind['measure'],
                                                             'quantity': int(each_ind['quantity'])*int(person_count)}
    pprint(result_dish)




get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2)
#get_shop_list_by_dishes(["Омлет", 'Фахитос'], 3)
