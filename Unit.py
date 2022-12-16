from PyQt5.QtWidgets import (QComboBox, QHBoxLayout, QWidget, QPushButton, QLabel, QLineEdit)
from PyQt5 import sip

class Unit(QWidget):
    def __init__(self):
        super(Unit, self).__init__()
        self.unitLayout = QHBoxLayout()

        label_unit = QLabel(f'<font size="4"> Unit </font>')

        self.comboBox_value = QComboBox()
        self.comboBox_value.addItems(['6', '9', '12', '15', '18'])

        self.lineEdit_location = QLineEdit()
        self.lineEdit_location.setPlaceholderText('Location')

        self.button_delUnit = QPushButton('X')
        self.button_delUnit.clicked.connect(self.delUnit)

        self.unitLayout.addWidget(label_unit)
        self.unitLayout.addWidget(self.comboBox_value)
        self.unitLayout.addWidget(self.lineEdit_location)
        self.unitLayout.addWidget(self.button_delUnit)

        self.setLayout(self.unitLayout)

    def delUnit(self):
        sip.delete(self)

