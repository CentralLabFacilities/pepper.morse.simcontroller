import sys
from PyQt4 import QtGui
from simcontroller import Ui_SimController
from middleware import Talker


class Editor(QtGui.QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()
        self.ui = Ui_SimController()
        self.ui.setupUi(self)
        fake_say_service = Talker("talk")
        opendoor_service = Talker("/pepper/morse/opendoor")
        self.ui.FakeSay.clicked.connect(lambda: fake_say_service.say(self.ui.SayText.text()))
        self.ui.openDoor.clicked.connect(lambda: opendoor_service.say("open"))
        self.ui.CloseDoor.clicked.connect(lambda: opendoor_service.say("close"))
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Editor()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
