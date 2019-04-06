import os

class Reader(object):

    def __init__(self, name, i, books=""):
        self.name = name
        self.id = i
        self.books = books

    def check(self):
        l = self.books.split(" ")
        if len(l) > 6:
            return True

def get_user():
    name = input("Enter the name: ")
    id = input("Enter the ID: ")
    return Reader(name, id)


def write_data(new_data):
    with open("reader.txt","a") as reader:
        print("{0.name}\t{0.id}\t{0.books}".format(new_data), file=reader)

def add_user():
    new_data = get_user()
    write_data(new_data)

def get_u_list():
    if os.path.getsize("reader.txt") > 0:
        with open("reader.txt", "r") as reader:
            for line in reader:
                name, i, books = tuple(line.strip('\n').split('\t'))
                new_reader = Reader(name, i, books)
                print("{0.name}\t{0.id}\t{0.books}".format(new_reader), file=None)


def user_info(u_id):
    with open("reader.txt", "r") as reader:
        for line in reader:
            name, i, books = tuple(line.strip('\n').split('\t'))
            if i == u_id:
                return Reader(name, i, books)
        else:
            return 0

def add_book(bid):
    in_id = input("Enter the id of user: ")
    user = user_info(in_id)
    if user == 0:
        print("User not found")
    else:
        if user.check():
            print("Quota is full")
        else:
            user.books = user.books.split(" ")
            user.books.append(bid)
            user.books = " ".join(user.books)
            modify(user, user.id)

def remove(bid):
    in_id = input("Enter the id of user: ")
    user = user_info(in_id)
    if user == 0:
        print("User not found")
    else:
        user.books = user.books.split(" ")
        try:
            user.books.pop(user.books.index(bid))
        except:
            print("Book not found ")
        user.books = " ".join(user.books)
        modify(user, user.id)




def modify(new_data, i):
    if os.path.getsize("reader.txt") > 0:
        with open("reader.txt","r") as u1:
            with open("new.txt","w") as u2:
                for line in u1:
                    name, id, books = tuple(line.strip('\n').split('\t'))
                    if i == id:
                        print("{0.name}\t{0.id}\t{0.books}".format(new_data), file=u2)
                    else:
                        print("{0}\t{1}\t{2}".format(name, id, books), file=u2)
        os.remove("reader.txt")
        os.rename("new.txt", "reader.txt")
    else:
        print("File is empty")

def modify_user(i):
    user = get_user()
    modify(user, i)


def delete(i):
    if os.path.getsize("reader.txt") > 0:
        with open("reader.txt","r") as u1:
            with open("new.txt","w") as u2:
                for line in u1:
                    name, id, books = tuple(line.strip('\n').split('\t'))
                    if i == id:
                        continue
                    else:
                        print("{0}\t{1}\t{2}".format(name, id, books), file=u2)
        os.remove("reader.txt")
        os.rename("new.txt", "reader.txt")
    else:
        print("File is empty")




if __name__ == "__main__":
    c = True
    while c:
        choice = int(input("\nEnter the choice\n1.Add user to Database: \n2.Get list: \n"
                           "3.Get user\n4.Modify data\n5.Delete Data\n6.Add book to user\n"
                           "7.Remove book from user " ))
        if choice == 1:
            add_user()
        elif choice == 2:
            get_u_list()
        elif choice == 3:
            in_id = input("Enter the id ")
            new_data = user_info(in_id)
            if new_data == 0:
                print("user not found ")
            else:
                print("{0.name}\t{0.id}\t{0.books}".format(new_data))
        elif choice == 4:
            i = input("Enter the id: ")
            user = user_info(i)
            if user == 0:
                print("User not found")
            else:
                modify_user(i)
        elif choice == 5:
            i = input("Enter the id you want to delete: ")
            delete(i)
        elif choice == 6:
            bid = input("Enter the id of the book you want to enter ")
            add_book(bid)
        elif choice == 7:
            bid = input("Enter the id of the book you want to delete ")
            remove(bid)
        c = input("Do you want to continue(y/Y) ")
        if not (c == 'y' or c == 'Y'):
            c = False
