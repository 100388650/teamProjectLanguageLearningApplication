function updateAnswer(answer) {
    // Shows the value of the current slider input in MapGdp/year_gdp.html
    document.getElementById('testAnswerText').value=answer;
}

@eel.expose
def get_new_cards():
    try:
        # First get the new car
        postgreSQL_select_Query = sql.SQL("select * from cards where category IS NULL and userId = ($i)").format(sql.Identifier(userId))
        cursor.execute(postgreSQL_select_Query)
        new_cards = cursor.fetchmany(amountToFetch) # Limits the number of rows fetched by 'amountToFetch'
        return new_cards
        except:
            error = "Error"
        return error
        # Throw appropriate error here
