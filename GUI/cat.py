# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(480, 420)
        MainWindow.setMinimumSize(QtCore.QSize(480, 420))
        MainWindow.setMaximumSize(QtCore.QSize(480, 420))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 480, 385))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_1)
        self.textBrowser.setGeometry(QtCore.QRect(2, 30, 470, 260))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_11.setGeometry(QtCore.QRect(100, 320, 280, 40))
        self.pushButton_11.setObjectName("pushButton_11")
        self.checkBox = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox.setGeometry(QtCore.QRect(20, 10, 50, 16))
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 10, 70, 16))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox_3.setGeometry(QtCore.QRect(150, 10, 70, 16))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox_4.setGeometry(QtCore.QRect(230, 10, 70, 16))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox_5.setGeometry(QtCore.QRect(310, 10, 70, 16))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.radioButton = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton.setGeometry(QtCore.QRect(20, 300, 89, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.spinBox = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox.setGeometry(QtCore.QRect(20, 325, 60, 30))
        self.spinBox.setMaximum(10000)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(2, 30, 470, 260))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 320, 280, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 5, 100, 20))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 5, 100, 20))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(250, 5, 100, 20))
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setGeometry(QtCore.QRect(20, 325, 60, 30))
        self.spinBox_2.setMaximum(10000)
        self.spinBox_2.setProperty("value", 10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(2, 30, 470, 260))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 320, 280, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_3.setGeometry(QtCore.QRect(20, 325, 60, 30))
        self.spinBox_3.setMaximum(10000)
        self.spinBox_3.setProperty("value", 10)
        self.spinBox_3.setDisplayIntegerBase(10)
        self.spinBox_3.setObjectName("spinBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 5, 100, 20))
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setTabletTracking(False)
        self.tab_4.setToolTip("")
        self.tab_4.setObjectName("tab_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 320, 280, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(2, 5, 470, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.spinBox_4 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_4.setGeometry(QtCore.QRect(20, 325, 60, 30))
        self.spinBox_4.setMaximum(10000)
        self.spinBox_4.setProperty("value", 10)
        self.spinBox_4.setDisplayIntegerBase(10)
        self.spinBox_4.setObjectName("spinBox_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setEnabled(True)
        self.tab_5.setAccessibleName("")
        self.tab_5.setAccessibleDescription("")
        self.tab_5.setObjectName("tab_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser_6.setGeometry(QtCore.QRect(2, 200, 470, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_2.setGeometry(QtCore.QRect(2, 157, 180, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_10.setGeometry(QtCore.QRect(290, 157, 180, 40))
        self.pushButton_10.setObjectName("pushButton_10")
        self.textEdit = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit.setGeometry(QtCore.QRect(2, 5, 470, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.layoutWidget = QtWidgets.QWidget(self.tab_6)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.CalculatorDisplay = QtWidgets.QTextBrowser(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalculatorDisplay.sizePolicy().hasHeightForWidth())
        self.CalculatorDisplay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CalculatorDisplay.setFont(font)
        self.CalculatorDisplay.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.CalculatorDisplay.setObjectName("CalculatorDisplay")
        self.gridLayout.addWidget(self.CalculatorDisplay, 0, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_2.setMinimumSize(QtCore.QSize(100, 202))
        self.textEdit_2.setMaximumSize(QtCore.QSize(100, 202))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_dot = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.gridLayout_2.addWidget(self.pushButton_dot, 2, 3, 1, 1)
        self.pushButton_Multiply = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Multiply.setObjectName("pushButton_Multiply")
        self.gridLayout_2.addWidget(self.pushButton_Multiply, 0, 2, 1, 1)
        self.pushButton0 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton0.setObjectName("pushButton0")
        self.gridLayout_2.addWidget(self.pushButton0, 6, 0, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout_2.addWidget(self.pushButton_div, 0, 3, 1, 1)
        self.pushButton_leftbrackets = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_leftbrackets.setObjectName("pushButton_leftbrackets")
        self.gridLayout_2.addWidget(self.pushButton_leftbrackets, 6, 1, 1, 1)
        self.pushButton5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton5.setObjectName("pushButton5")
        self.gridLayout_2.addWidget(self.pushButton5, 3, 1, 1, 1)
        self.pushButton_mod = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_mod.setObjectName("pushButton_mod")
        self.gridLayout_2.addWidget(self.pushButton_mod, 3, 3, 1, 1)
        self.pushButton3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout_2.addWidget(self.pushButton3, 2, 2, 1, 1)
        self.pushButton_Add = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.gridLayout_2.addWidget(self.pushButton_Add, 0, 0, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout_2.addWidget(self.pushButton1, 2, 0, 1, 1)
        self.pushButton9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton9.setObjectName("pushButton9")
        self.gridLayout_2.addWidget(self.pushButton9, 4, 2, 1, 1)
        self.pushButton8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton8.setObjectName("pushButton8")
        self.gridLayout_2.addWidget(self.pushButton8, 4, 1, 1, 1)
        self.pushButton_rightbrackets = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_rightbrackets.setObjectName("pushButton_rightbrackets")
        self.gridLayout_2.addWidget(self.pushButton_rightbrackets, 6, 2, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton6.setObjectName("pushButton6")
        self.gridLayout_2.addWidget(self.pushButton6, 3, 2, 1, 1)
        self.pushButton4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton4.setObjectName("pushButton4")
        self.gridLayout_2.addWidget(self.pushButton4, 3, 0, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout_2.addWidget(self.pushButton2, 2, 1, 1, 1)
        self.pushButton_Minus = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Minus.setObjectName("pushButton_Minus")
        self.gridLayout_2.addWidget(self.pushButton_Minus, 0, 1, 1, 1)
        self.pushButton7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton7.setObjectName("pushButton7")
        self.gridLayout_2.addWidget(self.pushButton7, 4, 0, 1, 1)
        self.pushButton_Cal = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Cal.setObjectName("pushButton_Cal")
        self.gridLayout_2.addWidget(self.pushButton_Cal, 6, 3, 1, 1)
        self.pushButton_Clear = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.gridLayout_2.addWidget(self.pushButton_Clear, 4, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 460, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 150, 160, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_9.setGeometry(QtCore.QRect(300, 150, 160, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setEnabled(True)
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wenjie\'s cat                                      By WenJie"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_11.setText(_translate("MainWindow", "随机身份生成"))
        self.checkBox.setText(_translate("MainWindow", "姓名"))
        self.checkBox_2.setText(_translate("MainWindow", "手机号"))
        self.checkBox_3.setText(_translate("MainWindow", "身份证号"))
        self.checkBox_4.setText(_translate("MainWindow", "银行卡号"))
        self.checkBox_5.setText(_translate("MainWindow", "车牌号"))
        self.radioButton.setText(_translate("MainWindow", "无头输出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "身份生成"))
        self.pushButton_5.setText(_translate("MainWindow", "身份证号生成"))
        self.comboBox.setCurrentText(_translate("MainWindow", "请选择省份"))
        self.comboBox.setItemText(0, _translate("MainWindow", "请选择省份"))
        self.comboBox.setItemText(1, _translate("MainWindow", "北京市"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "请选择城市"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "请选择城市"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "北京市"))
        self.comboBox_3.setCurrentText(_translate("MainWindow", "请选择区县"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "请选择区县"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "北京市"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "身份证号"))
        self.pushButton_6.setText(_translate("MainWindow", "银行卡号生成"))
        self.comboBox_4.setCurrentText(_translate("MainWindow", "请选择银行"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "请选择银行"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "招商银行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "银行卡号"))
        self.pushButton_7.setText(_translate("MainWindow", "UUID生成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "UUID"))
        self.pushButton_2.setText(_translate("MainWindow", "MD5加密"))
        self.pushButton_10.setText(_translate("MainWindow", "BASE64加密"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "加密"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_Multiply.setText(_translate("MainWindow", "*"))
        self.pushButton0.setText(_translate("MainWindow", "0"))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_leftbrackets.setText(_translate("MainWindow", "("))
        self.pushButton5.setText(_translate("MainWindow", "5"))
        self.pushButton_mod.setText(_translate("MainWindow", "%"))
        self.pushButton3.setText(_translate("MainWindow", "3"))
        self.pushButton_Add.setText(_translate("MainWindow", "+"))
        self.pushButton1.setText(_translate("MainWindow", "1"))
        self.pushButton9.setText(_translate("MainWindow", "9"))
        self.pushButton8.setText(_translate("MainWindow", "8"))
        self.pushButton_rightbrackets.setText(_translate("MainWindow", ")"))
        self.pushButton6.setText(_translate("MainWindow", "6"))
        self.pushButton4.setText(_translate("MainWindow", "4"))
        self.pushButton2.setText(_translate("MainWindow", "2"))
        self.pushButton_Minus.setText(_translate("MainWindow", "-"))
        self.pushButton7.setText(_translate("MainWindow", "7"))
        self.pushButton_Cal.setText(_translate("MainWindow", "="))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "计算器"))
        self.pushButton_8.setText(_translate("MainWindow", "二维码生成"))
        self.pushButton_9.setText(_translate("MainWindow", "条形码生成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "二维码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "设置"))
