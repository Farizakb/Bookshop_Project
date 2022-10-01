from flask_wtf import FlaskForm 
from wtforms import StringField ,TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, Length



class CommentForm(FlaskForm):
    full_name = StringField(label = 'Tam Adiniz', validators=[DataRequired(), Length(min=3,max=30)])
    dil = SelectField(label = 'Hansi dilde oxumusunuz?',choices=["Azerbaycan","Turk","English"])
    qiymetlendirem = SelectField(label = "Ulduz verin", choices=[1,2,3,4,5])
    message = TextAreaField(label = "message")


class RegisterForm(FlaskForm):
    first_name = StringField(label = 'Adiniz', validators=[DataRequired(), Length(min=3,max=30)])
    last_name = StringField(label = 'Soyadiniz', validators=[DataRequired(), Length(min=3,max=30)])
    email = StringField(label = "Email", validators=[DataRequired(), Email(), Length(min=4,max=30)])
    username = StringField(label = 'Tam Adiniz', validators=[DataRequired(), Length(min=3,max=30)])
    password = StringField(label = 'Shifreniz', validators=[DataRequired(), Length(min=8,max=30)])


class LoginForm(FlaskForm):
    username = StringField(label = 'Tam Adiniz', validators=[DataRequired(), Length(min=3,max=30)])
    password = StringField(label = 'Shifreniz', validators=[DataRequired(), Length(min=8,max=30)])
