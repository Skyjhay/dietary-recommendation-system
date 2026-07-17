"""
Configuration module for the Dietary Recommendation System
Load settings from environment variables
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration"""
    
    # Flask
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = os.getenv('FLASK_DEBUG', True)
    TESTING = False
    
    # Server
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))
    
    # API
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', 30))
    API_MAX_CONTENT_LENGTH = int(os.getenv('API_MAX_CONTENT_LENGTH', 16777216))
    
    # CORS
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')
    
    # Data
    DATA_FILE = os.getenv('DATA_FILE', 'data/dietary_data.json')
    
    # KNN
    KNN_K_NEIGHBORS = int(os.getenv('KNN_K_NEIGHBORS', 5))
    KNN_TEST_SIZE = float(os.getenv('KNN_TEST_SIZE', 0.2))
    KNN_RANDOM_STATE = int(os.getenv('KNN_RANDOM_STATE', 42))
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'app.log')


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'production'


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    DATA_FILE = 'tests/fixtures/test_data.json'


def get_config(env=None):
    """Get configuration based on environment"""
    if env is None:
        env = os.getenv('FLASK_ENV', 'development')
    
    config_map = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }
    
    return config_map.get(env, DevelopmentConfig)
