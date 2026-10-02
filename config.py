from urllib.parse import quote_plus
import os
import secrets
from pathlib import Path

import socket


# Base Directory of the application
BASE_DIR = Path(__file__).resolve().parent


def is_mysql_available(host, port):
    try:
        s = socket.create_connection((host, int(port)), timeout=1.0)
        s.close()
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


class Config:
    # Flask application secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(32)

    # Database Settings
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '3306')
    DB_NAME = os.environ.get('DB_NAME', 'mediconnect_db')

    # MySQL connection string
    # quote_plus safely handles special characters in password
    MYSQL_URI = (
        f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # SQLite Fallback path
    SQLITE_URI = f"sqlite:///{BASE_DIR}/medicare.db"

    # Use MySQL database
    SQLALCHEMY_DATABASE_URI = MYSQL_URI

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # File Upload Directory Setup
    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        'app',
        'static',
        'uploads'
    )

    PROFILE_PICS_FOLDER = os.path.join(
        UPLOAD_FOLDER,
        'profile_pics'
    )

    REPORTS_FOLDER = os.path.join(
        UPLOAD_FOLDER,
        'reports'
    )

    # Max file upload size (16MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # Allowed extensions
    ALLOWED_EXTENSIONS = {
        'png',
        'jpg',
        'jpeg',
        'gif',
        'pdf',
        'doc',
        'docx'
    }

    @classmethod
    def init_app(cls, app):
        # Create directories if they do not exist
        os.makedirs(
            cls.PROFILE_PICS_FOLDER,
            exist_ok=True
        )

        os.makedirs(
            cls.REPORTS_FOLDER,
            exist_ok=True
        )