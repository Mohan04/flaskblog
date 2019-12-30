import os

class Config:
    SECRET_KEY = 'cdffc84294b0ffc6f942b3e7bbf1c41b'
    SQLALCHEMY_DATABASE_URI ='sqlite:///site.db'
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME= os.environ.get('EMAIL_USER')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASS')