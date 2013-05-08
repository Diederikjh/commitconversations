'''
Created on 07 Apr 2013

@author: drbergie
'''


from google.appengine.ext import db

def MessagesByIndexQuery(index):
    return db.GqlQuery("SELECT * FROM GitHubCommitComment WHERE insertCounter = :1", index)
