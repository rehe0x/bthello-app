from .search import serarch

# ...
def init_app(app):
    app.register_blueprint(serarch)
