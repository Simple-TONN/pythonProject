from pprint import pprint

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
Country = 'Россия'
geo_logs_result =[]
for geo in geo_logs:
    res = geo
    for res1, res2 in res.items():
        #print(res1,res2)
        if Country in res2:
            #print("rrrrrrrrrrrrr")
            geo_logs_result.append(res)

pprint(geo_logs_result)
