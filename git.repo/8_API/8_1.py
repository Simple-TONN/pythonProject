import requests

token = "2619421814940190"

her = ["Hulk", "Captain America", "Thanos"]
res_dict ={}
for each_her in her:
    response = requests.get(f'https://superheroapi.com/api/{token}/search/{each_her}')
    res_dict[each_her]=int(response.json()['results'][0]['powerstats']['intelligence'])

print(res_dict)
print(max(res_dict.values()))
print(max(res_dict.keys()))






