class Library:
    def __init__(self, listofbooks, library_name, donation):
        self.listofbooks = listofbooks
        self.library_name = library_name
        self.donation = donation


    def display_book(self):
        ''' This function will display all the books '''
        for x in range(len(self.listofbooks)):
            print(f"{x+1}> {self.listofbooks[x]}")

        return ""

    def delete_books(self,book_name):
        '''This function will delete the book'''
        self.listofbooks.remove(book_name)
        
    def add_book(self, book_name):
        '''This function will add book'''
        self.listofbooks.append(book_name)

    def see_donation(self):
        '''This function will print the total donation'''
        print(self.donation)

    def give_donation(self, amount_get):
        '''This function will add the amount in the donation'''
        self.donation = self.donation + amount_get



def main():
    key = 123456789
    List_of_books = ["Learn Python", "Learn Java", "Bhagwat Gita"]
    Rishaw = Library(List_of_books, "Rishaw", 10)

    print(f"Welcome to the Rishaw's library. Type 'r' for delete , 'd' for display, 'a' for add, 'g' for give donation, 's' for see donation,'quit' for exit")

    get = False
    while (get != True):
        take = input("Select : ")
        if take == "d":
            Rishaw.display_book()

        elif take == "r":
            try:
                take_key = int(input("Enter the secret key to delete the book : "))
                if take_key == key:
                    Book__Name = input("Enter the name of the book : ")
                    Rishaw.delete_books(Book__Name)

                else:
                    print("Wrong key word , We can't delete the book")


            except ValueError:
                print("Invalid value")


        elif take == "quit":
            get = True
            
        elif take == "a":
            book_title = input("Enter the book name : ")
            Rishaw.add_book(book_title)

        elif take == "s":
            Rishaw.see_donation()

        elif take == "g":
            amount = int(input("Enter the amount of donation : "))
            Rishaw.give_donation(amount)

        else:
            print("LOL")


if __name__ == "__main__":
    main()