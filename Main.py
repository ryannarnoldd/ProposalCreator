import Proposal
import Unit
import Discount
import Note
import sys
from PyQt5.QtWidgets import *

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        w = 1680
        h = 300
        self.setWindowTitle('Proposal Creator')
        self.setGeometry(int(1680/2 - w/2), int(1050/2 - h/2), w, h)
        self.resize(w, h)
        #self.setStyleSheet('background-color: rgb(255, 255, 255)')

        layout = QVBoxLayout()
        formsLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()
        homeownerLayout = QGridLayout()

        unitsLayout = QVBoxLayout()
        unitsButtonLayout = QGridLayout()
        self.unitsFormLayout = QVBoxLayout()

        discountsLayout = QVBoxLayout()
        discountsButtonLayout = QGridLayout()
        self.discountsFormLayout = QVBoxLayout()

        notesLayout = QVBoxLayout()
        notesButtonLayout = QGridLayout()
        self.notesFormLayout = QVBoxLayout()

        extraLayout = QGridLayout()

        label_name = QLabel('<font size="4">Name:</font>')
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText('Name')
        homeownerLayout.addWidget(label_name, 0, 0)
        homeownerLayout.addWidget(self.lineEdit_name, 0, 1)

        label_street = QLabel('<font size="4">Street:</font>')
        self.lineEdit_street = QLineEdit()
        self.lineEdit_street.setPlaceholderText('Address')
        homeownerLayout.addWidget(label_street, 1, 0)
        homeownerLayout.addWidget(self.lineEdit_street, 1, 1)

        label_town = QLabel('<font size="4">Town:</font>')
        self.lineEdit_town = QLineEdit()
        self.lineEdit_town.setPlaceholderText('Town')
        homeownerLayout.addWidget(label_town, 2, 0)
        homeownerLayout.addWidget(self.lineEdit_town, 2, 1)

        label_zipcode = QLabel('<font size="4">Zipcode:</font>')
        self.lineEdit_zipcode = QLineEdit()
        self.lineEdit_zipcode.setPlaceholderText('Zipcode')
        homeownerLayout.addWidget(label_zipcode, 3, 0)
        homeownerLayout.addWidget(self.lineEdit_zipcode, 3, 1)

        label_phone = QLabel('<font size="4">Phone:</font>')
        self.lineEdit_phone = QLineEdit()
        self.lineEdit_phone.setPlaceholderText('XXX-YYY-ZZZZ')
        homeownerLayout.addWidget(label_phone, 4, 0)
        homeownerLayout.addWidget(self.lineEdit_phone, 4, 1)

        label_email = QLabel('<font size="4">Email:</font>')
        self.lineEdit_email = QLineEdit()
        self.lineEdit_email.setPlaceholderText('anyone@email.com')
        homeownerLayout.addWidget(label_email, 5, 0)
        homeownerLayout.addWidget(self.lineEdit_email, 5, 1)

        formsLayout.addLayout(homeownerLayout)

        label_units = QLabel('<font size="4">Units:</font>')
        self.button_units = QPushButton('Add Unit')
        self.button_units.clicked.connect(self.addUnit)
        unitsButtonLayout.addWidget(label_units, 0, 0)
        unitsButtonLayout.addWidget(self.button_units, 0, 1)

        scroll_units = QScrollArea()
        scroll_units.setWidgetResizable(True)
        scroll_units.setFixedHeight(400)
        scroll_units.setFixedWidth(300)
        scroll_units_widget = QWidget()
        scroll_units_widget.setLayout(self.unitsFormLayout)
        self.unitsFormLayout.addStretch()
        self.unitsFormLayout.setDirection(QVBoxLayout.TopToBottom)
        scroll_units.setWidget(scroll_units_widget)

        unitsLayout.addLayout(unitsButtonLayout)
        unitsLayout.addWidget(scroll_units)

        formsLayout.addLayout(unitsLayout)

        label_discounts = QLabel('<font size="4">Discounts:</font>')
        self.button_discounts = QPushButton('Add Discount')
        self.button_discounts.clicked.connect(self.addDiscount)
        discountsButtonLayout.addWidget(label_discounts, 0, 0)
        discountsButtonLayout.addWidget(self.button_discounts, 0, 1)

        scroll_discounts = QScrollArea()
        scroll_discounts.setFixedHeight(400)
        scroll_discounts.setFixedWidth(400)
        scroll_discounts.setWidgetResizable(True)
        scroll_discounts_widget = QWidget()
        scroll_discounts_widget.setLayout(self.discountsFormLayout)
        self.discountsFormLayout.addStretch()
        self.discountsFormLayout.setDirection(QVBoxLayout.TopToBottom)
        scroll_discounts.setWidget(scroll_discounts_widget)


        discountsLayout.addLayout(discountsButtonLayout)
        discountsLayout.addWidget(scroll_discounts)

        formsLayout.addLayout(discountsLayout)

        label_notes = QLabel('<font size="4">Notes:</font>')
        self.button_notes = QPushButton('Add Note')
        self.button_notes.clicked.connect(self.addNote)
        notesButtonLayout.addWidget(label_notes, 0, 0)
        notesButtonLayout.addWidget(self.button_notes, 0, 1)

        scroll_notes = QScrollArea()
        scroll_notes.setWidgetResizable(True)
        scroll_notes.setFixedHeight(400)
        scroll_notes.setFixedWidth(300)
        scroll_notes_widget = QWidget()
        scroll_notes_widget.setLayout(self.notesFormLayout)
        self.notesFormLayout.addStretch()
        self.notesFormLayout.setDirection(QVBoxLayout.TopToBottom)
        scroll_notes.setWidget(scroll_notes_widget)

        notesLayout.addLayout(notesButtonLayout)
        notesLayout.addWidget(scroll_notes)

        formsLayout.addLayout(notesLayout)

        label_difficulty = QLabel('<font size="4">Difficulty:</font>')
        self.lineEdit_difficulty = QLineEdit()
        self.lineEdit_difficulty.setPlaceholderText('A B C D')
        extraLayout.addWidget(label_difficulty, 0, 0)
        extraLayout.addWidget(self.lineEdit_difficulty, 0, 1)

        label_kumo = QLabel('<font size="4">Kumo Cloud(s):</font>')
        self.spinBox_kumo = QSpinBox()
        self.spinBox_kumo.setMinimum(0)
        self.spinBox_kumo.setValue(0)
        extraLayout.addWidget(label_kumo, 1, 0)
        extraLayout.addWidget(self.spinBox_kumo, 1, 1)

        label_author = QLabel('<font size="4">Author:</font>')
        self.comboBox_author = QComboBox()
        self.comboBox_author.addItems(['Scott Arnold', 'Rob Penney', 'John Baccello', 'Jon Block'])
        self.comboBox_author.setEditable(True)
        self.comboBox_author.setCurrentText("Select Author")
        extraLayout.addWidget(label_author, 2, 0)
        extraLayout.addWidget(self.comboBox_author, 2, 1)

        label_electric = QLabel('<font size="4">Electric:</font>')
        self.comboBox_electric = QComboBox()
        self.comboBox_electric.addItems(['Rycor HVAC', 'Jaffer Electric', 'Craft Electric', 'TZ Electric'])
        #self.comboBox_author.setEditable(True)
        #self.comboBox_author.setCurrentText("Author")
        extraLayout.addWidget(label_electric, 3, 0)
        extraLayout.addWidget(self.comboBox_electric, 3, 1)

        label_solution = QLabel('<font size="4">Heat Solution:</font>')
        self.buttonGroup_solution = QButtonGroup()

        solutionLayout = QHBoxLayout()

        radio_partial = QRadioButton('Partial')
        self.buttonGroup_solution.addButton(radio_partial, 1)
        solutionLayout.addWidget(radio_partial)

        self.radio_full = QRadioButton('Full')
        self.radio_full.setChecked(True)
        self.buttonGroup_solution.addButton(self.radio_full, 2)
        solutionLayout.addWidget(self.radio_full)

        extraLayout.addWidget(label_solution, 4, 0)
        extraLayout.addLayout(solutionLayout, 4, 1)

        formsLayout.addLayout(extraLayout)
        
        button_clear = QPushButton('Clear')
        button_clear.clicked.connect(self.clearFields)
        buttonLayout.addWidget(button_clear, 1)
        #buttonLayout.setRowMinimumHeight(8, 25)

        button_propose = QPushButton('Propose')
        button_propose.clicked.connect(self.createProposal)
        buttonLayout.addWidget(button_propose, 2)
        #buttonLayout.setRowMinimumHeight(8, 25)

        layout.addLayout(formsLayout)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)

    def createProposal(self):
        d = {}
        d['name'] = self.lineEdit_name.text()
        d['street'] = self.lineEdit_street.text()
        d['town'] = self.lineEdit_town.text()
        d['zipcode'] = self.lineEdit_zipcode.text()
        d['phone'] = self.lineEdit_phone.text()
        d['email'] = self.lineEdit_email.text()

        d['units'] = {}
        for unit in self.getWidgets(self.unitsFormLayout):
            if type(unit) == Unit.Unit:
                location = unit.lineEdit_location.text()
                value = unit.comboBox_value.currentText()
                d['units'][location] = str(value)
        
        d['discounts'] = []
        for discount in self.getWidgets(self.discountsFormLayout):
            if type(discount) is Discount.Discount:
                d['discounts'].append(
                    {
                        'amount' : str(discount.lineEdit_amount.text()),
                        'reason' : discount.lineEdit_reason.text(),
                        'perUnit' : discount.checkBox_perUnit.isChecked()
                    }
                )

        d['notes'] = []
        for note in self.getWidgets(self.notesFormLayout):
            if type(note) is Note.Note:
                d['notes'].append(note.lineEdit_note.text())

        d['difficulty'] = self.lineEdit_difficulty.text()
        d['kumoCloud'] = int(self.spinBox_kumo.text())
        d['author'] = self.comboBox_author.currentText()
        d['electric'] = self.comboBox_electric.currentText()
        d['fullSolution'] = self.radio_full.isChecked()

        Proposal.createProposal(d)

        msg = QMessageBox()
        msg.setText(f'Enjoy your proposal,  {d["author"]}!')
        msg.exec_()

    def clearFields(self):
        self.lineEdit_name.clear()
        self.lineEdit_street.clear()
        self.lineEdit_town.clear()
        self.lineEdit_zipcode.clear()
        self.lineEdit_phone.clear()
        self.lineEdit_email.clear()
        self.lineEdit_difficulty.clear()
        #self.comboBox_author.setCurrentIndex(0)

        self.clearLayout(self.unitsFormLayout)
        self.unitsFormLayout.addStretch()

        self.clearLayout(self.discountsFormLayout)
        self.discountsFormLayout.addStretch()

        self.clearLayout(self.notesFormLayout)
        self.notesFormLayout.addStretch()


    def addUnit(self):
        numOfUnits = len(self.getWidgets(self.unitsFormLayout))-1
        self.unitsFormLayout.insertWidget(numOfUnits, Unit.Unit() )

    def addDiscount(self):
        numOfDiscounts = len(self.getWidgets(self.discountsFormLayout))-1
        self.discountsFormLayout.insertWidget(numOfDiscounts, Discount.Discount() )

    def addNote(self):
        numOfNotes = len(self.getWidgets(self.notesFormLayout))-1
        self.notesFormLayout.insertWidget(numOfNotes, Note.Note() )

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

    form = Main()
    form.show()

    sys.exit(app.exec_())
