import requests

id = input()
answer = requests.get('https://api.vk.com/method/friends.get?user_id=' + id
                        + '&v=5.52&access_token=1396751313967513139675132b13e44e5e11396139675134d5820d0cf10ae78f6d5aa55').json()
for id_p in answer['response']['items']:
    info = requests.get('https://api.vk.com/method/users.get?user_id=' + str(id_p) +
                          '&v=5.52&access_token=1396751313967513139675132b13e44e5e11396139675134d5820d0cf10ae78f6d5aa55').json()
    fio = info['response'][0]
    print(str(fio['first_name']) + str(fio['last_name']))

