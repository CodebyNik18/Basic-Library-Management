class Library:
    no_of_books = 0
    book = []
    len_of_books = 0
    def add_books(self):
        add = int(input("How many books you want to add ? = "))
        for i in range(add):
            adding_books = input("Enter the name of book = ")
            if adding_books.strip().lower() in (i.lower() for i in Library.book):
                print("Repetition is not allowed...")
            else:
                Library.book.append(adding_books)
                Library.no_of_books += 1
                Library.len_of_books += 1
        # print(Library.no_of_books)

    def rent_books(self):
        if Library.book == []:
            print("There is no book to rent...")
        else:
            print("Select the Book you want to rent...")
            for i in range(1, len(Library.book) + 1):
                print(f"{i}. {Library.book[i-1].title()}")
            option = input("Enter the Book name to rent: ").strip().lower()
            if option not in (i.lower() for i in Library.book):
                print("Book is not in the Library...")
            else:
                # print(Library.len_of_books)
                print("Thanks for renting the Book...'{}'".format(option))
                Library.len_of_books -= 1
                Library.book.remove(option)
            # print(Library.len_of_books)

    def check(self):
        if Library.no_of_books == 0:
            print("Book collection is Empty....")
        elif Library.no_of_books == Library.len_of_books:
            print("All Books are present in the library..")
        else:
            print(f"{Library.no_of_books - Library.len_of_books} Books are missing from the library..")
            
person1 = Library()


# print(person1.book)
# person1.add_books()
# person1.rent_books()
# person1.check()


while True:
    print("Press '1' to Add Books..")
    print("Press '2' to Rent Books..")
    print("Press '3' to Check all Books are present or not..")
    print("Press '4' to Exit..\n")
    ch = int(input("Select your option: "))
    if ch == 1:
        print("Only admin can access this...Write password to access below..")
        passw = input("Enter the admin Password to access: ")
        if passw == "admin":
            person1.add_books()
        else:
            print("Password is wrong...\n")
    elif ch == 2:
        person1.rent_books()
    elif ch == 3:
        person1.check()
    elif ch == 4:
        print("Thank you...for visiting")
        break
    else:
        print("Invalid option...")