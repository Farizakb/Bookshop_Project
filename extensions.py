from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from app1 import app

db = SQLAlchemy(app)
migrate = Migrate(app,db,compare_type = True)
login_manager = LoginManager(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Salam@127.0.0.1:3306/Books'