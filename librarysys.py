class Library(object):
    
    """
    Library Class that operates library management system
    
    Attributes
    ----------
    books  : store available books in a list
    
    
    Methods
    -------
    display_available_books
        Display the current available books.
        
    lend_books
        Takes the name of the book and removes it from the list of books in the library.
    
    add_books
        Add the book back to the library after it is returned. 
        
    """

    onloan = []
    def __init__(self, books: list):
        
        """ 
        Constructor that initiate Library class 
        Assuming the library only has three books for now: 
        The Last Battle, The Screwtape Letters and The Great Divorce.

        """
        
        self.books = books

    def display_available_books(self)->str:
        
        """
        a method to display the current available books
        
        """
        
        
        print("There are currently {} available books in the library.".format(len(self.books)))
        print("=----------------------------------------------------=")
        for idx, book in enumerate(self.books):
            print(idx+1, book)
            
            
    def levenshtein_ratio_and_distance(self, input1, input2, ratio_calc = False):
        """ 
            Calculates levenshtein distance between two strings.

        """
        
        self.input1 = input1
        self.input2 = input2
        
        # Initialise matrix of zeros by specified number of rows and columns
        rows = len(self.input1)+1
        cols = len(self.input2)+1
        dist = np.zeros((rows,cols),dtype = int)

        # Replace zeroes with the indeces of each character of the two inputs
        for i in range(1, rows):
            for j in range(1,cols):
                dist[i][0] = i
                dist[0][j] = j

        # Iterate over the matrix to compute the score
        # There are 3 possible operations: deletions,insertions and/or substitutions  
        # Each operation is assigned a score, else score is zero

        for col in range(1, cols):
            for row in range(1, rows):
                if input1[row-1] == input2[col-1]:
                    score = 0 #  if character matches exactly at i,j position score zero
                else:
                    # the score for substitution is 2
                    #If we calculate just distance, then the cost of a substitution is 1.
                    if ratio_calc == True:
                        score = 2
                    else:
                        score = 1
                dist[row][col] = min(dist[row-1][col] + 1,      # deletions
                                     dist[row][col-1] + 1,          # insertions
                                     dist[row-1][col-1] + score)     # substitutions
        if ratio_calc == True:
            # Calculate ratio
            Ratio = ((len(self.input1)+len(self.input2)) - dist[row][col]) / (len(self.input1)+len(self.input2))
            return round(Ratio,2)
    
    
    def lend_books(self, book=None):
        
        
        """ 
        a method for lending a book. 
        This method takes the name of the book and removes it from the list of books in the library.
        
        """
        self.book = book
        
        
        if self.book in self.books:
            self.books.remove(self.book)
            self.onloan.append(self.book)
            print("You have selected")
            print("=---------------------------=")
            print("=--", self.book.title(),"=--" )    
            print("=---------------------------=")
            print("Your loan is due in 7 days.")

        elif len(self.book) <1:
            print("Title cant be blank.")
        
        else:
            result = {}
            for title in self.books:
                Ratio = round(self.levenshtein_ratio_and_distance(self.book,title,ratio_calc = True),2)
                result[title] = Ratio
            
            final = max(result, key=result.get)
            
            if result[final]> 0.6:
                print("Did you mean ", final, "?")
            else:
                print("Title not found / On loan.")
                
       
    def add_books(self, book=None):
        """
        a method to add the book back to the library after it is returned. 
        This method takes the name of the book and add it to the list of available books. 
        
        """
        
        self.book = book 
        if self.book in self.onloan:
            self.books.append(book)
            print("You have returned")
            print("=---------------------------=")
            print("=--", self.book.title(),"=--" )    
            print("=---------------------------=")
            print("Thank you.")
    
        else:
            print("You haven't previously borrowed this book.")

    def DisplayMenu(self):
        # Display Menu Screen
        
        print("\n*********************************")
        print("1. Display all available books")
        print("2. Request a book")
        print("3. Return a book")
        print("Q. Quit")
        print("\nEnter your choice: ", end = "")

class Student():
    
    """
    Student Class, inherited from Library class. 
    Student interacts with library management system.
    

    Methods
    -------
    request_book
        Asks the user to enter the name of the book they want to borrow and returns the name of the book.
        
    return_book
        Asks the user to enter the name of the book they want to return and returns the name of the book.

    """
    
    def requestBook(self):
        
        self.book = input("Request a book.").title()
        #print("You have requested ", self.stu_book)
        return self.book
    

    def returnBook(self):
        
        self.book = input("Return a book").title()
        return self.book
    


def main():
    import numpy as np

    LibraryBooks = Library(['The Last Battle', 'The Screwtape Letters', 'The Great Divorce'])
    OrignalBooks = Library
    student = Student()
    Choice = ""
    print("\n*********************************")
    print("***** Welcome to OOP Library ****")
    print("*********************************")
        
        
    while Choice != "Q":
        LibraryBooks.DisplayMenu()
        Choice = str(input()).upper()
        
        if Choice == "1":
            LibraryBooks.display_available_books()
            
        elif Choice == "2":
            LibraryBooks.lend_books(student.requestBook())
            
            
        elif Choice == "3":
            LibraryBooks.add_books(student.returnBook())
        
        elif Choice == "Q":
            print("press Enter to close.")
            input()
        else:
            print("Only choose from the option above!!!!")


if __name__ == "__main__":
    main()   