import eel
import psycopg2
eel.init('loginpage')
startup_options = { #startup options for the app
    'mode': "chrome"
    'host': 'localhost',
    'port': 8080,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
    }
@eel.expose #allows the python function to be called as a JS function
def fetchLoginDetails(username): #gets usernames from the database
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

eel.start('language_learning_application_login_page.html', options=my_options)
