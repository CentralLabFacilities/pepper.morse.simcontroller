# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simcontroller.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SimController(object):
    def setupUi(self, SimController):
        SimController.setObjectName(_fromUtf8("SimController"))
        SimController.resize(644, 453)
        self.centralWidget = QtGui.QWidget(SimController)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 611, 371))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.openDoor = QtGui.QPushButton(self.tab)
        self.openDoor.setGeometry(QtCore.QRect(10, 20, 99, 27))
        self.openDoor.setObjectName(_fromUtf8("openDoor"))
        self.CloseDoor = QtGui.QPushButton(self.tab)
        self.CloseDoor.setGeometry(QtCore.QRect(10, 50, 99, 27))
        self.CloseDoor.setObjectName(_fromUtf8("CloseDoor"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.FakeSay = QtGui.QPushButton(self.tab_2)
        self.FakeSay.setGeometry(QtCore.QRect(10, 20, 99, 27))
        self.FakeSay.setObjectName(_fromUtf8("FakeSay"))
        self.FakeRec = QtGui.QPushButton(self.tab_2)
        self.FakeRec.setGeometry(QtCore.QRect(10, 60, 99, 27))
        self.FakeRec.setObjectName(_fromUtf8("FakeRec"))
        self.SayText = QtGui.QLineEdit(self.tab_2)
        self.SayText.setGeometry(QtCore.QRect(120, 20, 481, 27))
        self.SayText.setObjectName(_fromUtf8("SayText"))
        self.RecText = QtGui.QLineEdit(self.tab_2)
        self.RecText.setGeometry(QtCore.QRect(120, 60, 481, 27))
        self.RecText.setObjectName(_fromUtf8("RecText"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.waveButton = QtGui.QPushButton(self.tab_3)
        self.waveButton.setGeometry(QtCore.QRect(10, 20, 151, 27))
        self.waveButton.setObjectName(_fromUtf8("pushButton"))
        # self.HumanWave = QtGui.QLineEdit(self.tab_3)
        # self.HumanWave.setGeometry(QtCore.QRect(170, 20, 141, 27))
        # self.HumanWave.setObjectName(_fromUtf8("HumanWave"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        SimController.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(SimController)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        SimController.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(SimController)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        SimController.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(SimController)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 644, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuPepper_Sim_Controller = QtGui.QMenu(self.menuBar)
        self.menuPepper_Sim_Controller.setObjectName(_fromUtf8("menuPepper_Sim_Controller"))
        SimController.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuPepper_Sim_Controller.menuAction())

        self.retranslateUi(SimController)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SimController)

    def retranslateUi(self, SimController):
        SimController.setWindowTitle(_translate("SimController", "SimController", None))
        self.openDoor.setText(_translate("SimController", "Open Door", None))
        self.CloseDoor.setText(_translate("SimController", "Close Door", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SimController", "Environment", None))
        self.FakeSay.setText(_translate("SimController", "Fake Say", None))
        self.FakeRec.setText(_translate("SimController", "Fake Rec", None))
        self.SayText.setText(_translate("SimController", "Max", None))
        self.RecText.setText(_translate("SimController", "Max", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SimController", "Speech", None))
        self.waveButton.setText(_translate("SimController", "Make Forlan Wave", None))
        # self.HumanWave.setText(_translate("SimController", "Max", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SimController", "HRI", None))
        self.menuPepper_Sim_Controller.setTitle(_translate("SimController", "Pepper Sim Controller", None))

