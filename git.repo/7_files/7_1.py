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


#pprint(read_book())


def get_shop_list_by_dishes(dishes, person_count):
    fin_dish = {}
    result_dish = {}
    book = read_book()

    for dish in dishes:
        if dish in book:
            #print(dish)
            temp_name_dish = {}
            for each_ind in book[dish]:
                print("sssss",each_ind)


                if each_ind["ingredient_name"] in temp_name_dish.keys():
                    fin_dish['ingredient_name'] = each_ind["ingredient_name"]
                    #print(each_ind["ingredient_name"])
                    print(each_ind["quantity"])
                    print(fin_dish['quantity'])
                    fin_dish['quantity'] = int(fin_dish['quantity'])+int(each_ind["quantity"])
                    print(fin_dish['quantity'])
                    fin_dish['measure'] = each_ind["measure"]
                else:
                    temp_name_dish[each_ind["ingredient_name"]] = 56787867
                    fin_dish['ingredient_name'] = each_ind["ingredient_name"]
                    fin_dish['quantity'] = each_ind["quantity"]
                    fin_dish['measure'] = each_ind["measure"]
                result_dish[fin_dish['ingredient_name']] = {'measure':fin_dish['measure'], 'quantity': int(fin_dish['quantity'])*person_count }
        #print(temp_name_dish)
        #print(fin_dish)
        else:
            print(f"net dishes{dish}")
    pprint(result_dish)

#dishes_list = ["Омлет", "Фахитос"]
#dishes_list = ['Запеченный картофель', 'Омлет']

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2)
get_shop_list_by_dishes(["Омлет", "Фахитос"],3)
