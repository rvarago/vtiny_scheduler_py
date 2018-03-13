# -*- coding: utf-8 -*-
""" A very simple scheduler to register and schedule tasks for execution 
 @author rvarago

 Example:
    sched = VTintySched()
    
    sched.register(task1)
    sched.register(task2)

    sched.execute()
"""

class VTinySched(object):
    
    def __init__(self):
        self.__taskPool = []

    def register(self, task):
        """ Append a new task at the end of the pool """
        self.__taskPool.append(task)
    
    def __len__(self):
        """ Pool size """
        return len(self.__taskPool)
    
    def execute(self):
        """ Executes the tasks while the pool has pending tasks """
        while len(self):
            currentTask = self.__taskPool.pop(0)
            if currentTask() == True:
                # The task returns True if it needs to be repeated
                self.register(currentTask)
