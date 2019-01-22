from .search import serarch
from .custom_tempfilter import init_ctfilter

# ...
def init_app(app):
    #注册
    app.register_blueprint(serarch)
    #初始化自定义过滤器
    init_ctfilter(app)