
queries = [
    'ffff',
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'курс доллара3',
    'курс доллара2',
    'курс доллара1',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
#считаем  количество  слов в кажом запросе и создаем словарь где  запрос является ключем и  количество слов в нем значением
queries_dict = {}
for temp in queries:
    queries_dict[temp] = len(temp.split())
#print(queries_dict)

# считаем  общее количество запроосов и создем ещё один словарь с ключем количество слов и  значением количество запросов
proportion100=0
count_queries_dict = {}
for queries_dict_key, queries_dict_value in queries_dict.items():
    proportion100 = proportion100 + 1
    if queries_dict_value in count_queries_dict:
        count_queries_dict[queries_dict_value] = count_queries_dict[queries_dict_value]+1
    else:
        count_queries_dict[queries_dict_value] = 1
#print(count_queries_dict)
#print(proportion100)

proportion = 0
for count_queries_key, count_queries_value in count_queries_dict.items():
    proportion = count_queries_value*100/proportion100
    print(f"Колличество слов в запросе {count_queries_key} процентная составляющая {round(proportion,3)} %")








