import flask
from flask import Flask, render_template
import json
from flask import request

app = Flask(__name__)

f=open('teachers.json','r')
teachers=json.loads(f.read())['teachers']
f.close()


goalsdict = {"travel": "Для путешествий", "study": "Для учебы", "work": "Для работы", "relocate": "Для переезда"}

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/goals/<goal>')
def goals(goal):
    return render_template('goal.html')

@app.route('/profiles/<tutorid>/')
def profiles(tutorid):
    tutor = [x for x in teachers if x['id'] == int(tutorid)][0]

    return render_template('profile.html', tutor=tutor, goalsdict=goalsdict)

@app.route('/request/')
def requestpage():
    return render_template('request.html')

@app.route('/request_done/')
def request_done():
    return render_template('request_done.html')

@app.route('/booking/<tutorid>/<dayofweek>/<time>/')
def booking(tutorid, dayofweek, time):
    tutor = [x for x in teachers if x['id'] == int(tutorid)][0]
    return render_template('booking.html', tutor=tutor, dayofweek=dayofweek, time=time)

@app.route('/booking_done', methods=["POST"])
def booking_done():
    if request.method == 'POST':
        clientWeekday = request.form.get("clientWeekday")
        clientTime = request.form.get("clientTime")
        clientTeacher = int(request.form.get("clientTeacher"))
        clientName = request.form.get("clientName")
        clientPhone = request.form.get("clientPhone")
        f = open('booking.json', 'a')
        book={"clientWeekday":clientWeekday,
              "clientTime":clientTime,
              "clientTeacher":clientTeacher,
              "clientName":clientName,
              "clientPhone":clientPhone}
        f.write(json.dumps(book))
    return render_template('booking_done.html', clientWeekday=clientWeekday,
                           clientTime=clientTime, clientTeacher=clientTeacher,
                           clientName=clientName, clientPhone=clientPhone)



if __name__ == '__main__':
    app.run()