import os


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', '$y0ur$3cr3tK3y')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
