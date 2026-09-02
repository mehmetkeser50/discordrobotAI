# İçeri Aktarma
from flask import Flask, render_template,request, redirect, session
# Veritabanı kütüphanesini içe aktarma
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "my_top_secret_123"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # DB oluşturma
db = SQLAlchemy(app )


class Card(db.Model):
    __tablename__="cards"
        
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(100),nullable=False)
    subtitle=db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    def __repr__(self): 
        return f"<Card {self.title}>"

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable = False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self): 
        return f"<Card {self.id}>"

with app.app_context():
    db.create_all()

# Görev #1. Kullanıcı tablosunu oluşturun.


# İçerik sayfasını başlatma
@app.route('/', methods=['GET','POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']
            
        # Görev #4. Kullanıcı doğrulamasını uygulayın
        users_db = User.query.all()
        for user in  users_db:
            if form_login == user.email and form_password == user.password:
                session["user_email"] = user.email
                return redirect ("/index")

            else:
                error = "Hatalı E-Posta Veya Şifre Girdiniz: Lütfen Eğer Bu E-Posta Başkasınınsa ve ondan izin almadıysanız bu E-Postayı Kullanmayın. Lütfen Kendi E-Postanızı Kullanın. Eğer Şifreyi Unuttuysanız Siz Sorumlusunuz. Bizde Sıfırlama Butonu Falan Olmaz Sorumlu Kullanıcıdadır."
     
    else:
        return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Görev #3. Kullanıcı doğrulamasını uygulayın
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()

        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


# İçerik sayfasını başlatma
@app.route('/index')
def index():
    # DB nesnelerini görüntüleme
    email = session.get('user_email')
    cards = Card.query.filter_by(user_email=email).all()
   

    return render_template('index.html',
                           #kartlar = kartlar
                          cards=cards 
                           )

# Kartla sayfayı çalıştırma
@app.route('/card/<int:id>')
def card(id):
#Görev #2. Id'ye göre doğru kartı görüntüleme
      card=Card.query.get(id)
      return render_template('card.html', card=card)

   

# Sayfayı çalıştırma ve kart oluşturma
@app.route('/create')
def create():
    return render_template('create_card.html')

# Kart formu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if 'user_email' not in session:
        return redirect('/')
    
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']
        email = session['user_email']
        # Görev #2. Verileri DB'de depolamak için bir yol oluşturun
        card = Card(title=title, subtitle=subtitle, text=text, user_email=email)
        db.session.add(card)
        db.session.commit()



        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
