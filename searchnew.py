import bibtexparser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        options = QFileDialog.Options()
        bibtexFile, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                    "BibTeX Files (*.bib)", options=options)
        db = bibtexparser.load(bibtexFile)
        self.currentlist = db.entries

        self.setWindowTitle("Search")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.boxlabel = QLabel("Entry Type:")

        layout = QFormLayout()
        self.typeinput = QComboBox()
        self.typeinput.addItem("-Please select type for Search")
        self.typeinput.addItem("Author")
        self.typeinput.addItem("Title")
        self.typeinput.addItem("Type")
        self.typeinput.addItem("Year")
        self.typeinput.activated[str].connect(self.selected)

        layout.addWidget(self.boxlabel)
        layout.addWidget(self.typeinput)
        self.setLayout(layout)

    def selected(self, data):
        if data == "Author":
            dlc = SAuthor()
            dlc.exec_()
        if data == "Title":
            dlc = STitle()
            dlc.exec_()
        if data == "Type":
            dlc = SType()
            dlc.exec_()
        if data == "Year":
            dlc = SYear()
            dlc.exec_()


class SAuthor(QDialog):
    def __init__(self, *args, **kwargs):
        super(SAuthor, self).__init__(*args, **kwargs)

        self.setWindowTitle("Author")
        self.setFixedWidth(400)
        self.setFixedHeight(100)

        self.searchButton = QPushButton("Search")

        self.line1 = QLineEdit()
        self.text1 = QLabel("Author:")
        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.searchButton)
        self.searchButton.clicked.connect(self.btn_clk)
        self.setLayout(layout)

    def btn_clk(self):
        author = self.line1.text()
        searchedlist = list()
        for k in self.currentlist:
            if k["author"] == author:
                searchedlist.append(k)
        print(currentlist)



class SType(QDialog):
    def __init__(self, *args, **kwargs):
        super(SType, self).__init__(*args, **kwargs)

        self.setWindowTitle("Type")
        self.setFixedWidth(400)
        self.setFixedHeight(100)

        self.searchButton = QPushButton("Search")

        self.line1 = QLineEdit()
        self.text1 = QLabel("Type:")
        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.searchButton)
        self.searchButton.clicked.connect(self.btn_clk)
        self.setLayout(layout)

    def btn_clk(self):
        type1 = self.line1.text()
        searchedlist = list()
        for k in self.currentlist:
            if k["type1"] == type1:
                searchedlist.append(k)
        print(searchedlist)


class STitle(QDialog):
    def __init__(self, *args, **kwargs):
        super(STitle, self).__init__(*args, **kwargs)

        self.setWindowTitle("Title")
        self.setFixedWidth(400)
        self.setFixedHeight(100)

        self.searchButton = QPushButton("Search")

        self.line1 = QLineEdit()
        self.text1 = QLabel("Title:")
        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.searchButton)
        self.searchButton.clicked.connect(self.btn_clk)
        self.setLayout(layout)

    def btn_clk(self):
        title = self.line1.text()
        searchedlist = list()
        for k in self.currentlist:
            if k["title"] == title:
                searchedlist.append(k)
        print(searchedlist)


class SYear(QDialog):
    def __init__(self, *args, **kwargs):
        super(SYear, self).__init__(*args, **kwargs)

        self.setWindowTitle("Year")
        self.setFixedWidth(400)
        self.setFixedHeight(100)

        self.searchButton = QPushButton("Search")

        self.line1 = QLineEdit()
        self.text1 = QLabel("Year:")
        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.line1)
        layout.addWidget(self.searchButton)
        self.searchButton.clicked.connect(self.btn_clk)
        self.setLayout(layout)

    def btn_clk(self):
        year = self.line1.text()
        searchedlist = list()
        for k in self.currentlist:
            if k["year"] == year:
                searchedlist.append(k)
        print(searchedlist)