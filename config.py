import os

project_dir = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')

class Config:
    SECRET_KEY = 'SUPER_SECRET'
    DEBUG = True
    TESTING = True
    USER_DB='root'
    HOST_DB='localhost'
    PASSWORD_DB= 'YOUR-PASSWORD'
    PROJECT_DIR = project_dir
    SQLALCHEMY_DATABASE_URI= f'mysql+pymysql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}/poevent'
    SQLALCHEMY_TRACK_MODIFICATIONS = False