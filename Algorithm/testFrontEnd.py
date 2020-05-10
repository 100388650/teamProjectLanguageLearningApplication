# A test front end for the algorithm
from tkinter import *
import database
import functions
import json
from datetime import datetime

countCard = 0

root = Tk()

# Variables START
# Database variables START
all_cards = database.get_new_cards() # All cards currently stored
to_study = database.return_review_cards() # Cards to study
cardCorrect = False
no_of_cards_left = len(to_study)
no_of_total_cards = len(all_cards)
# Database variables END

cards = {}
cards['cards'] = []
cards['cards'].append({
    'cardId': '0',
    'category': '0.1',
    'front_content': 'wordA',
    'back_content': 'wordA_answer',
    'userId': '0',
    'firstAccessed': datetime.date(2020,5,1)
})
cards['cards'].append({
    'cardId': '1',
    'category': '0.1',
    'front_content': 'wordB',
    'back_content': 'wordB_answer',
    'userId': '0',
    'firstAccessed': datetime.date(2020,4,1)
})
cards['cards'].append({
    'cardId': '2',
    'category': '0.1',
    'front_content': 'wordC',
    'back_content': 'wordC_answer',
    'userId': '0',
    'firstAccessed': datetime.date(2020,3,1)
})

local_to_study_card_id = [] # Push in cards to study from the local JSON
local_to_study_card_cat = []
local_to_study_card_front = []
local_to_study_card_back = []

no_of_total_local_cards = len(cards)
no_of_to_study_local_cards = len(local_to_study_card_id)
# Variables END

# Algorithm functions START
with open('cards.txt', 'w') as output:
    json.dump(cards, output)


def generate_fib(): # A function for generating the fibonnaci sequence numbers for the daily cards
    a,b = 1,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b


def localGetCards(userID):
    # This function is for getting locally stored cards at the start of the study session
    amountToFetch = database.amountToFetch
    with open('cards.txt') as cards:
        cardData = json.load(cards)
        for c in cardData:
            if c['userId'] == userID:
                # 'amountToFetch' amount of new cards are fetched
                if (c['category'] == 0.1) or (c['category'] == 0.2) or (c['category'] == 0.3):
                    i = 0
                    while i <= amountToFetch:
                        local_to_study_card_id.insert(c['id'])
                        local_to_study_card_cat.insert(c['category'])
                        local_to_study_card_front.insert(c['front_content'])
                        local_to_study_card_back.insert(c['back_content'])
                        i = i + 1
                else:
                    # For cards that are not new, only get them if they are to be reviewed on the current date
                    todayDate = datetime.today()
                    dateToCheck = c['firstAccessed']
                    differenceToCheck = todayDate - dateToCheck
                    fib = generate_fib()
                    fibs = [next(fib) for _ in range(differenceToCheck)]
                    # Get the number of fibonacci places equal to the days the program has been used for
                    if differenceToCheck in fibs:
                        # This will check if the difference between the current date and the 'first accessed' date of the card,
                        # which stores the date that the card was assigned it's current category, is in the fibonacci sequence.
                        # If so, then it is flagged as to be reviewed. If not, it is ignored.
                        local_to_study_card_id.insert(c['id'])
                        local_to_study_card_cat.insert(c['category'])
                        local_to_study_card_front.insert(c['front_content'])
                        local_to_study_card_back.insert(c['back_content'])


def checkCard(currentCardNo, userInput): # Checks the user's answer for the cards fetched from the database
    if all_cards[currentCardNo] == userInput:
        cardCorrect = True
    else:
        cardCorrect = False


def localCheckCard(currentCardNo,userInput): # Checks the user's answer for cards saved locally

    with open('cards.txt') as cards:
        cardData = json.load(cards)
        for c in cardData:
            i = 0
            while (i < no_of_to_study_local_cards):
                if c['cardId'] == currentCardNo:
                    if userInput == c['back_content']:
                        cardCorrect = True
                        return cardCorrect
                    else:
                        cardCorrect = False
                        if (i == (no_of_to_study_local_cards)):
                            cardCorrect = False # Error handling in case the card does not exist
                            error = "Error: the card does not exist."
                            return error
                        else:
                            i = (i+1)


