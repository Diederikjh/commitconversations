'''
Created on 01 Apr 2013

@author: drbergie
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import message_getter
import dataAccess
import modelInterrogator
import logging

class AddCommentsTask(webapp.RequestHandler):
    def post(self):
        message_getter.getMessages()
        
class RemoveDuplicateIndexMessagesTask(webapp.RequestHandler):
    def post(self):
        logging.getLogger().setLevel(logging.INFO)
        duplicateIndex = self.request.get('duplicateIndex')
        duplicateIndex = int(duplicateIndex)
        logging.info("duplicate index is " + str(duplicateIndex))        
        messages = dataAccess.MessagesByIndexQuery(duplicateIndex)
        newIndex = modelInterrogator.getMaxIndex()
        newIndex += 1
        i = 0
        for message in messages:
            #Update index
            message.insertCounter = newIndex
            #don't update the first found task, as it has correct index
            if i != 0:
                logging.info('Updating message with new index ' + str(newIndex))
                message.put()
                newIndex += 1
            i += 1
        
application = webapp.WSGIApplication(
                                     [('/tasks/addComments', AddCommentsTask), 
                                      ('/tasks/removeDuplicateIndexes', RemoveDuplicateIndexMessagesTask)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()