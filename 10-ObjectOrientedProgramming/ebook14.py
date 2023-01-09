class ebook():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False
    def open(self):
        if self.is_open == False:
            self.is_open = True
    def close(self):
        if self.is_open == True:
            self.is_open = False
    def read(self, pages):
        if self.is_open == True:
            self.current_page += pages
        else:
            print("Not possible. Book is closed")
    def status(self):
        print(f"title = {self.title}, author = {self.author}, number of pages = {self.pages}, current page = {self.current_page}")