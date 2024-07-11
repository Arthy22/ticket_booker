import mysql.connector as mycon
from report import PdfReport

object = mycon.connect(host="localhost", user="root", password="{Arthy1234}", database="cinema",
                       auth_plugin="mysql_native_password")

if object.is_connected:
    print("Hi welcome to database cinema")
cursor = object.cursor()
object.commit()

cursor.execute("use cinema")


class User:
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        global balance
        cursor.execute("select balance from booking where number=" + str(card.number))
        for i in cursor:
            balance = i[0]
        if seat.is_free():
            if card.validate():
                if balance > seat.price:
                    seat.occupy()

                    cursor.execute(
                        "update booking set balance=" + str(balance - seat.price) + " where number=" + str(
                            card.number))
                    print("Purchase succesfull")
                    ticket = Ticket(self.name, seat.price, seat.seat_id)
                    ticket.to_pdf()
            else:
                print("Card details not valid")
        else:
            print("Seat is already occupied")


class Seat:
    def __init__(self, seat_id):
        self.seat_id = seat_id
        cursor.execute("select price from cinema where seat_id='" + str(self.seat_id) + "'")
        for i in cursor:
            self.price = i[0]

    def is_free(self):
        global taken
        cursor.execute("select taken from cinema where seat_id='" + str(self.seat_id) + "'")
        for i in cursor:
            taken = i[0]
        if taken == 0:
            return True
        else:
            return False

    def occupy(self):
        cursor.execute("update cinema set taken=1 where seat_id='" + str(self.seat_id) + "'")


class Card:
    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self):
        cursor.execute("select type,number,cvc,holder from booking where number=" + str(self.number))
        for i in cursor:
            if i[0] == self.type and i[1] == self.number and i[2] == self.cvc and i[3] == self.holder:
                return True
            else:
                return False


class Ticket:
    def __init__(self, user, price, seat):
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self):
        pdf = PdfReport(filename="Ticket.pdf")
        pdf.generate(self.user, self.price, self.seat)


user1 = User(name="John")
seat1 = Seat("A1")
card1 = Card("Visa", 12345678, 123, "John Smith")
user1.buy(seat1, card1)

"""
cursor.execute("select * from booking")
for i in cursor:
    print(i)

print("****************************")
cursor.execute("select * from cinema")
for i in cursor:
    print(i)
"""
