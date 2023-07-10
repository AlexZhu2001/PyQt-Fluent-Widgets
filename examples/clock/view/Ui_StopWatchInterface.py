# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Python_Study\Github_Repositories\PyQt-Fluent-Widgets\StopWatchInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_StopWatchInterface(object):
    def setupUi(self, StopWatchInterface):
        StopWatchInterface.setObjectName("StopWatchInterface")
        StopWatchInterface.resize(867, 781)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(StopWatchInterface)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.timeLabel = DisplayLabel(StopWatchInterface)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout.addWidget(self.timeLabel, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.hourLabel = TitleLabel(StopWatchInterface)
        self.hourLabel.setObjectName("hourLabel")
        self.horizontalLayout_3.addWidget(self.hourLabel)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.minuteLabel = TitleLabel(StopWatchInterface)
        self.minuteLabel.setObjectName("minuteLabel")
        self.horizontalLayout_3.addWidget(self.minuteLabel)
        spacerItem3 = QtWidgets.QSpacerItem(90, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.secondLabel = TitleLabel(StopWatchInterface)
        self.secondLabel.setObjectName("secondLabel")
        self.horizontalLayout_3.addWidget(self.secondLabel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(24)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.startButton = PillToolButton(StopWatchInterface)
        self.startButton.setMinimumSize(QtCore.QSize(68, 68))
        self.startButton.setIconSize(QtCore.QSize(21, 21))
        self.startButton.setChecked(True)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        self.flagButton = PillToolButton(StopWatchInterface)
        self.flagButton.setEnabled(False)
        self.flagButton.setMinimumSize(QtCore.QSize(68, 68))
        self.flagButton.setIconSize(QtCore.QSize(21, 21))
        self.flagButton.setObjectName("flagButton")
        self.horizontalLayout_2.addWidget(self.flagButton)
        self.restartButton = PillToolButton(StopWatchInterface)
        self.restartButton.setEnabled(False)
        self.restartButton.setMinimumSize(QtCore.QSize(68, 68))
        self.restartButton.setIconSize(QtCore.QSize(21, 21))
        self.restartButton.setObjectName("restartButton")
        self.horizontalLayout_2.addWidget(self.restartButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(StopWatchInterface)
        QtCore.QMetaObject.connectSlotsByName(StopWatchInterface)

    def retranslateUi(self, StopWatchInterface):
        _translate = QtCore.QCoreApplication.translate
        StopWatchInterface.setWindowTitle(_translate("StopWatchInterface", "Form"))
        self.timeLabel.setText(_translate("StopWatchInterface", "00:00:00"))
        self.hourLabel.setText(_translate("StopWatchInterface", "小时"))
        self.minuteLabel.setText(_translate("StopWatchInterface", "分钟"))
        self.secondLabel.setText(_translate("StopWatchInterface", "秒"))
from qfluentwidgets import DisplayLabel, PillToolButton, TitleLabel
