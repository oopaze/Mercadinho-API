import os

class Config(object):
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'MinhaNamoradaEUmaGostosinhaLinda'
	basedir = os.path.abspath(os.path.dirname(__file__))



class Development(Config):
	ENV = 'Development'
	DEBUG = True
	basedir = os.path.abspath(os.path.dirname(__file__))
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mercadin.db')


class Production(Config):
	ENV = 'Production'
	DEBUG = False
	basedir = os.path.abspath(os.path.dirname(__file__))
	os.environ['FLASK_APP'] = os.path.join(self.basedir, 'run.py')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mercadin.db')
