from flask import Blueprint

main = Blueprint('main', __name__)

from app.main import views # Import views AFTER blueprint is created