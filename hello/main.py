import user
import hello

print("\nWealcome to Library\n")

choice = True
while choice:
    op = int(input("\nChoose the operation:\n1.Issue book\n2.Return book\n3.Get book list\n4.Get book info\n: "))
    if op == 1:
        uid = input("Scan your user rfid tag\n")
        while True:
            bid = input("Scan the book id\n")
            hello.iss_ret("True")
            user.add_book(bid)
            c = input("Do want to add more book(y/Y): ")
            if not (c == 'y' or c == 'Y'):
                break

    elif op == 3:
        hello.get_list()
    elif op == 4:
        hello.main_get_book()
