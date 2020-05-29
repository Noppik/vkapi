import requests

id = input()
answer = requests.get('https://api.vk.com/method/friends.get?user_id=' + id
                        + '&v=5.52&access_token').json()
for id_p in answer['response']['items']:
    info = requests.get('https://api.vk.com/method/users.get?user_id=' + str(id_p) +
                          '').json()
    fio = info['response'][0]
    print(str(fio['first_name']) + str(fio['last_name']))

