from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_project'


from models import * 
from extensions import *
from controllers import *



if __name__ == '__main__':
    db.init_app(app)
    migrate.init_app(app)
    app.run(debug=True)


