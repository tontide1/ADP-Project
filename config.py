import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-hard-to-guess-string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 10

    # Path to the trained chatbot model
    CHATBOT_MODEL_PATH = os.environ.get('CHATBOT_MODEL_PATH') or os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'data', 'models', 'chatbot_model.joblib'
    )

    # Email configuration (optional)
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['your-email@example.com']

class DevelopmentConfig(Config):
    """Configuration for development environment."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')

class TestingConfig(Config):
    """Configuration for testing environment."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for faster tests
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing purposes
    SECRET_KEY = 'test-secret-key'

class ProductionConfig(Config):
    """Configuration for production environment."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    ENABLE_CORS = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}