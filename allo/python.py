import requests
import sys
username = sys.argv[1]

session = {'PHPSESSID': 'sm8ukhk73eu0h2514s6p9s7c8p'}

search = requests.get(f'https://overseer.1337.ma/api/users?page=1&username={username}', cookies = session).json()
user_id = search['hydra:member'][0]['student']['id']
res_body = requests.get(f"https://overseer.1337.ma/_next/data/QLfn6qnLowKAK_ZiVhg8E/user/{user_id}.json?id=0", cookies = session).json()
overseer_data = res_body['pageProps']['data']
print(overseer_data)
user_y = overseer_data['student'][0]['y']
user_x = overseer_data['student'][0]['x']
user_stats = {} if user_x > 614 else overseer_data['plotData']['plots'][user_x]
big_wire = user_stats.get('Avg. teams')
small_wire = user_stats.get('Min. of double ETA') or user_stats.get('Max blackhole')

print(overseer_data['student'][0]['login'])
if user_x > 614:
    print("saliti")
elif user_y >= big_wire:
    print("nadi")
elif user_y < big_wire and user_y >= small_wire:
    print('chwia')
else:
    print('d3if')