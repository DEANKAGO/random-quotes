"""
The app configurations
"""
import os


class Config:
    """
    The default configuration class
    """
    DEBUG = False
    SECRET_KEY = 'verysecretkey'
    


class DevelopmentConfig(Config):
    """
    The development configuration class
    """
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'


class TestingConfig(Config):
    """
    The testing configuration class
    """
    DEBUG = True
    test_db_url = os.getenv('DATABASE_TEST_URL')


class ProductionConfig(Config):
    """
    The testing configuration class
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL')


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "SQLALCHEMY_DATABASE_URI": os.getenv('DATABASE_URL'),
    "test_db_url": os.getenv('DATABASE_TEST_URL'),
    "prod_db_url": os.getenv('DATABASE_TEST_URL')
}
