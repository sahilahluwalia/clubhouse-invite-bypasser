from flask import Flask, render_template, request, redirect, url_for
import requests

URL = "https://www.joinclubhouse.com/join/cryptohub-india/rBAf6Wkd/maGODjjz?fbclid=IwAR1OoAYBQBXI3pmjkoPx6lmUkRieGKH-ZHLow7Wl-Pus6KLxKQ8pYMpyD0s"
miniurl = "https://www.joinclubhouse.com/join_club_from_invite"


def magic(fullno):
    client = requests.session()
    req = client.get(URL)
    if 'csrftoken' in client.cookies:
        csrftoken = client.cookies['csrftoken']
    else:
        csrftoken = client.cookies['csrf']

    cookie = req.headers['Set-Cookie']
    cookie = cookie.split(';')
    cookie = cookie[0]
    headers = {
        'x-csrftoken': csrftoken,
        'referer': URL,
        'cookie': cookie
    }
    data = {
        'phone_number': fullno,
        'invite_code': 'rBAf6Wkd'
    }
    response = requests.post(miniurl, headers=headers, data=data)
    return response.json()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route("/phone", methods=['POST', 'GET'])
def phone():
    if request.method == 'POST':
        phone = request.form.get("phone")
        countrycode = request.form.get("countrycode")
        fullno = "+"+countrycode+phone
        if len(fullno) < 8 or len(fullno) > 16:
            return render_template('phone.html', bol="FAILED")
        answer = magic(fullno)
        #answer = {}
        #answer['success'] = True
        if answer['success'] == True:
            bol = "SUCESS"
        else:
            bol = "FAILED"
        return render_template('phone.html', fullno=fullno, bol=bol)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
