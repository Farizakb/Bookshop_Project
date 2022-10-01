from extensions import db, login_manager
from sqlalchemy import ForeignKey
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Bookss(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    author = db.Column (db.String(30), nullable=False)
    price = db.Column (db.Float(3),default = 0.00)
    description = db.Column (db.Text(),nullable=False)
    image_url = db.Column (db.String(40))
    stock = db.Column (db.Integer(), nullable=False)
    genre = db.Column(db.String(30))
    language = db.Column (db.String(30), nullable = False)
    publiser = db.Column (db.String(40), nullable=True)

    # Book modeli düzəldilməlidir (fildlər: id, title, author, price, description, image_url, stock, genre, language, publisher)




    def __init__(self,title,aut,pr,des,img,stc,genr,lang,publ):
        self.title = title
        self.author = aut
        self.price = pr
        self.description = des
        self.image_url = img
        self.stock = stc
        self.genre = genr
        self.language = lang
        self.publiser = publ




    def save(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return self.title





class Comment(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String(30), nullable=False)
    dil  = db.Column (db.String(30), nullable=False)
    qiymetlendirme = db.Column (db.String(30))
    message = db.Column (db.Text())
    book = db.Column (db.Integer(),ForeignKey("bookss.id"))


    def __init__(self,full_name,dil,qiymetlendirme,message,book):
        self.full_name = full_name
        self.dil = dil
        self.qiymetlendirme = qiymetlendirme
        self.message = message
        self.book = book


    def __repr__(self):
        return self.full_name

    def save(self):
        db.session.add(self)
        db.session.commit()



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column (db.String(30),nullable=False)
    email  = db.Column (db.String(30), nullable=False)
    username = db.Column(db.String(30), nullable = False)
    password = db.Column (db.String(255),nullable = False)
    is_active = db.Column (db.Boolean,nullable = False)
    is_superuser = db.Column (db.Boolean, nullable =False)


    def __init__(self,f_n,l_n,em,us,ps,i_a = True,i_s = False):
        self.first_name = f_n
        self.last_name = l_n
        self.email = em
        self.username = us
        self.password = ps
        self.is_active = i_a
        self.is_superuser = i_s

    def set_password(self,new_password):
        self.password = generate_password_hash(new_password)

    def chech_password(self,password):
        return check_password_hash(self.password,password)

    def save(self):
        db.session.add(self)
        db.session.commit()







