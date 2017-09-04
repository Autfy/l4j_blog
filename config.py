#-*- coding=utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'SSDFDSFDFD'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/db'
#SQLALCHEMY_DATABASE_URI ='sqlite:///'+os.path.join(basedir,'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = True
