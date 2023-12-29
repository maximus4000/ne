#Импорт
from flask import Flask, render_template,request, redirect
#Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)
#Создание таблицы

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<User {self.id}>'

#Запуск страницы с контентом
@app.route('/#home')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        email =  request.form['email']
        text =  request.form['text']

        #Создание объкта для передачи в дб

        card = User(email=email, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)


if __name__ == "__main__":
    app.run(debug=True)
