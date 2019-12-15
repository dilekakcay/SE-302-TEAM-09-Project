from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QtWidgets.QWidget):
    def __init__(self, rows, columns):
        QtWidgets.QWidget.__init__(self)
        self.table = QtGui.QTableWidget(self)
        self.table.setRowCount(rows)
        self.table.setColumnCount(columns)
        for column in range(columns):
            for row in range(rows):
                item = QtGui.QTableWidgetItem('Text%d' % row)
                self.table.setItem(row, column, item)
        self.edit = QtGui.QLineEdit(self)
        self.button = QtGui.QPushButton('Search', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.table)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

    def handleButton(self):
        items = self.table.findItems(
            self.edit.text(), QtCore.Qt.MatchExactly)
        if items:
            results = '\n'.join(
                'row %d column %d' % (item.row() + 1, item.column() + 1)
                for item in items)
        else:
            results = 'Found Nothing'
        QtGui.QMessageBox.information(self, 'Search Results', results)