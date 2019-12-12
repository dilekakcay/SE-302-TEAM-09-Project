import re
from typing import List


class Item:
    def __init__(self, type, typeTitle, author, title, year, volume, journal, page1, page2, key):
        self.type = type
        self.typeTitle = typeTitle
        self.author = author
        self.title = title
        self.year = year
        self.volume = volume
        self.journal = journal
        self.page1 = page1
        self.page2 = page2
        self.key = key


class Create:
    def __init__(self, type, typeTitle, author, title, year, volume, journal, page1, page2, key):
        self.type = type
        self.typeTitle = typeTitle
        self.author = author
        self.title = title
        self.year = year
        self.volume = volume
        self.journal = journal
        self.page1 = page1
        self.page2 = page2
        self.key = key
        self.obj_item = Item(self.type, self.typeTitle, self.author, self.title, self.year, self.volume, self.journal,
                             self.page1, self.page2, self.key)

    def create(self):
        bibtex = "\n@%s{%s,\n " \
                 "author = {%s},\n " \
                 "title = {%s},\n " \
                 "year = {%d},\n " \
                 "volume = {%d},\n " \
                 "pages = {%d--%d},\n " \
                 "journal = {%s},\n " \
                 "keywords = {%s}}\n" \
                 % (str(self.obj_item.type), str(self.obj_item.typeTitle), str(self.obj_item.author),
                    str(self.obj_item.title), self.obj_item.year, self.obj_item.volume, self.obj_item.page1,
                    self.obj_item.page2, str(self.obj_item.journal), str(self.obj_item.key))
        f = open("bibtex.bib", "r+")
        f.read()
        f.write(bibtex)
        f.close()

    def read(self):
        f = open("bibtex.bib", "r")
        new = f.read()
        entries = new.split('@')[1:]
        print(entries)

type = str(input("Enter bib's type:"))
typeTitle = str(input("Enter bib's type's title:"))
volume = int(input("Enter volume:"))
journal = str(input("Enter journal:"))
author = str(input("Enter author(s):"))
step1 = author.split("and")
#düzenlenicek
res = []
for s in step1:
    sub = s.split(' ')
    res.append(sub)
#
title = str(input("Enter title:"))
year = int(input("Enter year:"))
page1 = int(input("Enter initial page:"))
page2 = int(input("Enter final page:"))
key = str(input("Enter a key value:"))
c = Create(type, typeTitle, res, title, year, volume, journal, page1, page2, key)
c.create()
c.read()
