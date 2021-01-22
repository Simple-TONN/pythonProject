from pprint import pprint
#source = ['2018-01-01', 'yandex', 'cpc', 100]
source = ['2018-01-01', 'yandex']
if len(source)==1:
    pritn("Словарь невозможен")
temp_dict = source[-1]
del(source[-1])
while len(source) >= 1:
        temp_dict = {source[-1]: temp_dict}
        del source[-1]

pprint(temp_dict)
