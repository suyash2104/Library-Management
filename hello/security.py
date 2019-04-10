import hello
import sec_rfid

while True:
    alarm = "off"
    bid = sec_rfid.s_rfid()
    print(bid)
    book = hello.get_book(bid)
    if (not(book == 0) and book.issue == "True") or bid == "30200":
        print(alarm)
        sec_rfid.w_rf_data("0")
    else:
        alarm = "on"
        print(alarm)
        sec_rfid.w_rf_data("1")