from .routes.views import views
from .routes.api import apiView
from flask import Flask

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'shamoil18bobby56'
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(apiView, url_prefix='/')

    return app
