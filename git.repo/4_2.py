
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
a = set()
list_result = []
set_results = set()
for list_number in ids.values():
    set_results = set_results.union(set(list_number))
for set_result in set_results:
    list_result.append(set_result)
print(list_result)
