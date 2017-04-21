from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


app = Flask(__name__)


engine = create_engine('sqlite:///roles.db')
Base.metadata.bind = engine


@app.route('/')
def Index():
    return "Hello Finsystem"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

