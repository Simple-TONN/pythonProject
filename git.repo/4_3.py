
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
temp_dict = {}
for temp in queries:
    temp_dict[temp] = len(temp.split())
print(temp_dict)

temp2 = {}
for temp_count_queries in temp_dict.values():
    if temp_count_queries in temp2:
        temp2[temp_count_queries] = temp2[temp_count_queries]+1
    else:
        temp2[temp_count_queries] = 1

print(temp2)
print_list = []
sum_proporcia100=0
for count_queries,s_proporcia in temp2.items():
    sum_proporcia100 = sum_proporcia100 + s_proporcia
    print_list.append(f"")

print(sum_proporcia100)

