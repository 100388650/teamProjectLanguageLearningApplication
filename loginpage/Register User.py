"""
This code will be used on the registration form.
The user will input their username and password that they wish to register with.
The database will check if that username already exists.
If the username does not exist then the user will be added to user database.
If the username does exist an error will pop up and they will be prompted to enter a new username.
"""
import psycopg2
from datetime import date

userExists = True
userRegistered = False

while userExists:
    newUsername = input("Enter your username: ")
    password = input("Enter your password: ")
    connection = psycopg2.connect(user="", # The connections information is entered here
                                  password="",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    try:
        cursor = connection.cursor()

        postgreSQL_select_Query = "select * from Users" # Selects all users in the database

        cursor.execute(postgreSQL_select_Query)
        user_records = cursor.fetchall()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    if newUsername in user_records:
        userExists = True
        print(
            "That username is already in use: please choose a new one.")  # The user should be able to enter a new username and resubmit it after this point
    else:
        userExists = False

print("That username is available for use. Registering you...")
        # Additional user information generated below
        dateOfRegistration = str(date.today())
        # The user information is added to the database below
        connection = psycopg2.connect(user="",  # The connections information is entered here
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Users (userID, password, date) VALUES (%s, %s, %s)",(newUsername,password,dateOfRegistration)) # Inserts the user's information into the database

        except (Exception, psycopg2.Error) as error:
            print("Error whilst registering user: ", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("User successfully registered")
                userRegistered = True
                print("PostgreSQL connection is closed")
