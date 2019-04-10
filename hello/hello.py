
import os
class Books(object):

    def __init__(self, name, author, id, iss='False'):
        self.name = name
        self.author = author
        self.id = id
        self.issue = iss

    def issued(self):
        self.issue = 'True'
        print("Book is not in library")

    def returned(self):
        self.issue = 'False'
        print("Book is in library")


def get_data():
    name = input("Enter the book name: ")
    author = input("Enter the author: ")
    id = input("Enter the ID: ")
    return Books(name, author, id)


def write_data():
    new_book = get_data()
    with open("books.txt", 'a') as books:
        print("{0.name}\t{0.author}\t{0.id}\t{0.issue}".format(new_book), file=books)


def get_list():
    if os.path.getsize("books.txt") > 0:
        with open("books.txt", "r") as books:
            for line in books:
                name, author, id, iss = tuple(line.strip('\n').split('\t'))
                book = Books(name, author, id, iss)
                print("Book: {0.name}\tAuthor: {0.author}\tId: {0.id}\tIssue status: {0.issue}".format(book) +"\n"+ "-" *100)

    else:
        print("List is empty")


def get_book(in_id):
    with open("books.txt", "r") as books:
        for line in books:
            name, author, i, iss = tuple(line.strip('\n').split('\t'))
            if in_id == i:
                return Books(name, author, i, iss)
        else:
            return 0

def main_get_book():
    in_id = input("Enter the id ")
    new_data = get_book(in_id)
    if new_data == 0:
        print("Book not found ")
    else:
        print("Book: {0.name}\tAuthor: {0.author}\tId{0.id}\tIssue status: {0.issue}".format(new_data))



def modify_data():
    if os.path.getsize("books.txt") > 0:
        in_id = input("Enter the id of book you want to change: ")
        with open("books.txt","r") as book1:
            with open("new.txt","w") as book2:
                for line in book1:
                    name, author, id, iss = tuple(line.strip('\n').split('\t'))
                    if in_id == id:
                        new_data = get_data()
                        print("{0.name}\t{0.author}\t{0.id}\t{0.issue}".format(new_data), file=book2)
                    else:
                        print("{0}\t{1}\t{2}\t{3}".format(name,author,id,iss), file=book2)
        os.remove("books.txt")
        os.rename("new.txt", "books.txt")
    else:
        print("File is empty")

def delete_data():
    if os.path.getsize("books.txt") > 0:
        in_id = input("Enter the id of book you want to delete: ")
        with open("books.txt","r") as book1:
            with open("new.txt","w") as book2:
                for line in book1:
                    name, author, id, iss = tuple(line.strip('\n').split('\t'))
                    if in_id == id:
                        continue
                    else:
                        print("{0}\t{1}\t{2}\t{3}".format(name,author,id, iss), file=book2)
        os.remove("books.txt")
        os.rename("new.txt", "books.txt")
    else:
        print("File is empty")


# Try to reduce this code by using modify function.
# Same function for returning also.
def iss_ret(operation, in_id):
    book = get_book(in_id)
    if book == 0:
        if __name__ == "__main__":
            print("Book not found")
    else:
        if book.issue == operation:
            if operation == "True":
                print("Book is not in library!!!")
            else:
                print("Book is already in library")

        else:
            book.issue = operation
            if operation == "True":
                print("Book is issued")
            else:
                print("Book is returned")
            if os.path.getsize("books.txt") > 0:
                with open("books.txt","r") as book1:
                    with open("new.txt","w") as book2:
                        for line in book1:
                            name, author, id, iss = tuple(line.strip('\n').split('\t'))
                            if in_id == id:
                                print("{0.name}\t{0.author}\t{0.id}\t{0.issue}".format(book), file=book2)
                            else:
                                print("{0}\t{1}\t{2}\t{3}".format(name,author,id,iss), file=book2)
                os.remove("books.txt")
                os.rename("new.txt", "books.txt")
            else:
                print("File is empty")


if __name__ == "__main__":
    c = True
    while c:
        choice = int(input("\nEnter the choice\n1.Add book to Database: \n2.Get list\n"
                           "3.Get Book\n4.Modify data\n5.Delete Data\n6.Issue book\n7.Return book " ))
        if choice == 1:
            write_data()
        elif choice == 2:
            get_list()
        elif choice == 3:
            main_get_book()
        elif choice == 4:
            modify_data()
        elif choice == 5:
            delete_data()
        elif choice == 6:
            in_id = input("Enter the ID of book: ")
            iss_ret("True", in_id)
        elif choice == 7:
            in_id = input("Enter the ID of book: ")
            iss_ret("False", in_id)
        else:
            print("Wrong choice")
        c = input("Do you want to continue(y/Y) ")
        if not (c == 'y' or c == 'Y'):
            c = False
