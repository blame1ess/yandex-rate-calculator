# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSplitter, QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(480, 433)
        MainWindow.setMinimumSize(QSize(480, 433))
        MainWindow.setMaximumSize(QSize(480, 433))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setWindowTitle(u"Yandex Tariff Calculator - v1.0 - Salikh Pernebek")
        icon = QIcon()
        icon.addFile(u"yandex-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"\n"
"QPushButton {\n"
"	font-size: 15px;\n"
"	font-weight: 700;\n"
"	background-color: silver;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #ffcc01;\n"
"}\n"
"")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 200, 311, 28))
        self.splitter.setOrientation(Qt.Horizontal)
        self.radioButton_2 = QRadioButton(self.splitter)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"font-size: 20px;")
        self.splitter.addWidget(self.radioButton_2)
        self.radioButton = QRadioButton(self.splitter)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"font-size: 20px;\n"
"")
        self.splitter.addWidget(self.radioButton)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 40, 111, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 111, 51))
        self.label.setStyleSheet(u"font-weight: 700;\n"
"font-size: 15px;\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 10, 201, 31))
        self.label_3.setStyleSheet(u"font-weight: 700;\n"
"font-size: 15px;\n"
"")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(210, 40, 201, 31))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 120, 111, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 61, 16))
        self.label_2.setStyleSheet(u"font-weight: 700;\n"
"font-size: 15px;\n"
"")
        self.PushButton = QPushButton(self.centralwidget)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setGeometry(QRect(120, 270, 241, 41))
        self.PushButton.setStyleSheet(u"")
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(70, 330, 341, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u044c\u0435\u0440", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u0440\u0435\u0441\u0441", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0438\u043b\u043b\u043e\u043c\u0435\u0442\u0440\u044b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430", None))
        self.lineEdit_3.setText("")
        self.lineEdit_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0443\u0442\u044b", None))
        self.PushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        pass
    # retranslateUi

#### Created by Salikh Pernebek v1.0 ####
