from PyQt5 import sip
from PyQt5.QtWidgets import (QComboBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget)


# Unit class.
class Unit(QWidget):
    def __init__(self):
        super(Unit, self).__init__()
        self.unitLayout = QHBoxLayout()

        label_unit = QLabel(f'<font size="4"> Unit </font>')

        # Create a combo box for the unit value (the 'BTU' value).
        self.comboBox_value = QComboBox()
        self.comboBox_value.addItems(['6', '9', '12', '15', '18'])

        # Create a line edit for the unit location (the 'Location' value).
        self.lineEdit_location = QLineEdit()
        self.lineEdit_location.setPlaceholderText('Location')

        # Create a button to delete the unit, if needed.
        self.button_delUnit = QPushButton('X')
        self.button_delUnit.clicked.connect(self.delUnit)

        # Add the widgets to the layout.
        widgets = [label_unit, self.comboBox_value, self.lineEdit_location, self.button_delUnit]
        [self.unitLayout.addWidget(widget) for widget in widgets]

        self.setLayout(self.unitLayout)

    # Delete the unit, using sip.delete().
    def delUnit(self):
        sip.delete(self)