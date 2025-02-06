import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file (if it exists)

class Config:
    """Base configuration class."""

    # Secret key for signing cookies and other security-related things
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-hard-to-guess-string'

    # Database configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications for performance

    # Chatbot model path
    CHATBOT_MODEL_PATH = os.environ.get('CHATBOT_MODEL_PATH') or 'data/models/chatbot_model.joblib'

    # Email configuration (optional - if you need email functionality)
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['your-email@example.com']

    # Number of posts per page (for pagination)
    POSTS_PER_PAGE = 10

    # Allowed file extensions for uploads (if you have file upload functionality)
    # ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class DevelopmentConfig(Config):
    """Configuration for development environment."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')

class TestingConfig(Config):
    """Configuration for testing environment."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory database for testing
    WTF_CSRF_ENABLED = False  # Disable CSRF protection for testing
    SECRET_KEY = 'test-secret-key' # Use a specific secret key for testing

class ProductionConfig(Config):
    """Configuration for production environment."""

    # Use a real database URL (e.g., PostgreSQL, MySQL)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # IMPORTANT: Set a strong SECRET_KEY in your environment variables!
    # You might also want to set DEBUG = False and configure logging.

# Dictionary to easily access different configurations
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig  # Default configuration
}