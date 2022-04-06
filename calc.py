import sys
import Unit
from PyQt5.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout, QVBoxLayout, QScrollArea, QWidget, QPushButton, QRadioButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5 import sip
from PyQt5 import QtCore, QtGui, QtWidgets

class Calculator(QWidget):
    def __init__(self):
        w = 300
        h = 300
        super(Calculator, self).__init__()
        self.setWindowTitle('Proposal Calculator')
        self.setGeometry((1680/2 - w/2), (1050/2 - h/2), w, h)
        self.resize(w, h)

        layout = QVBoxLayout()
        enterLayout = QGridLayout()
        inputLayout = QVBoxLayout()
        unitsLayout = QVBoxLayout()
        unitsButtonLayout = QGridLayout()
        self.unitsFormLayout = QVBoxLayout()

        displayLayout = QVBoxLayout()

        label_size = QLabel('<font size="4">Size:</font>')
        self.lineEdit_w = QLineEdit()
        self.lineEdit_w.setValidator(QtGui.QIntValidator(0, 200, self))
        self.lineEdit_w.setPlaceholderText('W')
        self.lineEdit_h = QLineEdit()
        self.lineEdit_h.setValidator(QtGui.QIntValidator(0, 200, self))
        self.lineEdit_h.setPlaceholderText('H')
        enterLayout.addWidget(label_size, 0, 0)
        enterLayout.addWidget(self.lineEdit_w, 0, 1)
        enterLayout.addWidget(self.lineEdit_h, 0, 2)

        label_temp = QLabel('<font size="4">Temp:</font>')
        self.comboBox_author = QComboBox()
        self.comboBox_author.addItems(['2', '5', '6', '9'])
        self.comboBox_author.setCurrentText('5')
        enterLayout.addWidget(label_temp, 1, 0)
        enterLayout.addWidget(self.comboBox_author, 1, 1)

        label_BTU = QLabel('<font size="4">Average BTU:</font>')
        self.lineEdit_btu = QLineEdit()
        self.lineEdit_btu.setValidator(QtGui.QIntValidator(0, 100, self))
        self.lineEdit_btu.setPlaceholderText('BTU')
        enterLayout.addWidget(label_BTU, 2, 0)
        enterLayout.addWidget(self.lineEdit_btu, 2, 1)

        inputLayout.addLayout(enterLayout)

        scroll_units = QScrollArea()
        scroll_units.setWidgetResizable(True)
        scroll_units.setFixedHeight(100)
        scroll_units.setFixedWidth(200)
        scroll_units_widget = QWidget()
        scroll_units_widget.setLayout(self.unitsFormLayout)
        self.unitsFormLayout.addStretch()
        self.unitsFormLayout.setDirection(QVBoxLayout.TopToBottom)
        scroll_units.setWidget(scroll_units_widget)

        unitsLayout.addLayout(unitsButtonLayout)
        unitsLayout.addWidget(scroll_units)

        inputLayout.addLayout(unitsLayout)

        inputLayout.addLayout(enterLayout)

        layout.addLayout(inputLayout)

        self.setLayout(layout)

    def delUnit(self):
        sip.delete(self)

    def addUnit(self):
        numOfUnits = len(self.getWidgets(self.unitsFormLayout))-1
        self.unitsFormLayout.insertWidget(numOfUnits, Unit.Unit() )

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def getWidgets(self, tempLayout):
        tempList = []
        for i in range(tempLayout.count()):
            tempList.append(tempLayout.itemAt(i).widget())
        return tempList


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Calculator()
    form.show()

    sys.exit(app.exec_())
