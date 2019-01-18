from flask import Flask

def create_app():
    from . import  routes
    app = Flask(__name__,static_folder='templates',static_url_path='/s3')
    routes.init_app(app)
    return app