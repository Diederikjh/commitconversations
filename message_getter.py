

from github import Github, GithubException
from random import shuffle
from random import choice
import json
from model import GitHubCommitComment

from google.appengine.ext import db
from modelInterrogator import getMaxIndex
#  Script to return three random commit comments from github
## Depends on http://jacquev6.github.com/PyGithub/introduction.html
# 
# final goal is to generate a cartoon with speachbubbles based on these data sets
#
#  Title ideas:
#     git hub converstions
#     git hub prose   
#
#
#  TODO:
#    - save commit URL for direct access.
#    - MAke cron job get x amount of commit messages.
#    -  Show 3 random messages in a sensable way
#

class CommitComment:
    message = ""
    sha = ""
    def __init__(self, message, sha, owner, repo):
        self.message = message
        self.sha = sha
        self.owner = owner
        self.repo = repo
        

def getExistingComment(sha, repoName, ownerName):
    commitMessages = db.GqlQuery("SELECT * FROM GitHubCommitComment WHERE owner = :1 AND repo = :2 AND sha = :3 LIMIT 1", ownerName, repoName, sha)
    if commitMessages.count(limit=1) > 0:
        return commitMessages[0]
    else:
        return None

def getMessages():
    MAX_REPO_COUNT = 5
    MAX_COMMIT_COUNT = 3
    
    json_data=open('files/githubcredentials.json')
    data = json.load(json_data)
    json_data.close()
    
    githubUsername = data["username"]
    githubPassword = data["password"]
    
    g = Github(githubUsername, githubPassword)
    
    # TODO rather list repos http://developer.github.com/v3/repos/#list-all-repositories with random Id to get Random repos
    words =  open('files/worddata.txt').read().split()
    randomWord = choice(words)
    #Gets NO repos   
    #randomWord = "housefalls"
    #gets empty repo
    #randomWord = "livers"
    print(randomWord)
    pagedRepos = g.legacy_search_repos(randomWord)
    
    currentMaxIndex = getMaxIndex()
    
    commentClassList = []
    repoCount = 0
    commitCount = 0
    for repo in pagedRepos:
        print(repo.full_name)
        pagedCommits = repo.get_commits()
        repoCount = repoCount + 1
        try:  
            for commit in pagedCommits:
                gitcommit = commit.commit
                comment = gitcommit.message
                sha = gitcommit.sha
                ownerName = repo.owner.name
                if len(comment.strip) == 0:
                    continue
                s = CommitComment(comment, sha, repo.full_name, ownerName)
                commitcoment = getExistingComment(sha, repo.full_name, ownerName)
                if commitcoment == None:
                    commitcoment = GitHubCommitComment()    
                # if comment empty - don't save
                commitcoment.message = comment
                commitcoment.sha = sha 
                commitcoment.repo = repo.full_name
                commitcoment.owner = ownerName
                commitcoment.url = commit.url
                commitcoment.insertCounter = currentMaxIndex + commitCount
                commitcoment.put()
                commentClassList.append(s)
                commitCount += 1
                if commitCount >= MAX_COMMIT_COUNT:
                    break
        except GithubException as e:
            # Usually empty repository exception
            print(e) 
        if repoCount >= MAX_REPO_COUNT:
            break
    
    messages = [];
    if (len(commentClassList) >= 3):        
        shuffle(commentClassList)
        messages.append(commentClassList[0])
        messages.append(commentClassList[1])
        messages.append(commentClassList[2])
        encoding = 'utf-8'
        print commentClassList[0].message.encode(encoding)
        print commentClassList[1].message.encode(encoding)
        print commentClassList[2].message.encode(encoding)
        return messages

    