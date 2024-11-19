# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///segotel.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db?timeout=30'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_really_long_and_random_secret_key'  # Use environment variable or fallback

