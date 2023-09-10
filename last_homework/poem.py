class Poem:
    def __init__(self, name, author, dynasty, form, peom):
        self.name = name
        self.author = author
        self.dynasty = dynasty
        self.form = form
        self.poem = peom

    def __str__(self):
        print(self.name, self.author, self.dynasty, self.kind, self.poem)


class Poet:
    def __init__(self, name, dynasty, synopsis):
        self.name = name
        self.dynasty = dynasty
        self.synopsis = synopsis

    def __str__(self):
        print(self.name, self.synopsis)


class Book:
    def __init__(self, name, dynasty, synopsis):
        self.name = name
        self.dynasty = dynasty
        self.synopsis = synopsis

    def __str__(self):
        print(self.name, self.synopsis)
