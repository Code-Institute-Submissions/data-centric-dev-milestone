import requests
import os
from flask import Flask
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Testing Heroku URL #
def request():
    request = requests.get('https://data-centric-dev.herokuapp.com/')
    print('Heroku server response for index page - {r}'.format(r=request))


request()


# To test MongoDB connection I have created a test database
def test_add():
    mydict = {"name": "Test", "address": "Test"}
    mongo.db.test.insert_one(mydict)
    print(list(mongo.db.test.find({})))


test_add()
