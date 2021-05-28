import requests
URL="https://www.joinclubhouse.com/join/cryptohub-india/rBAf6Wkd/maGODjjz?fbclid=IwAR1OoAYBQBXI3pmjkoPx6lmUkRieGKH-ZHLow7Wl-Pus6KLxKQ8pYMpyD0s"
miniurl="https://www.joinclubhouse.com/join_club_from_invite"
def magic(fullno):
    client = requests.session()
    req=client.get(URL)
    if 'csrftoken' in client.cookies:
        csrftoken = client.cookies['csrftoken']
    else:
        csrftoken = client.cookies['csrf']

    cookie=req.headers['Set-Cookie']
    cookie=cookie.split(';')
    cookie=cookie[0]
    headers={
        'x-csrftoken':csrftoken,
        'referer':URL,
        'cookie': cookie
    }
    data = {
    'phone_number': fullno,
    'invite_code': 'rBAf6Wkd'
    }
    response = requests.post(miniurl, headers=headers, data=data)
    return response.json()

F=magic('+919878765676')
#fol=F[0]
print(F)
print(F['success'])
#print(fol)