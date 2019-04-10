import user

in_id = input("Enter the id ")
new_data = user.user_info(in_id)
if new_data == 0:
    print("user not found ")
else:
    print("{0.name}\t{0.id}\t{0.books}".format(new_data))