import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("postgres://qnoyeqzbyhguyo:9045655718d1a3d54d4059de8a39f3c4563491fef4cbfb52917d2066b1937024@ec2-54-157-78-113.compute-1.amazonaws.com:5432/d4j0mlpmf0hfi1"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("postgres://qnoyeqzbyhguyo:9045655718d1a3d54d4059de8a39f3c4563491fef4cbfb52917d2066b1937024@ec2-54-157-78-113.compute-1.amazonaws.com:5432/d4j0mlpmf0hfi1"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
