class Item(object):
    def __init__(self, name, year, type, ID):
        self.name = name
        self.year = year
        self.type = type
        self.ID = ID

    def get_year(self):
        return self.year

    def get_type(self):
        return self.type

    def get_ID(self):
        return self.ID


class Journal(Item):
    def __init__(self,
                 name,
                 year,
                 type,
                 ID):
        super().__init__(name, year, type, ID)


class Book(Item):
    def __init__(self,
                 name,
                 year,
                 type,
                 ID):
        super().__init__(name, year, type, ID)


class Conferance(Item):
    def __init__(self,
                 name,
                 year,
                 type,
                 ID):
        super().__init__(name, year, type, ID)



class Article(Item):
    def __init__(self,
                 name,
                 year,
                 type,
                 ID):
        super().__init__(name, year, type, ID)



class Miscellaneous(Item):
    def __init__(self,
                 name,
                 year,
                 type,
                 ID):
        super().__init__(name, year, type, ID)



