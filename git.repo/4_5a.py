source = ['2018-01-01', 'yandex', 'cpc', 100]
back_source = list(reversed(source))
print(back_source)
start = back_source[0]
del(back_source[0])
for value in back_source:
    start = {value: start}
print(start)