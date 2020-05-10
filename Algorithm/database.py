import psycopg2
from psycopg2 import sql
import functions

amountToFetch = 10
newCat = "example" # The new category is defined here, when a card has been reviewed
currentCard = "example" # The card currently being reviewed is defined here
userId = 123 # The ID of the currently logged in user is defined here

connection = psycopg2.connect(user="",
                                  password="",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
cursor = connection.cursor()

# Get new cards:
# Get amountToFetch amount of new cards where category == Null
# Get review cards:
# If the interval between current date and the date of category change fits into
# a fibonacci value, then get the card
    # Get the interval from functions.py's start_of_study_check()
# Else, ignore the card
# Put all cards into an array

def get_new_cards():
    try:
        # First get the new cards
        postgreSQL_select_Query = sql.SQL("select * from cards where category IS NULL and userId = ($i)").format(sql.Identifier(userId))
        cursor.execute(postgreSQL_select_Query)
        new_cards = cursor.fetchmany(amountToFetch) # Limits the number of rows fetched by 'amountToFetch'
        return new_cards
    except:
        error = "Error"
        return error
        # Throw appropriate error here

def return_review_cards():
    try:
        # First get all cards except Null ones
        postgreSQL_select_Query = "select id, category, content, firstDayUsed from cards where category IS NOT NULL" # The program will parse through categories and store the ids of cards that are to be reviewed
        cursor.execute(postgreSQL_select_Query)
        all_cards = cursor.fetchall()
        review_cards = []
        i = 0
        while i <= all_cards.length:
            for row in all_cards:
                cardId = row[0]
                firstDayUsed = row[3]
                if functions.start_of_study_check(firstDayUsed): # The program will append the card to the review cards array if the card is on a 'review day' (as defined by the fibonacci sequence)
                    review_cards.append(cardId)
                    i = (i+1)
                else:
                    i = (i+1)
        return review_cards
    except:
        error = "Error"
        return error
        # Throw appropriate error here


def update_new_card(answer, cardId, category):
    # Updates the new cards for the current study session (category A, B and C cards)
    newCat = functions.calculate_next_cat(answer,category) # This returns the new category
    postgreSQL_select_Query = sql.SQL("update cards set category = ($s) where id = ($d) and userId = ($i)").format(sql.Identifier(newCat, cardId, userId))
    cursor.execute(postgreSQL_select_Query)


def update_card(answer, cardId, category):
    newCat = functions.calculate_next_date(answer, category) # This returns the new category
    postgreSQL_select_Query = sql.SQL("update cards set category = ($d) where id = ($d) and userId = ($i)").format(sql.Identifier(newCat, cardId, userId))
    cursor.execute(postgreSQL_select_Query)