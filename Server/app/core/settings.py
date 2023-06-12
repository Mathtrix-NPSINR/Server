import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "Mathtrix"
    SQLALCHEMY_DATABASE_URL = "sqlite:///app/data/mathtrix.db"
    MATHTRIX_EMAIL_ADDRESS = os.getenv("MATHTRIX_EMAIL_ADDRESS")
    MATHTRIX_EMAIL_PASSWORD = os.getenv("MATHTRIX_EMAIL_PASSWORD")
    QR_CODES_DIRECTORY = "app/data/qrcodes/"


settings = Settings()
