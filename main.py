from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///progect.db'
db = SQLAlchemy(app)


class Dannye(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Integer, default=0)
    answer1 = db.Column(db.Integer, default=0)
    answer2 = db.Column(db.Integer, default=0)
    answer3 = db.Column(db.Integer, default=0)
    desk1 = db.Column(db.Integer, default=0)
    desk2 = db.Column(db.Integer, default=0)
    desk3 = db.Column(db.Integer, default=0)
    desk4 = db.Column(db.Integer, default=0)
    desk5 = db.Column(db.Integer, default=0)
    answer31_TRUE = db.Column(db.Integer, default=1)
    answer32_TRUE = db.Column(db.Integer, default=4)
    answer33_TRUE = db.Column(db.Integer, default=1)
    answer34_TRUE = db.Column(db.Integer, default=2)
    answer35_TRUE = db.Column(db.Integer, default=3)
    answer36_TRUE = db.Column(db.Integer, default=2)
    answer37_TRUE = db.Column(db.Integer, default=2)
    answer38_TRUE = db.Column(db.Integer, default=1)
    answer39_TRUE = db.Column(db.Integer, default=3)
    answer310_TRUE = db.Column(db.Integer, default=2)
    answer11_TRUE = db.Column(db.Integer, default=1)
    answer12_TRUE = db.Column(db.Integer, default=1)
    answer13_TRUE = db.Column(db.Integer, default=1)
    answer14_TRUE = db.Column(db.Integer, default=2)
    answer15_TRUE = db.Column(db.Integer, default=1)
    answer16_TRUE = db.Column(db.Integer, default=1)
    answer17_TRUE = db.Column(db.Integer, default=1)
    answer18_TRUE = db.Column(db.Integer, default=1)
    answer19_TRUE = db.Column(db.Integer, default=1)
    answer110_TRUE = db.Column(db.Integer, default=2)
    answer21_TRUE = db.Column(db.Integer, default=1)
    answer22_TRUE = db.Column(db.Integer, default=4)
    answer23_TRUE = db.Column(db.Integer, default=3)
    answer24_TRUE = db.Column(db.Integer, default=1)
    answer25_TRUE = db.Column(db.Integer, default=1)
    answer26_TRUE = db.Column(db.Integer, default=4)
    answer27_TRUE = db.Column(db.Integer, default=1)
    answer28_TRUE = db.Column(db.Integer, default=4)
    answer29_TRUE = db.Column(db.Integer, default=1)
    answer210_TRUE = db.Column(db.Integer, default=4)
    name1 = db.Column(db.String(15), nullable=False)
    name2 = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return '<Dannye %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']
        dannye = Dannye(name1=name1, name2=name2)
        db.session.add(dannye)
        db.session.commit()
        users = db.session.query(Dannye).filter(Dannye.name1 == name1, Dannye.name2 == name2).all()
        for elem in users:
            return redirect("/tests/{}".format(elem.id))
    else:
        return render_template('register.html')


@app.route('/gameswhat/<int:id>', methods=['POST', 'GET'])
def gameswhat(id):
    if request.method == 'POST':
        users = db.session.query(Dannye).filter(Dannye.id == id).all()
        for elem in users:
            answers3 = 0
            if int(request.form['answer1']) == int(elem.answer31_TRUE):
                answers3 += 1
            if int(request.form['answer2']) == int(elem.answer32_TRUE):
                answers3 += 1
            if int(request.form['answer3']) == int(elem.answer33_TRUE):
                answers3 += 1
            if int(request.form['answer4']) == int(elem.answer34_TRUE):
                answers3 += 1
            if int(request.form['answer5']) == int(elem.answer35_TRUE):
                answers3 += 1
            if int(request.form['answer6']) == int(elem.answer36_TRUE):
                answers3 += 1
            if int(request.form['answer7']) == int(elem.answer37_TRUE):
                answers3 += 1
            if int(request.form['answer8']) == int(elem.answer38_TRUE):
                answers3 += 1
            if int(request.form['answer9']) == int(elem.answer39_TRUE):
                answers3 += 1
            if int(request.form['answer10']) == int(elem.answer310_TRUE):
                answers3 += 1
            if int(request.form['answer10']) == 4:
                user = db.session.query(Dannye).filter(Dannye.id == id).first()
                user.desk5 = 1
                db.session.commit()
        user = db.session.query(Dannye).filter(Dannye.id == id).first()
        user.answer3 = answers3
        db.session.commit()
        return redirect("/tests/{}".format(id))
    else:
        return render_template('gameswhat.html', id=id)



