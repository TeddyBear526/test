class writer:
    def __init__(self):
        self.name = ""
        self.lastname = ""

class book:
    def __init__(self):
        self.title = ""
        self.owner = None

writer1 = writer()
writer1.name = "jasper"
writer1.lastname = "Jamesson"

book1 = book()
book1.title = "The Bible"
book1.owner = writer1

print(book1.title)
print(book1.owner.name, book1.owner.lastname)
