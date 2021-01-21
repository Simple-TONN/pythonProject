from pprint import pprint

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'test': ['Париж', 'Россия']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
Country = 'Россия'
geo_logs_result =[]
for geo in geo_logs:
    #res = geo
    for visit, visit_info in geo.items():
        #print(res1,res2)
        if Country in visit_info:
            #print("rrrrrrrrrrrrr")
            geo_logs_result.append(geo)

pprint(geo_logs_result)
