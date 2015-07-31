import os
import sys

#Constant for verify connection
FTRACK_CONNECTOR = False

sys.path += ["C:/server/apps/3rdparty/ftrack-python"]
os.environ['FTRACK_SERVER'] = 'https://cas.ftrackapp.com'

import ftrack

FTRACK_CONNECTOR = True


class Connector(object):
    """class for connector
    Args:
        user (Optional[str]): user name, and user system username if None
    """
    def __init__(self, user=None):
        super(Connector, self).__init__()

        self.user = user
        self.userDetails = None
        self.userTasks = None

        if not self.user:
            self.user = os.environ['USERNAME']

    def getUser(self):
        return self.user

    def setUser(self, value):
        self.user = value




    def connect(self):    

        os.environ['LOGNAME'] = self.user
        if FTRACK_CONNECTOR is True:
            print 'Connection Sussceful !'

    def getUserDetails(self):

        self.userDetails = ftrack.getUser(self.user)
        return self.userDetails

    def getUserTasks(self):
        self.userDetails = ftrack.getUser(self.user)
        return self.userDetails
