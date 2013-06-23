from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext import db

from google.appengine.api import taskqueue

from dataAccess import MessagesByIndexQuery

import jinja2
import os
from Tasks import startMessageGetTask, startFixMultipleInsertIndexTask
from modelInterrogator import getRandomMessage
import navbar

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
    

def ensureDbNotEmpty():
    if not modelInterrogator.dataStoreHasMessages():
        startMessageGetTask()
        
class ConversationsHandler(webapp.RequestHandler):
    def get(self):
        n = navbar.navbar()
        n.setNavBarItemActive("Conversation")
        template_values = { }
        n.appendTemplateInfo(template_values)
        template = JINJA_ENVIRONMENT.get_template('files/templates/conversation.html')
        self.response.write(template.render(template_values))
        ensureDbNotEmpty()
        
class DevTestHandler(webapp.RequestHandler):
    def get(self):
        n = navbar.navbar()
        n.setNavBarItemActive("Doing now?")
        template_values = { }
        n.appendTemplateInfo(template_values)
        template = JINJA_ENVIRONMENT.get_template('files/templates/nav-base.html')
        self.response.write(template.render(template_values))
            
class WhatAreYouDoingDevHandler(webapp.RequestHandler):
    def get(self):
        n = navbar.navbar()
        n.setNavBarItemActive("Single")
        template_values = { }
        n.appendTemplateInfo(template_values)
        template = JINJA_ENVIRONMENT.get_template('files/templates/waydn.html')
        self.response.write(template.render(template_values))
        
        ensureDbNotEmpty()
        
class AboutHandler(webapp.RequestHandler):
    def get(self):
        n = navbar.navbar()
        n.setNavBarItemActive("About")
        template_values = { }
        n.appendTemplateInfo(template_values)
        template = JINJA_ENVIRONMENT.get_template('files/templates/about.html')
        self.response.write(template.render(template_values))
        
        ensureDbNotEmpty()

class RedirectToDefaultNavItemHandeler(webapp.RequestHandler):
    def get(self):
        self.redirect("/conversation")

application = webapp.WSGIApplication([
                                      ('/', RedirectToDefaultNavItemHandeler),
                                      ('/conversation', ConversationsHandler),
                                      ('/WAYDN',WhatAreYouDoingDevHandler),
                                      ('/About',AboutHandler)
                                      #('/oneMessage', ShowOneMessage), 
                                      #('/readAllMessages', ShowMessages), 
                                      #('/devtest', DevTestHandler),
                                      ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
