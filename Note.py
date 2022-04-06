import sys
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout, QHBoxLayout, QVBoxLayout, QScrollArea, QWidget, QPushButton, QRadioButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5 import sip
from PyQt5 import QtCore, QtGui, QtWidgets

class Note(QWidget):
    def __init__(self):
        super(Note, self).__init__()
        self.noteLayout = QHBoxLayout()

        label_note = QLabel(f'<font size="4"> Note </font>')

        self.lineEdit_note = QLineEdit()
        self.lineEdit_note.setPlaceholderText('Note')

        self.button_delNote = QPushButton('X')
        self.button_delNote.clicked.connect(self.delNote)

        self.noteLayout.addWidget(label_note)
        self.noteLayout.addWidget(self.lineEdit_note)
        self.noteLayout.addWidget(self.button_delNote)

        self.setLayout(self.noteLayout)

    def delNote(self):
        sip.delete(self)
