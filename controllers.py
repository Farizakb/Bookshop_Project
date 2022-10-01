from flask import render_template , request, redirect
from flask_login import login_user , login_required, logout_user
from app1 import app
from forms import CommentForm, LoginForm, RegisterForm
from models import *



@app.route("/")
@login_required
def Books():
    books = Bookss.query.all()
    return render_template("Index.html",datas = books)



@app.route("/book/<int:book_int>/", methods = ["GET", "POST"])
def Book(book_int):
    book = Bookss.query.get(book_int)
    print(book)
    form = CommentForm()
    if request.method == "POST":
        post_data = request.form
        form = CommentForm(data=post_data)
        if form.validate_on_submit():
            comment = Comment(full_name=form.full_name.data,dil=form.dil.data,qiymetlendirme=form.qiymetlendirem.data,message=form.message.data, book = book_int)
            comment.save()
            form.full_name.data = " "
            form.dil.data = " "
            form.qiymetlendirem.data = " "
            form.message.data = " "


    datas = Comment.query.filter_by(book = book_int)

        

    
    return render_template("Product.html", data = book,form=form, datas = datas)



@app.route("/register/",methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        post_data = request.form
        form = RegisterForm(data=post_data)
        if form.validate_on_submit():
            user = User(f_n=form.first_name.data, l_n=form.last_name.data,em=form.email.data,us=form.username.data,ps=form.password.data)
            user.save()
            form.first_name.data = " "
            form.last_name.data = " "
            form.email.data = " "
            form.username.data = " "
            form.password.data = " "
            return redirect("/login/")
    return render_template("sign-up.html", form=form)





@app.route("/login/",methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        post_data = request.data
        form = LoginForm(data = post_data)
        if form.validate_on_submit():
            user = User.query.filter_by(username = form.username.data).first()
            print(user)
            print(user.password,form.password.data)
            
            if user and user.password == form.password.data:
                login_user(user)
                print("User login oldu")
                return redirect("/")
            else:
                print("User login ola bilmedi")
    return render_template("sign_in.html", form=form)


@app.route("/logout/",methods = ["GET", "POST"])
def logout():
    logout_user()
    return redirect("/login/")










# app.route("/contact",methods = ["GET","POST"])
# # def contact():
# #     form = ContactForm()
# #     post_data = request.form
#     print(post_data)
#     if request.method == "POST":
#         form = ContactForm(data=post_data)
#         print(form)
#         print(form.validate_on_submit())
#         if form.validate_on_submit():
#             contact = Contact(full_name=form.full_name.data,email=form.email.data,service=form.service.data,budget=form.budget.data,message=form.message.data)
#             contact.save()
#             form.full_name.data = " "
#             form.email.data = " "
#             form.service.data = " "
#             form.budget.data = " "
#             form.message.data = " "
#     return render_template("index.html",form = form)