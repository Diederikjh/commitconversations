'''
Created on 04 Apr 2013

@author: drbergie
'''

from google.appengine.ext import db
from model import GitHubCommitComment
import random
from dataAccess import MessagesByIndexQuery
from Tasks import startFixMultipleInsertIndexTask
import Tasks
import logging

def getMaxIndex():
    firstResult = db.GqlQuery("SELECT * FROM GitHubCommitComment ORDER BY insertCounter DESC").get()
    if firstResult is None:
        return 0;
    else:
        return firstResult.insertCounter


def dataStoreHasMessages():
    query = db.GqlQuery("SELECT * FROM GitHubCommitComment")
    count = query.count(limit=1);
    if count == 1:
        return True
    else:
        return False


def getMessageByIDCheckingForDuplicates(randomIndex):
    randomMessageQuery = MessagesByIndexQuery(randomIndex)
    messageCount = randomMessageQuery.count(limit=5)
    if messageCount > 1:
        logging.info("Starting duplicate insert counter task")
        Tasks.startFixMultipleInsertIndexTask(randomIndex)
    return randomMessageQuery

def getRandomMessage():
    if not dataStoreHasMessages():
        Tasks.startMessageGetTask()
        logging.info("Tasks are empty")
        return None
    continueWithLoop = True;
    while continueWithLoop:
        maxIndex = getMaxIndex()
        randomIndex = random.randint(0, maxIndex)
        randomMessageQuery = getMessageByIDCheckingForDuplicates(randomIndex)
            
        randomMessages = randomMessageQuery.get()
        if randomMessages != None:
            break;
        else:
            logging.warning("Could not get message for insert value " + str(randomIndex))
    return randomMessages
    
    
def getMessageByInsertId(insertId):
    messageByIdQuery = getMessageByIDCheckingForDuplicates(insertId)
    message = messageByIdQuery.get()
    if message == None:
        logging.warning("Message with ID " + str(insertId) + " not found")
        return getRandomMessage()
    return message

def getCountRepo(repoName):
    commitMessagesQuery = db.GqlQuery("SELECT * FROM GitHubCommitComment WHERE repo = :1 ", repoName)
    return commitMessagesQuery.count()



