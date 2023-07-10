# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Python_Study\Github_Repositories\PyQt-Fluent-Widgets\FocusInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_FocusInterface(object):
    def setupUi(self, FocusInterface):
        FocusInterface.setObjectName("FocusInterface")
        FocusInterface.resize(911, 807)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(FocusInterface)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(32, 40, 32, -1)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.focusCard = CardWidget(FocusInterface)
        self.focusCard.setMinimumSize(QtCore.QSize(380, 424))
        self.focusCard.setMaximumSize(QtCore.QSize(410, 424))
        self.focusCard.setStyleSheet("")
        self.focusCard.setObjectName("focusCard")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.focusCard)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pinButton = TransparentToolButton(self.focusCard)
        self.pinButton.setObjectName("pinButton")
        self.horizontalLayout_2.addWidget(self.pinButton)
        self.moreButton = TransparentToolButton(self.focusCard)
        self.moreButton.setObjectName("moreButton")
        self.horizontalLayout_2.addWidget(self.moreButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.prepareFocusLabel = SubtitleLabel(self.focusCard)
        self.prepareFocusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.prepareFocusLabel.setObjectName("prepareFocusLabel")
        self.verticalLayout.addWidget(self.prepareFocusLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.hintLabel = BodyLabel(self.focusCard)
        self.hintLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hintLabel.setObjectName("hintLabel")
        self.verticalLayout.addWidget(self.hintLabel)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.timePicker = TimePicker(self.focusCard)
        self.timePicker.setObjectName("timePicker")
        self.verticalLayout.addWidget(self.timePicker, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.bottomHintLabel = BodyLabel(self.focusCard)
        self.bottomHintLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bottomHintLabel.setObjectName("bottomHintLabel")
        self.verticalLayout.addWidget(self.bottomHintLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.skipRelaxCheckBox = CheckBox(self.focusCard)
        self.skipRelaxCheckBox.setEnabled(True)
        self.skipRelaxCheckBox.setObjectName("skipRelaxCheckBox")
        self.verticalLayout.addWidget(self.skipRelaxCheckBox, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.startFocusButton = PrimaryPushButton(self.focusCard)
        self.startFocusButton.setAutoDefault(True)
        self.startFocusButton.setObjectName("startFocusButton")
        self.verticalLayout.addWidget(self.startFocusButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.focusCard, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressCard = CardWidget(FocusInterface)
        self.progressCard.setMinimumSize(QtCore.QSize(380, 424))
        self.progressCard.setMaximumSize(QtCore.QSize(410, 424))
        self.progressCard.setObjectName("progressCard")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.progressCard)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dailyProgressLabel = StrongBodyLabel(self.progressCard)
        self.dailyProgressLabel.setObjectName("dailyProgressLabel")
        self.horizontalLayout_4.addWidget(self.dailyProgressLabel)
        self.editButton = TransparentToolButton(self.progressCard)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_4.addWidget(self.editButton, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.yesterdayLabel = BodyLabel(self.progressCard)
        self.yesterdayLabel.setObjectName("yesterdayLabel")
        self.verticalLayout_5.addWidget(self.yesterdayLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.yesterdayTimeLabel = LargeTitleLabel(self.progressCard)
        self.yesterdayTimeLabel.setObjectName("yesterdayTimeLabel")
        self.verticalLayout_5.addWidget(self.yesterdayTimeLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.minuteLabel1 = BodyLabel(self.progressCard)
        self.minuteLabel1.setObjectName("minuteLabel1")
        self.verticalLayout_5.addWidget(self.minuteLabel1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.progressRing = ProgressRing(self.progressCard)
        self.progressRing.setMinimumSize(QtCore.QSize(150, 150))
        self.progressRing.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.progressRing.setFont(font)
        self.progressRing.setMaximum(24)
        self.progressRing.setProperty("value", 10)
        self.progressRing.setTextVisible(True)
        self.progressRing.setOrientation(QtCore.Qt.Horizontal)
        self.progressRing.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressRing.setUseAni(False)
        self.progressRing.setVal(10.0)
        self.progressRing.setStrokeWidth(15)
        self.progressRing.setObjectName("progressRing")
        self.horizontalLayout_5.addWidget(self.progressRing)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem11)
        self.continousComplianceDayLabel = BodyLabel(self.progressCard)
        self.continousComplianceDayLabel.setObjectName("continousComplianceDayLabel")
        self.verticalLayout_6.addWidget(self.continousComplianceDayLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.compianceDayLabel = LargeTitleLabel(self.progressCard)
        self.compianceDayLabel.setObjectName("compianceDayLabel")
        self.verticalLayout_6.addWidget(self.compianceDayLabel, 0, QtCore.Qt.AlignHCenter)
        self.dayLabel = BodyLabel(self.progressCard)
        self.dayLabel.setObjectName("dayLabel")
        self.verticalLayout_6.addWidget(self.dayLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem12)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.finishTimeLabel = BodyLabel(self.progressCard)
        self.finishTimeLabel.setObjectName("finishTimeLabel")
        self.verticalLayout_2.addWidget(self.finishTimeLabel, 0, QtCore.Qt.AlignHCenter)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.progressCard, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(FocusInterface)
        QtCore.QMetaObject.connectSlotsByName(FocusInterface)

    def retranslateUi(self, FocusInterface):
        _translate = QtCore.QCoreApplication.translate
        FocusInterface.setWindowTitle(_translate("FocusInterface", "Form"))
        self.prepareFocusLabel.setText(_translate("FocusInterface", "准备专注"))
        self.hintLabel.setText(_translate("FocusInterface", "我们将在每个会话期间关闭通知和应用警报。对于\n"
"较长的会话，我们将添加简短的休息时间，以便你\n"
"可以恢复精力。"))
        self.bottomHintLabel.setText(_translate("FocusInterface", "你将没有休息时间。"))
        self.skipRelaxCheckBox.setText(_translate("FocusInterface", "跳过休息"))
        self.startFocusButton.setText(_translate("FocusInterface", "启动专注时段"))
        self.dailyProgressLabel.setText(_translate("FocusInterface", "每日进度"))
        self.yesterdayLabel.setText(_translate("FocusInterface", "昨天"))
        self.yesterdayTimeLabel.setText(_translate("FocusInterface", "0"))
        self.minuteLabel1.setText(_translate("FocusInterface", "分钟"))
        self.progressRing.setFormat(_translate("FocusInterface", "目标 %v 小时"))
        self.continousComplianceDayLabel.setText(_translate("FocusInterface", "连续达标日"))
        self.compianceDayLabel.setText(_translate("FocusInterface", "0"))
        self.dayLabel.setText(_translate("FocusInterface", "天"))
        self.finishTimeLabel.setText(_translate("FocusInterface", "已完成：0 分钟"))
from qfluentwidgets import BodyLabel, CardWidget, CheckBox, LargeTitleLabel, PrimaryPushButton, ProgressRing, StrongBodyLabel, SubtitleLabel, TimePicker, TransparentToolButton
