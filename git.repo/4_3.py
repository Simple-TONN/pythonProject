
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'ffff'
]
#считаем  количество  слов в кажом запросе и создаем словарь где  запрос является ключем и  количество слов в нем значением
queries_dict = {}
for temp in queries:
    queries_dict[temp] = len(temp.split())
print(queries_dict)

# считаем  общее количество запроосов и создем ещё один словарь с ключем количество слов и  значением количество запросов
proportion100=0
temp2 = {}
for queries_dict_key, queries_dict_value in queries_dict.items():
    proportion100 = proportion100 + queries_dict_value
    if queries_dict_key in temp2:
        temp2[queries_dict_value] = temp2[queries_dict_value]+1
    else:
        temp2[queries_dict_value] = 1

print(temp2)
print_list = []
sum_proporcia100=0
for count_queries,s_proporcia in temp2.items():
    proportion100 = proportion100+ s_proporcia
    print_list.append(f"")

print(sum_proporcia100)
print((proportion100))

