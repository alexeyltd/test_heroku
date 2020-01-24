from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config.Config import Config

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='static')

# main app config
app.config.from_object(Config)

# db init
db = SQLAlchemy(app)
db.create_all()
db.session.commit()
migrate = Migrate(app, db)

# import routes from routes
from routes import Account, Admin, Article, Brief, Notification, Title


# frontend index page
@app.route('/')
def index():
    return render_template('index.html')


# all to vue router
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
