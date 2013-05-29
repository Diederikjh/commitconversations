'''
Created on 20 Apr 2013

@author: drbergie
'''
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import json
import modelInterrogator
from google.appengine.ext import db
import logging

class GetOneMessage(webapp.RequestHandler):
    def get(self):
        randomMessage = modelInterrogator.getRandomMessage()
        if randomMessage == None:
            logging.warn("None returned from db")
        else:
            self.response.out.write(json.dumps(db.to_dict(randomMessage)))

application = webapp.WSGIApplication(
                                     [('/api/1/getOneMessage', GetOneMessage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
