import threading

class LauncherManager(object):
    def __init__(self):
        self.name = self.__class__.__name__



class Manager(object):
    def new_thread(self):
        return TrackerEndPointManager(parent=self)

    def on_tracker_end_point_checked(self, thread, data):
        print(thread, data)

class TrackerEndPointManager(threading.Thread):
    def __init__(self, parent=None):
        self.parent = parent
        super(TrackerEndPointManager, self).__init__()

    def run(self):
        main()
#