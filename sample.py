from vtinysched import VTinySched

def TaskExecuteOnce():
    print("TaskExecuteOnce")
    return False

class TaskExecuteTwoTimes(object):

    def __init__(self):
        self.__executes = 2
    
    def __call__(self):
        print("TaskExecuteTwoTimes")
        self.__executes -= 1
        return self.__executes > 0


class TaskExecuteThreeTimes(object):

    def __init__(self):
        self.__executes = 3
    
    def __call__(self):
        print("TaskExecuteThreeTimes")
        self.__executes -= 1
        return self.__executes > 0

sched = VTinySched()
sched.register(TaskExecuteOnce)
sched.register(TaskExecuteTwoTimes())
sched.register(TaskExecuteThreeTimes())
sched.execute()
