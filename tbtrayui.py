# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/greg/PycharmProjects/tbtray/tbtrayui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(674, 492)
        icon = QtGui.QIcon.fromTheme("thunderbird")
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 160))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 160))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setMinimumSize(QtCore.QSize(0, 36))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineedit_defulticon = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineedit_defulticon.setMinimumSize(QtCore.QSize(400, 0))
        self.lineedit_defulticon.setObjectName("lineedit_defulticon")
        self.horizontalLayout_4.addWidget(self.lineedit_defulticon)
        self.toolButton_defaulticon = QtWidgets.QToolButton(self.groupBox_6)
        self.toolButton_defaulticon.setObjectName("toolButton_defaulticon")
        self.horizontalLayout_4.addWidget(self.toolButton_defaulticon)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setMinimumSize(QtCore.QSize(0, 36))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineedit_notifyicon = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineedit_notifyicon.setMinimumSize(QtCore.QSize(400, 0))
        self.lineedit_notifyicon.setObjectName("lineedit_notifyicon")
        self.horizontalLayout_5.addWidget(self.lineedit_notifyicon)
        self.toolButton_notifyicon = QtWidgets.QToolButton(self.groupBox_6)
        self.toolButton_notifyicon.setObjectName("toolButton_notifyicon")
        self.horizontalLayout_5.addWidget(self.toolButton_notifyicon)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkbox_minimizetotray = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkbox_minimizetotray.setMinimumSize(QtCore.QSize(0, 0))
        self.checkbox_minimizetotray.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.checkbox_minimizetotray.setObjectName("checkbox_minimizetotray")
        self.horizontalLayout_6.addWidget(self.checkbox_minimizetotray)
        self.checkbox_showcount = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkbox_showcount.setObjectName("checkbox_showcount")
        self.horizontalLayout_6.addWidget(self.checkbox_showcount)
        self.pushButton_colourpicker = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_colourpicker.setObjectName("pushButton_colourpicker")
        self.horizontalLayout_6.addWidget(self.pushButton_colourpicker)
        self.label_colour = QtWidgets.QLabel(self.groupBox_6)
        self.label_colour.setObjectName("label_colour")
        self.horizontalLayout_6.addWidget(self.label_colour)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_notifysound = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_notifysound.setObjectName("checkBox_notifysound")
        self.horizontalLayout_8.addWidget(self.checkBox_notifysound)
        self.lineEdit_notifysound = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_notifysound.setObjectName("lineEdit_notifysound")
        self.horizontalLayout_8.addWidget(self.lineEdit_notifysound)
        self.toolButton_notifysound = QtWidgets.QToolButton(self.groupBox_4)
        self.toolButton_notifysound.setObjectName("toolButton_notifysound")
        self.horizontalLayout_8.addWidget(self.toolButton_notifysound)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.checkBox_popup = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_popup.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_popup.setMaximumSize(QtCore.QSize(120, 16777215))
        self.checkBox_popup.setObjectName("checkBox_popup")
        self.horizontalLayout_13.addWidget(self.checkBox_popup)
        self.checkBox_fixedwidth = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_fixedwidth.setObjectName("checkBox_fixedwidth")
        self.horizontalLayout_13.addWidget(self.checkBox_fixedwidth)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_13.addWidget(self.label_4)
        self.spinBox_displaytime = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_displaytime.setMinimum(1)
        self.spinBox_displaytime.setProperty("value", 10)
        self.spinBox_displaytime.setObjectName("spinBox_displaytime")
        self.horizontalLayout_13.addWidget(self.spinBox_displaytime)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_13.addWidget(self.label_3)
        self.spinBox_xpos = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_xpos.setMinimumSize(QtCore.QSize(99, 0))
        self.spinBox_xpos.setMaximum(10000)
        self.spinBox_xpos.setProperty("value", 1585)
        self.spinBox_xpos.setObjectName("spinBox_xpos")
        self.horizontalLayout_13.addWidget(self.spinBox_xpos)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.radioButton_top = QtWidgets.QRadioButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setKerning(True)
        self.radioButton_top.setFont(font)
        self.radioButton_top.setObjectName("radioButton_top")
        self.horizontalLayout_12.addWidget(self.radioButton_top)
        self.radioButton_bottom = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_bottom.setObjectName("radioButton_bottom")
        self.horizontalLayout_12.addWidget(self.radioButton_bottom)
        self.checkBox_favicons = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_favicons.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_favicons.setObjectName("checkBox_favicons")
        self.horizontalLayout_12.addWidget(self.checkBox_favicons)
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.horizontalSlider_opacity = QtWidgets.QSlider(self.groupBox_5)
        self.horizontalSlider_opacity.setMinimumSize(QtCore.QSize(210, 0))
        self.horizontalSlider_opacity.setMaximum(100)
        self.horizontalSlider_opacity.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_opacity.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_opacity.setObjectName("horizontalSlider_opacity")
        self.horizontalLayout_12.addWidget(self.horizontalSlider_opacity)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.toolButton_firepopup = QtWidgets.QPushButton(self.groupBox_5)
        self.toolButton_firepopup.setMinimumSize(QtCore.QSize(0, 0))
        self.toolButton_firepopup.setMaximumSize(QtCore.QSize(84, 16777215))
        self.toolButton_firepopup.setObjectName("toolButton_firepopup")
        self.verticalLayout_4.addWidget(self.toolButton_firepopup)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editline_profilepath = QtWidgets.QLineEdit(self.groupBox)
        self.editline_profilepath.setObjectName("editline_profilepath")
        self.horizontalLayout.addWidget(self.editline_profilepath)
        self.toolButton_profilepath = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_profilepath.setObjectName("toolButton_profilepath")
        self.horizontalLayout.addWidget(self.toolButton_profilepath)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_accountwarrning = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_accountwarrning.setFont(font)
        self.label_accountwarrning.setText("")
        self.label_accountwarrning.setScaledContents(True)
        self.label_accountwarrning.setObjectName("label_accountwarrning")
        self.horizontalLayout_3.addWidget(self.label_accountwarrning)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pushButton_add = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_3.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.horizontalLayout_3.addWidget(self.pushButton_remove)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.pushButton_ok = QtWidgets.QPushButton(self.frame)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_2.addWidget(self.pushButton_ok)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TBTray Settings"))
        self.groupBox_6.setTitle(_translate("Form", "Tray Icon"))
        self.label_5.setText(_translate("Form", "Default Icon Path"))
        self.toolButton_defaulticon.setText(_translate("Form", "..."))
        self.label_6.setText(_translate("Form", "Notify Icon Path"))
        self.toolButton_notifyicon.setText(_translate("Form", "..."))
        self.checkbox_minimizetotray.setText(_translate("Form", "Minimize to tray"))
        self.checkbox_showcount.setText(_translate("Form", "Show unread Count"))
        self.pushButton_colourpicker.setText(_translate("Form", "Colour Picker"))
        self.label_colour.setText(_translate("Form", "Colour of unread count font"))
        self.groupBox_4.setTitle(_translate("Form", "Notify Sound"))
        self.checkBox_notifysound.setText(_translate("Form", "On/Off"))
        self.toolButton_notifysound.setText(_translate("Form", "..."))
        self.groupBox_5.setTitle(_translate("Form", "Popup"))
        self.checkBox_popup.setText(_translate("Form", "ON/OFF"))
        self.checkBox_fixedwidth.setToolTip(_translate("Form", "Fixed or variable width popup"))
        self.checkBox_fixedwidth.setText(_translate("Form", "Fixed Width"))
        self.label_4.setText(_translate("Form", "   Display Time"))
        self.spinBox_displaytime.setSuffix(_translate("Form", " sec\'s"))
        self.label_3.setText(_translate("Form", "Popup X position"))
        self.spinBox_xpos.setSuffix(_translate("Form", " px"))
        self.radioButton_top.setText(_translate("Form", "&Top-Right"))
        self.radioButton_bottom.setText(_translate("Form", "Bottom-Right"))
        self.checkBox_favicons.setText(_translate("Form", "Show Mail Favicons"))
        self.label.setText(_translate("Form", "    Opacity"))
        self.toolButton_firepopup.setText(_translate("Form", "Popup Test"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "General"))
        self.groupBox.setTitle(_translate("Form", "Profile Path selector"))
        self.toolButton_profilepath.setText(_translate("Form", "..."))
        self.label_2.setText(_translate("Form", "Profile List  ( .msf files)"))
        self.pushButton_add.setText(_translate("Form", "Add"))
        self.pushButton_remove.setText(_translate("Form", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Accounts"))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))
        self.pushButton_ok.setText(_translate("Form", "OK"))

