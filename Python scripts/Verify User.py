import psycopg2

loggedin = False
username = input("Username: ")

try:
    connection = psycopg2.connect(user="",
                                  password="",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from users"

    cursor.execute(postgreSQL_select_Query)
    user_records = cursor.fetchall()

    if username in user_records:
        loggedin = True
    else:
        loggedin = False

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

"""Once the users login is verified, they will be able to continue using the app; 
This will be done by having a variable set to true upon login and a while loops that runs
once this variable is true."""