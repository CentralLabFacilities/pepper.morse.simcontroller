import sys
from PyQt4 import QtGui
from simcontroller import Ui_SimController
from simcontroller_middleware import Talker


class Editor(QtGui.QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()
        self.ui = Ui_SimController()
        self.ui.setupUi(self)
        fake_say_service = Talker("talk")
        fake_rec_service = Talker("/pepper_robot/speechrec/context")
        opendoor_service = Talker("/pepper/morse/opendoor")
        wave_service = Talker("/pepper/morse/hri/forlan")
        self.ui.FakeSay.clicked.connect(lambda: fake_say_service.say(self.ui.SayText.text()))
        self.ui.FakeRec.clicked.connect(lambda: fake_rec_service.say(self.ui.RecText.text()))
        self.ui.openDoor.clicked.connect(lambda: opendoor_service.say("open"))
        self.ui.CloseDoor.clicked.connect(lambda: opendoor_service.say("close"))
        self.ui.waveButton.clicked.connect(lambda: wave_service.say("wave"))
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Editor()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
