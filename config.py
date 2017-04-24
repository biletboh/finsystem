#  Configuration of application
DEBUG = True
SECRET_KEY = 'development key'
WTF_CSRF_SECRET_KEY = 'secret csrf key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///roles.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False


#  Flask security configuration
SECURITY_URL_PREFIX = '/admin'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'ATGUasdfUEiOHAELKiubahiughaerGOJAEGj'
SECURITY_POST_LOGIN_VIEW = '/admin'
SECURITY_POST_LOGOUT_VIEW = '/admin'

