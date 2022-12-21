from PyQt5 import QtGui, sip
from PyQt5.QtWidgets import (QCheckBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget)

class Discount(QWidget):
    def __init__(self):
        super(Discount, self).__init__()
        self.discountLayout = QHBoxLayout()

        label_discount = QLabel(f'<font size="4"> Discount </font>')

        self.lineEdit_amount = QLineEdit()
        self.lineEdit_amount.setValidator(QtGui.QIntValidator(0, 200, self))
        self.lineEdit_amount.setPlaceholderText('$Amount')

        self.lineEdit_reason = QLineEdit()
        self.lineEdit_reason.setPlaceholderText('Reason')

        self.checkBox_perUnit = QCheckBox('Per')

        self.button_delDiscount = QPushButton('X')
        self.button_delDiscount.clicked.connect(self.delDiscount)
        
        self.discountLayout.addWidget(label_discount)
        self.discountLayout.addWidget(self.lineEdit_amount)
        self.discountLayout.addWidget(self.lineEdit_reason)
        self.discountLayout.addWidget(self.checkBox_perUnit)
        self.discountLayout.addWidget(self.button_delDiscount)

        self.setLayout(self.discountLayout)

    def delDiscount(self):
        sip.delete(self)

    def getLineEdit(self):
        return self.lineEdit_location