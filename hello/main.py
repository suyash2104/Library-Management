import user
import hello
import rfid_data

print("*" * 68)
print("-" * 68)
print("\n" + " " * 25 + "Welcome to Library" + "\n" + " " * 25)
print("-" * 68)
print("*" * 68)


while True:
    op = int(input("\nChoose the operation:\n1.Issue book\n2.Return book\n3.Get book list\n4.Get book info: "))

    if op == 1:
        print("\nScan the user id: ")
        uid =  rfid_data.rfid_data()
        new_data = user.user_info(uid)
        if new_data == 0:
            print("User not found ")
            continue
        else:
            print("Name: {0.name}\tId: {0.id}\tBooks: {0.books}".format(new_data))

        while True:
            print("Scan book id: ")
            bid = rfid_data.rfid_data()
            book = hello.get_book(bid)
            if book == 0:
                print("Book not found ")
            else:
                print("Book: {0.name}\tAuthor: {0.author}\tId: {0.id}\tIssue status: {0.issue}".format(book))
            user.add_book(bid, uid)
            hello.iss_ret("True", bid)
            c = input("Want to add more book(y/Y)? ")
            if not (c == 'y' or c == "Y"):
                break
    if op == 2:
        print("\nScan the user id: ")
        uid =  rfid_data.rfid_data()
        new_data = user.user_info(uid)
        if new_data == 0:
            print("User not found ")
            continue
        else:
            print("Name: {0.name}\tId: {0.id}\tBooks: {0.books}".format(new_data))
            while True:
                print("Scan book id: ")
                bid = rfid_data.rfid_data()
                book = hello.get_book(bid)
                if book == 0:
                    print("Book not found ")
                else:
                    print("Book: {0.name}\tAuthor: {0.author}\tId{0.id}\tIssue status: {0.issue}".format(book))
                user.remove(bid, uid)
                hello.iss_ret("False", bid)
                c = input("Want to add more book(y/Y)? ")
                if not (c == 'y' or c == "Y"):
                    break


    elif op == 3:
        hello.get_list()
    elif op == 4:
        hello.main_get_book()

    choice = input("Do you want to continue(y/Y): ")
    if not (choice == 'y' or choice == 'Y'):
        break