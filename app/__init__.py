import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify

# Import Flask extensions
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from flask_migrate import Migrate

from config import config  # Import your configuration

# Initialize Flask extensions globally but WITHOUT associating them with the app yet
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Define login view for authentication
login_manager.login_message_category = 'info' # Category for login messages (e.g., for Bootstrap alerts)
csrf = CSRFProtect()
cors = CORS()
migrate = Migrate() # Initialize Migrate without app and db

def create_app(config_name='default'):
    """Application factory function to create and configure the Flask app."""

    # Validate config_name
    if config_name not in config:
        raise ValueError(f"Configuration '{config_name}' is invalid. Choose from: {list(config.keys())}")

    app = Flask(__name__) # Create Flask application instance
    app.config.from_object(config[config_name]) # Load configuration from config.py

    # Initialize Flask extensions with the Flask application instance
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db) # Initialize Flask-Migrate with app and db

    # Register blueprints - Import blueprints AFTER app is created to avoid circular imports
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth') # Register auth blueprint with URL prefix

    from app.chatbot import chatbot as chatbot_blueprint
    app.register_blueprint(chatbot_blueprint, url_prefix='/chatbot') # Register chatbot blueprint with URL prefix

    from app.admin import admin as admin_blueprint  # Optional admin blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin') # Register admin blueprint with URL prefix

    # Setup logging for production (only if not in debug mode)
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/error.log', maxBytes=10240, backupCount=10)
        file_handler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)

    # Custom error handlers for 404 and 500 errors (returning JSON responses)
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found", "message": "Trang bạn yêu cầu không tồn tại"}), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"error": "Server Error", "message": "Đã xảy ra lỗi trên server"}), 500

    return app