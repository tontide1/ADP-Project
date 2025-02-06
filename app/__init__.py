from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS  # Import CORS
from config import config  # Import từ config.py

# Khởi tạo các extensions (chưa gắn với app)
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Route xử lý đăng nhập
login_manager.login_message_category = 'info'  # Loại message cho flash message
csrf = CSRFProtect()
cors = CORS()

def create_app(config_name='default'):
    """Tạo và cấu hình ứng dụng Flask."""

    app = Flask(__name__)

    # Load cấu hình
    app.config.from_object(config[config_name])

    # Khởi tạo các extensions với app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    cors.init_app(app) # Khởi tạo CORS và truyền app vào

    # Đăng ký các blueprints
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')  # URL prefix cho auth

    from app.chatbot import chatbot as chatbot_blueprint
    app.register_blueprint(chatbot_blueprint, url_prefix='/chatbot') # URL prefix cho chatbot

    # from app.admin import admin as admin_blueprint # Nếu có blueprint cho admin
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')


    return app