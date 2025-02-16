# app/chatbot/__init__.py
from flask import Blueprint

chatbot = Blueprint('chatbot', __name__)

from app.chatbot import views  # Import views AFTER blueprint creation
from app.chatbot import nlp # Optionally import nlp if you have nlp.py