@app.route('/gameseat/<int:id>', methods=['POST', 'GET'])
def gameseat(id):
    if request.method == 'POST':
        users = db.session.query(Dannye).filter(Dannye.id == id).all()
        for elem in users:
            answers2 = 0
            if int(request.form['answer1']) == int(elem.answer21_TRUE):
                answers2 += 1
            if int(request.form['answer2']) == int(elem.answer22_TRUE):
                answers2 += 1
            if int(request.form['answer3']) == int(elem.answer23_TRUE):
                answers2 += 1
            if int(request.form['answer4']) == int(elem.answer24_TRUE):
                answers2 += 1
            if int(request.form['answer5']) == int(elem.answer25_TRUE):
                answers2 += 1
            if int(request.form['answer6']) == int(elem.answer26_TRUE):
                answers2 += 1
            if int(request.form['answer7']) == int(elem.answer27_TRUE):
                answers2 += 1
            if int(request.form['answer7']) != int(elem.answer27_TRUE):
                user = db.session.query(Dannye).filter(Dannye.id == id).first()
                user.desk2 = 1
                db.session.commit()
            if int(request.form['answer8']) == int(elem.answer28_TRUE):
                answers2 += 1
            if int(request.form['answer9']) == int(elem.answer29_TRUE):
                answers2 += 1
            if int(request.form['answer10']) == int(elem.answer210_TRUE):
                answers2 += 1
        user = db.session.query(Dannye).filter(Dannye.id == id).first()
        user.answer2 = answers2
        db.session.commit()
        return redirect("/tests/{}".format(id))
    else:
        return render_template('gameseat.html', id=id)




@app.route('/gameshello/<int:id>', methods=['POST', 'GET'])
def gameshello(id):
    if request.method == 'POST':
        users = db.session.query(Dannye).filter(Dannye.id == id).all()
        for elem in users:
            answers1 = 0
            if int(request.form['answer1']) == int(elem.answer11_TRUE):
                answers1 += 1
            if int(request.form['answer2']) == int(elem.answer12_TRUE):
                answers1 += 1
            if int(request.form['answer3']) == int(elem.answer13_TRUE):
                answers1 += 1
            if int(request.form['answer3']) != int(elem.answer13_TRUE):
                user = db.session.query(Dannye).filter(Dannye.id == id).first()
                user.desk3 = 1
                db.session.commit()
            if int(request.form['answer4']) == int(elem.answer14_TRUE):
                answers1 += 1
            if int(request.form['answer4']) != int(elem.answer14_TRUE):
                user = db.session.query(Dannye).filter(Dannye.id == id).first()
                user.desk1 = 1
                db.session.commit()
            if int(request.form['answer5']) == int(elem.answer15_TRUE):
                answers1 += 1
            if int(request.form['answer6']) == int(elem.answer16_TRUE):
                answers1 += 1
            if int(request.form['answer7']) == int(elem.answer17_TRUE):
                answers1 += 1
            if int(request.form['answer8']) == int(elem.answer18_TRUE):
                answers1 += 1
            if int(request.form['answer9']) == int(elem.answer19_TRUE):
                answers1 += 1
            if int(request.form['answer10']) == int(elem.answer110_TRUE):
                answers1 += 1
        user = db.session.query(Dannye).filter(Dannye.id == id).first()
        user.answer1 = answers1
        db.session.commit()
        return redirect("/tests/{}".format(id))
    else:
        return render_template('gameshello.html', id=id)




@app.route('/tests/<int:id>')
def tests(id):
    dannye = Dannye.query.order_by(Dannye.answer).all()
    users = db.session.query(Dannye).all()
    for elem in users:
        answer = int(elem.answer1) + int(elem.answer2) + int(elem.answer3)
        elem.answer = answer
        db.session.commit()
    user = db.session.query(Dannye).filter(Dannye.id == id).first()
    return render_template('index.html', dannye=dannye, id=id, user=user)



@app.route('/tables/<int:id>')
def tables(id):
    users = db.session.query(Dannye).all()
    for elem in users:
        answer = int(elem.answer1) + int(elem.answer2) + int(elem.answer3)
        elem.answer = answer
        db.session.commit()
    dannye = Dannye.query.order_by(Dannye.answer.desc()).all()
    return render_template('tables.html', dannye=dannye, id=id)


@app.route('/dost/<int:id>')
def dostigenya(id):
    users = db.session.query(Dannye).all()
    for elem in users:
        answer = int(elem.answer1) + int(elem.answer2) + int(elem.answer3)
        elem.answer = answer
        db.session.commit()
    dannye = Dannye.query.order_by(Dannye.answer.desc()).all()
    user = db.session.query(Dannye).filter(Dannye.id == id).first()
    return render_template('dost.html', dannye=dannye, id=id, user=user)


if __name__ == '__main__':
    app.run(debug=True)
