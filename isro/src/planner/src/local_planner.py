import rospy

class LocalPlanner:
    def __init__(self):
        self.__init__()

def main(args=None):
    try:
        planner = LocalPlanner()
        rospy.spin()
    except rospy.ROSException:
        pass
