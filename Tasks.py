'''
Created on 20 Apr 2013

@author: drbergie
'''

from google.appengine.api import taskqueue

def startFixMultipleInsertIndexTask(randomIndex):
    taskqueue.add(url='/tasks/removeDuplicateIndexes', params={'duplicateIndex': randomIndex})
    
def startMessageGetTask():
    taskqueue.add(url='/tasks/addComments')