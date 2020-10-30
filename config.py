import os
import psycopg2
basedir = os.path.abspath(os.path.dirname(__file__))

# Definieren verschiedener Programmierumgebungen (Anwendung siehe __init__.py)
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secretkey'

    conn=psycopg2.connect(dbname='webers', user='postgres', host='microservice-architecture-master_db_1', password='password', port=5432)
    conn.autocommit=True
    cur=conn.cursor()

    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql+psycopg2://postgres:password@localhost:5432/webers')
    #SQLALCHEMY_USERNAME = 'postgres'
    #SQLALCHEMY_PASSWORD = 'password'
    #SQLALCHEMY_DATABASE_NAME = 'webers'
    #SQLALCHEMY_TABLE = 'sales'
    #SQLALCHEMY_DB_SCHEMA = 'public'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True