'''
Created on 31 May 2013

@author: drbergie
'''

class navItem():

    def __init__(self, name, url):
        self.name = name
        self.isActive = False
        self.url = url

    name = ""
    isActive = False
    url = ""
    
    

class navbar():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.navItems = [navItem("Doing now?", "/WAYDN"), 
                        navItem("Conversation", "/Conversation"),
                        navItem("Stream", "/Stream"),
                        navItem("About", "/About")]
        
    def setNavBarItemActive(self, navName):
        setItemActive = False
        for n in self.navItems:
            if n.name == navName:
                n.isActive = True
                setItemActive = True
                break
        if not setItemActive:
            raise Exception("Nav name " + navName + " not found")
            
    def validateList(self):
        activeCount = 0
        for n in self.navItems:
            if n.isActive == True:
                activeCount += 1
        if activeCount != 1:
            raise Exception("Incorrect amount of nav items are active")
                
    def getNavBarItemList(self):
        self.validateList()
        return self.navItems
    
