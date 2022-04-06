import sys
from PyQt5.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout, QScrollArea, QWidget, QPushButton, QRadioButton, QLabel, QLineEdit, QGridLayout, QMessageBox)

class Main(QWidget):
	def __init__(self, Parent = None):
		win_w = 500
		win_h = 500
		super(Main, self).__init__()
		self.setWindowTitle('Proposal Creator')
		self.setGeometry((1920 - win_w) // 2, (1080 - win_h) // 2, win_w, win_h)
		self.resize(300, 500)
	
	def GUI(self):

		layout = QHBoxLayout()
		homeownerLayout = QFormLayout()


		label_name = QLabel('<font size="4"> Name </font>')
		self.lineEdit_name = QLineEdit()
		self.lineEdit_name.setPlaceholderText('Homeowner Name')
		homeownerLayout.addRow(label_name, self.lineEdit_name)

		label_street = QLabel('<font size="4"> Street </font>')
		self.lineEdit_street = QLineEdit()
		self.lineEdit_street.setPlaceholderText('Homeowner Street Address')
		layout.addWidget(label_street, 1, 0)
		layout.addWidget(self.lineEdit_street, 1, 1)

		label_town = QLabel('<font size="4"> Town </font>')
		self.lineEdit_town = QLineEdit()
		self.lineEdit_town.setPlaceholderText('Homeowner Town')
		layout.addWidget(label_town, 2, 0)
		layout.addWidget(self.lineEdit_town, 2, 1)

		label_zipcode = QLabel('<font size="4"> Zipcode </font>')
		self.lineEdit_zipcode = QLineEdit()
		self.lineEdit_zipcode.setPlaceholderText('Homeowner Zipcode')
		layout.addWidget(label_zipcode, 3, 0)
		layout.addWidget(self.lineEdit_zipcode, 3, 1)

		label_phone = QLabel('<font size="4"> Phone </font>')
		self.lineEdit_phone = QLineEdit()
		self.lineEdit_phone.setPlaceholderText('Homeowner Phone Number')
		layout.addWidget(label_phone, 4, 0)
		layout.addWidget(self.lineEdit_phone, 4, 1)

		label_email = QLabel('<font size="4"> Email </font>')
		self.lineEdit_email = QLineEdit()
		self.lineEdit_email.setPlaceholderText('Homeowner Email Address')
		layout.addWidget(label_email, 5, 0)
		layout.addWidget(self.lineEdit_email, 5, 1)

		label_units = QLabel('<font size="4"> Units </font>')
		self.button_units = QPushButton('Add Unit')
		self.button_units.clicked.connect(self.addUnit)
		layout.addWidget(label_units, 6, 0)
		layout.addWidget(self.button_units, 6, 1)




		label_author = QLabel('<font size="4"> Author </font>')
		self.comboBox_author = QComboBox()
		self.comboBox_author.addItems(['Scott Arnold', 'Rob Penney', 'John Baccello', 'Jon Block'])
		self.comboBox_author.setEditable(True)
		self.comboBox_author.setCurrentText("Select Author")
		layout.addWidget(label_author, 7, 0)
		layout.addWidget(self.comboBox_author, 7, 1)
		

		button_clear = QPushButton('Clear')
		button_clear.clicked.connect(self.clearFields)
		layout.addWidget(button_clear, 8, 0)
		layout.setRowMinimumHeight(8, 25)

		button_login = QPushButton('Propose')
		button_login.clicked.connect(self.createProposal)
		layout.addWidget(button_login, 8, 1)
		layout.setRowMinimumHeight(8, 25)

		self.setLayout(layout)
    
	def createProposal(self):
		print(self.comboBox_author.currentText())
		msg = QMessageBox()
		msg.setText('Enjoy your proposal!')
		msg.exec_()

	def clearFields(self):
		self.lineEdit_name.setPlaceholderText('Homeowner Name')
		msg = QMessageBox()
		msg.setText('Cleared!')
		msg.exec_()

	def addUnit(self):
		label = QLabel()
		label_units = QLabel('<font size="4"> Units </font>')      
		self.scrollArea.addWidget(label_units)


if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = ProposalCreator()
	form.show()

	sys.exit(app.exec_())