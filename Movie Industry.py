import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="rachelHenderson",
    database="movieindustry",
    autocommit = True
)

mycursor = mydb.cursor()

print("""***************  WELCOME TO THE **MOVIE INDUSTRY** DATABASE.  ***************")
************  PLEASE SELECT AN OPTION BY TYPING '1', '2', or '3'.  ************")
1.) Display tables within the database.
2.) Check data within the database.
3.) Input data into the database.
********************************************************************************""")

def sd():
        for x in mycursor:
                print(x)

        #sh_data is like, show data.

def mce():
        mycursor.execute(sql, query)

        #mce is like, shorthand for mycursor.execute
                
## initial input = i 
i = int(input ("ENTER VALUE: "))
e = "****GREAT! NOW ENTER...***"
#tables to select = tts 
tts =    """AVAILABLE TABLES TO SELECT:
    1. movie cast | 2. studio employees | 3. movie
    4. studio | 5. theater | 6. tickets
    Type a number to choose a table: """

if (i == 1):
        print(tts)
        di = int(input ("ENTER VALUE: "))                  
        if (di == 1):
                mycursor.execute("DESCRIBE cast")
                sd()
                                                                                      
if (i == 2):
        print(tts)
        si = int(input ("ENTER VALUE: "))                                 
        if (si == 1):
                print("DISPLAYING ALL CAST MEMBERS: ")
                mycursor.execute("SELECT * FROM cast")
                sd()
        
        elif (si == 2):
                print ("DISPLAYING ALL STUDIO EMPLOYEES : ")
                mycursor.execute("SELECT * FROM employees")
                sd()
        
        elif (si == 3):
                print ("DISPLAYING ALL MOVIES WITHIN THE DATABASE: ")
                mycursor.execute("SELECT * FROM movie")
                sd()

        elif (si == 4):
                print ("DISPLAYING ALL STUDIOS WITHIN THE DATABASE: ")
                mycursor.execute("SELECT * FROM studio")
                sd()

        elif (si == 5):
                print ("DISPLAYING ALL THEATERS WITHIN THE DATABASE: ")
                mycursor.execute("SELECT * FROM theater")
                sd()

        elif (si == 6):
                print ("DISPLAYING ALL PURCHASED TICKETS: ")
                mycursor.execute("SELECT * FROM tickets")
                sd()

if(i == 3):
        print(tts)
        ii = int(input("ENTER VALUE: "))
        if (ii == 1):
                f_name = input("First name: ")
                l_name = input("Last name: ")
                role = input("Role (in movie): ")
                m_title = input("Name of movie they starred in: ")
                #m_title = movie title

                sql = "INSERT INTO cast (f_name, l_name, role, m_title) VALUES (%s, %s, %s, %s)"
                query = (f_name, l_name, role, m_title)
                mce()
  
        elif (ii == 2):
                f_name = input("First name: ")
                l_name = input("Last name: ")
                position = input("Position: ")
                salary = input("Salary: ")

                sql = "INSERT INTO employees (f_name, l_name, position, salary) VALUES (%s, %s, %s, %s)"
                query = (f_name, l_name, position, salary)
                mce()

        elif (ii == 3):
                print(e)
                movie_title = input("The movie's title: ")
                star_rating = input("The movie's star rating (1 lowest, 5 highest: ")
                genre = input("The movie's genre: ")
                tickets_sold = input("# of tickets this movie sold: ")

                sql = "INSERT INTO movie (movie_title, star_rating, genre, tickets_sold) VALUES (%s, %s, %s, %s)"
                query = (movie_title, star_rating, genre, tickets_sold)
                mce()

        elif (ii == 4):
                print(e)
                address = input("The studio's address: ")
                employee_pop = input("The # of employees at this studio: ")
                name = input("The name of this studio: ")

                sql = "INSERT INTO studio (address, employee_pop, name) VALUES (%s, %s, %s)"
                query = (address, employee_pop, name)
                mce()

        elif (ii == 5):
                print(e)
                name = input("The theater's name: ")
                screens = input("# of screens: ")
                address = input("The theater's address: ")

                sql = "INSERT INTO theater (name, screens, address) VALUES (%s, %s, %s)"
                query = (name, screens, address)
                mce()

        elif (ii == 6):
                print(e)
                color = input("The ticket's color: ")
                movie_title = input("The title of movie the ticket purchases access to: ")
                price = input("The ticket's price: ")

                sql = "INSERT INTO tickets (color, movie_title, price) VALUES (%s, %s, %s)"
                query = (color, movie_title, price)
                mce ()
                
                
                



  
                
