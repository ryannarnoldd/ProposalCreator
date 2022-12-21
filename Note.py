from PyQt5 import sip
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget)


class Note(QWidget):
    def __init__(self):
        super(Note, self).__init__()
        self.noteLayout = QHBoxLayout()

        label_note = QLabel(f'<font size="4"> Note </font>')

        self.lineEdit_note = QLineEdit()
        self.lineEdit_note.setPlaceholderText('Note')

        self.button_delNote = QPushButton('X')
        self.button_delNote.clicked.connect(self.delNote)

        # Add the widgets to the layout.
        widgets = [label_note, self.lineEdit_note, self.button_delNote]
        [self.noteLayout.addWidget(widget) for widget in widgets]

        self.setLayout(self.noteLayout)

    def delNote(self):
        sip.delete(self)