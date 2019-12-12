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
type = type.replace('ö', 'o')
type = type.replace('ğ', 'g')
type = type.replace('ü', 'u')
type = type.replace('ç', 'c')
type = type.replace('ş', 's')
type = type.title()
typeTitle = str(input("Enter bib's type's title:"))
typeTitle = typeTitle.replace('ö', 'o')
typeTitle = typeTitle.replace('ğ', 'g')
typeTitle = typeTitle.replace('ü', 'u')
typeTitle = typeTitle.replace('ç', 'c')
typeTitle = typeTitle.replace('ş', 's')
typeTitle = typeTitle.title()
volume = int(input("Enter volume:"))
journal = str(input("Enter journal:"))
journal = journal.replace('ö', 'o')
journal = journal.replace('ğ', 'g')
journal = journal.replace('ü', 'u')
journal = journal.replace('ç', 'c')
journal = journal.replace('ş', 's')
journal = journal.title()
author = str(input("Enter author(s):"))
author = author.replace('ö', 'o')
author = author.replace('ç', 'c')
author = author.replace('ğ', 'g')
author = author.replace('ü', 'u')
author = author.replace('ş', 's')
author = author.title()
"""step1 = author.split("and")
res = []
for s in step1:
    sub = s.split(',')
    res.append(sub)
print(res)"""
title = str(input("Enter title:"))
title = title.replace('ö', 'o')
title = title.replace('ç', 'c')
title = title.replace('ğ', 'g')
title = title.replace('ü', 'u')
title = title.replace('ş', 's')
title = title.title()
year = int(input("Enter year:"))
page1 = int(input("Enter initial page:"))
page2 = int(input("Enter final page:"))
key = str(input("Enter a key value:"))
key = key.replace('ö', 'o')
key = key.replace('ç', 'c')
key = key.replace('ğ', 'g')
key = key.replace('ü', 'u')
key = key.replace('ş', 's')
key = key.title()
c = Create(type, typeTitle, author, title, year, volume, journal, page1, page2, key)
c.create()
c.read()
