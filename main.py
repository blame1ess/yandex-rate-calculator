
import sys
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

from ui import Ui_MainWindow

from excel import calculation_courier, calculation_express


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PushButton.clicked.connect(self.km)

    def km(self):
        if self.ui.radioButton_2.isChecked():
            a = self.ui.lineEdit.text()
            distance = int(a)
            city = self.ui.lineEdit_3.text()
            self.ui.lineEdit_4.setText(str(calculation_courier(distance, city)))
        elif self.ui.radioButton.isChecked():
            a = self.ui.lineEdit.text()
            distance = int(a)
            city = self.ui.lineEdit_3.text()
            time_str = self.ui.lineEdit_2.text()
            if time_str == "":
                time_str = 0
            self.ui.lineEdit_4.setText(str(calculation_express(distance, city, time_str)))


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

#### Created by Salikh Pernebek v1.0 ####