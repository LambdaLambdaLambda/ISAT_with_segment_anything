# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'COCO_to_ISAT_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(514, 202)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_save_root = QtWidgets.QPushButton(self.widget)
        self.pushButton_save_root.setObjectName("pushButton_save_root")
        self.gridLayout.addWidget(self.pushButton_save_root, 3, 1, 1, 1)
        self.pushButton_label_path = QtWidgets.QPushButton(self.widget)
        self.pushButton_label_path.setObjectName("pushButton_label_path")
        self.gridLayout.addWidget(self.pushButton_label_path, 2, 1, 1, 1)
        self.lineEdit_save_root = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_save_root.setEnabled(True)
        self.lineEdit_save_root.setReadOnly(True)
        self.lineEdit_save_root.setObjectName("lineEdit_save_root")
        self.gridLayout.addWidget(self.lineEdit_save_root, 3, 0, 1, 1)
        self.lineEdit_label_path = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_label_path.setEnabled(True)
        self.lineEdit_label_path.setReadOnly(True)
        self.lineEdit_label_path.setObjectName("lineEdit_label_path")
        self.gridLayout.addWidget(self.lineEdit_label_path, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.checkBox_keepcrowd = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_keepcrowd.setObjectName("checkBox_keepcrowd")
        self.horizontalLayout_2.addWidget(self.checkBox_keepcrowd)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_info = QtWidgets.QLabel(self.widget_4)
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.horizontalLayout_3.addWidget(self.label_info)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_cache = QtWidgets.QPushButton(self.widget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/关闭_close-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cache.setIcon(icon)
        self.pushButton_cache.setObjectName("pushButton_cache")
        self.horizontalLayout.addWidget(self.pushButton_cache)
        self.pushButton_apply = QtWidgets.QPushButton(self.widget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/校验_check-one.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_apply.setIcon(icon1)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout.addWidget(self.pushButton_apply)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ISAT to VOC png"))
        self.pushButton_save_root.setText(_translate("Dialog", "Save root"))
        self.pushButton_label_path.setText(_translate("Dialog", "Json path"))
        self.lineEdit_save_root.setPlaceholderText(_translate("Dialog", "ISAT jsons save root"))
        self.lineEdit_label_path.setPlaceholderText(_translate("Dialog", "COCO json path"))
        self.checkBox_keepcrowd.setText(_translate("Dialog", "Keep crowd"))
        self.label.setText(_translate("Dialog", "Convert COCO json to ISAT jsons."))
        self.pushButton_cache.setText(_translate("Dialog", "cache"))
        self.pushButton_apply.setText(_translate("Dialog", "convert"))
import icons_rc