def localUpdateCard(studiedId, cardCategory, success):
    # Removes the last studied card from the deck
    # if the category is not 0.1, 0.2 or 0.3
    if (cardCategory != 0.1) and (cardCategory != 0.2) and (cardCategory != 0.3):
        if success:
            cardIndex = local_to_study_card_id.index(studiedId)
            # The above gets the index of the card to be updated, in the arrays, so it can be
            # updated in all the arrays below)
            local_to_study_card_id.pop(cardIndex)
            local_to_study_card_front.pop(cardIndex)
            local_to_study_card_back.pop(cardIndex)
            local_to_study_card_cat.pop(cardIndex)
            newCardCategory = (cardCategory +1)
            oldCardCategory = cardCategory
            # The JSON file is updated below, with the new category
            with open("cards.txt", "r") as cards:
                cardsData = cards.read()
            cardsData = cardsData.replace(oldCardCategory,newCardCategory)

            with open('cards.txt','w') as cards:
                cards.write(cardsData)
        else:
            # If the answer was not correct, then the category is reduced by one instead
            cardIndex = local_to_study_card_id.index(studiedId)
            # The above gets the index of the card to be updated, in the arrays, so it can be
            # updated in all the arrays below)
            local_to_study_card_id.pop(cardIndex)
            local_to_study_card_front.pop(cardIndex)
            local_to_study_card_back.pop(cardIndex)
            local_to_study_card_cat.pop(cardIndex)
            newCardCategory = (cardCategory - 1)
            oldCardCategory = cardCategory
            # The JSON file is updated below, with the new category
            with open("cards.txt", "r") as cards:
                cardsData = cards.read()
            cardsData = cardsData.replace(oldCardCategory, newCardCategory)

            with open('cards.txt', 'w') as cards:
                cards.write(cardsData)
    else:
        # Else, the card is currently in the 'initial review' phase (category 0.1, 0.2 or 0.3)
        # so it is not deleted from the current card stack unless it is 0.3
        if (cardCategory == 0.1) or (cardCategory == 0.2):
            newCategory = (cardCategory + 0.1)
            cardIndex = local_to_study_card_id.index(studiedId)
            local_to_study_card_cat[cardIndex] = newCategory
        else:
            # Make the category '1' and remove it from the 'to study' deck
            oldCardCategory = cardCategory
            newCardCategory = 1
            cardIndex = local_to_study_card_id(studiedId)
            local_to_study_card_id.pop(cardIndex)
            local_to_study_card_front.pop(cardIndex)
            local_to_study_card_back.pop(cardIndex)
            local_to_study_card_cat.pop(cardIndex)

            # The JSON file is updated below, with the new category
            with open("cards.txt", "r") as cards:
                cardsData = cards.read()
            cardsData = cardsData.replace(oldCardCategory, newCardCategory)

            with open('cards.txt', 'w') as cards:
                cards.write(cardsData)

# Algorithm functions END

# GUI elements START

def iterateCard(countCard):
    # Iterates by 1 when the user presses 'submit'
    # It is used in fetching the next card or ending the study session
    countCard = countCard + 1
    return countCard

user_id_form = Entry(root).place(x=95, y=180)
user_id = user_id_form.get()
start_study_session = Button(root, text="Start studying", command=localGetCards(user_id))
show_card_front = Label(root, text=local_to_study_card_front[countCard], font=("Arial", 36), compound=CENTER)
user_answer = Entry(root).place(x=95, y=260)
submit_answer = Button(root, text ="Submit answer", command=localCheckCard(user_answer.get()))
show_card_back = Button()
currentCardCategory = local_to_study_card_cat[countCard]
currentCardId = local_to_study_card_id[countCard]
next_card_button = Button(root, text="Get next card", command= lambda :[iterateCard(countCard), localUpdateCard(currentCardId,currentCardCategory,cardCorrect)])
# GUI elements END
