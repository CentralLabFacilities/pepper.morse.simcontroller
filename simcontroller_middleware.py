import rospy
from std_msgs.msg import String


class Talker:
    def __init__(self, topic):
        self.topic = topic
        self.pub = rospy.Publisher(str(self.topic), String, queue_size=10)
        rospy.init_node('sim_controller_talker', anonymous=True)

    def say(self, text):
        print "Sending Talk String '%s' via %s" % (text, self.topic)
        self.pub.publish(str(text))
