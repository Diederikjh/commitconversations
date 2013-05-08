'''
Created on 24 Mar 2013

@author: drbergie
'''

from google.appengine.ext import db

class GitHubCommitComment(db.Model):
    """A git hub commit comment, saved as TEXT and SHA of """
    message = db.StringProperty(multiline=True)
    owner = db.StringProperty()
    repo = db.StringProperty()
    sha = db.StringProperty()
    url = db.StringProperty()
    insertCounter = db.IntegerProperty()
