from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "Mathtrix"
    SQLALCHEMY_DATABASE_URL = "sqlite:///app/data/mathtrix.db"


settings = Settings()
