stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 199, 'email': 42, 'ok': 98}

max_stats_value = []
for stats_values in stats.values():
    max_stats_value.append(stats_values)

for resultkey, resultvalue in stats.items():
    if resultvalue== max(max_stats_value):
        print(resultkey)
