class librarydb():

    def __init__(self,books_list,library_name):
        self.bookslist=books_list
        self.libraryname=library_name
        self.lend=[]

    def displaybook(self,savelist):
        for i in range(len(savelist)):
            print(i,savelist[i])

    def lendbook(self,bookkeeper,nameofbook):
        if self.bookslist[nameofbook] in self.bookslist:
            self.lend.append(self.bookslist[nameofbook])
            self.bookslist.pop(nameofbook)
            print('Book lended')
        else:
            print('Book is not Available in our library\n'
                  f'{bookkeeper} you can lend from above displayed books')

    def addbook(self,bookadd):
        if bookadd in self.bookslist:
            print('Book already exist in library')
        else:
            self.bookslist.append(bookadd)
            print('Book Added')

    def returnbook(self,nameofbook,bookkeeper):
        if self.lend[nameofbook] in self.lend:
            self.bookslist.append(self.lend[nameofbook])
            self.lend.pop(nameofbook)
            print('Book returned')
        else:
            print(f"{bookkeeper} this book doesn't belongs from our library")

    def removebook(self,bookremove):
            self.bookslist.pop(bookremove)
            print('Book Removed')

run = True
while(run):
    designation=input("ADMIN/STUDENT?: ").upper()
    if designation=='ADMIN':
        print('LOGIN DETAILS')
        user=input('Username: ')
        password=input('Password: ')
        if user=='admin' and password=='12345':
            books=list(input('Enter list of books: ').split(','))
            name=input('Name of library: ')
            print(f"Welcome to {name} Virtual Library Database\n")
            yash=librarydb(books,name)
            while (run):
                if __name__ == "__main__":
                    print('<<<<<<<<<<<<<<>>>>>>>>>>>>>>>')
                    print('Choose the option:\n'
                          'display / add / remove / quit')
                    opt = str(input('option: '))
                    if opt == 'display':
                        yash.displaybook(books)
                    elif opt == 'quit':
                        print(f'Exit from {name} Virtual Library')
                        run = False
                    elif opt == 'add':
                        addbookname = input('Add book name: ')
                        yash.addbook(addbookname)
                        yash.displaybook(books)
                    elif opt == 'remove':
                        yash.displaybook(books)
                        removebookname = int(input('Remove book no.: '))
                        yash.removebook(removebookname)
                    else:
                        print("Invalid Input")
        else:
            print('Unauthorized user')
    elif designation=='STUDENT':
        studentbook = ['Song of ice and fire','Ramayana','Mahabharat','Vikram Chandra,']
        studentname = input("Enter your name: ")
        yash = librarydb(studentbook, studentname)
        while (run):
            if __name__ == "__main__":
                print('<<<<<<<<<<<<<<>>>>>>>>>>>>>>>')
                print('Choose the option:\n'
                      'display / lend / return / quit')
                opt = str(input('option: '))
                if opt == 'display':
                    yash.displaybook(studentbook)
                elif opt == 'quit':
                    print('Exit from Virtual Library')
                    run = False
                elif opt == 'lend':
                    lender = studentname
                    yash.displaybook(studentbook)
                    book = int(input('Which book you want?: '))
                    yash.lendbook(lender, book)
                elif opt == 'return':
                    returner = studentname
                    yash.displaybook(yash.lend)
                    book = int(input('Which book do you want to return?:'))
                    yash.returnbook(book, returner)
                else:
                    print("Invalid Input")
    else:
        print("Type ADMIN or STUDENT")
