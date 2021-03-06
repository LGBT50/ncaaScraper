from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import time

from gSheet import sendToGoogleSheets
from ncaaScraper import scraperFunc
from googleSearch import instaLink


#initializing app, api, and cors
application = Flask(__name__)
api = Api(application)
cors = CORS(application, origins={"origins": "*"})

#definiing endpoints and actions
class ncaa(Resource):
    def post(self):
        scraperFunc()
        return "Success"
    def get(self):
        return "get"

class getLink(Resource):
    def post(self):
        instaLink()
        return "Success"
    def get(self):
        return "get"

class Home(Resource):
    def get(self):
        return "Hello World!"
api.add_resource(ncaa, "/ncaa")
api.add_resource(Home, "/")
api.add_resource(getLink, "/getLink")



if __name__ == "__main__":
   application.run()

#