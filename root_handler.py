from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext import db

from google.appengine.api import taskqueue

from dataAccess import MessagesByIndexQuery

import jinja2
import os
from Tasks import startMessageGetTask, startFixMultipleInsertIndexTask
from modelInterrogator import getRandomMessage

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

#NOTE unused import, but breaks query if not present. Obviously __init__ does magic.
from model import GitHubCommitComment
import modelInterrogator
import random


class ShowMessages(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        commitMessages = db.GqlQuery("SELECT * FROM GitHubCommitComment ")
        for commitMessage in commitMessages:
            self.response.out.write('<p>' + commitMessage.message)
#            self.response.out.write('<br>' + commitMessage.repo)
#            if commitMessage.owner is not None:
#                self.response.out.write('<br>')
#                self.response.out.write(commitMessage.owner)
#            if commitMessage.url is not None:
#                self.response.out.write('<br><a href="')
#                self.response.out.write(commitMessage.url)
#                self.response.out.write('">link</a>')
            self.response.out.write('</p>')
        self.response.out.write('</body></html>')
        
        startMessageGetTask()
        
class ShowOneMessage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        randomMessage = getRandomMessage()
        if not randomMessage == None:
            self.response.out.write('<p>' + randomMessage.message)
            self.response.out.write('</p>')
        self.response.out.write('</body></html>')
    

class LandingHandler(webapp.RequestHandler):
    def get(self):
        template_values = {
            'greeting': 'GitHub Conversations',
            'url': 'https://google.com',
            'url_linktext': 'google',
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

application = webapp.WSGIApplication(
                                     [('/readAllMessages', ShowMessages), ('/oneMessage', ShowOneMessage), ('/', LandingHandler)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()