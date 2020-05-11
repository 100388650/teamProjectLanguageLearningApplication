Currently, the algorithm is not fully functional. The reasons for this are reflected upon in
100495585's personal team log. Further details are given in the 'overview-watch-first' video as well.

The algorithm can be divided into 2 parts:
Database linked:
# This attempted to implement the algorithm by fetching data from a postgreSQL database
	database.py -> provides functionality to connect to a postgreSQL database
	databaseCreation.sql -> provides functionality to create the postgreSQL database
	functions.py -> provides functionality to the 

Locally stored:
# This attempted to implement the algorithm via locally stored cards
	exampleFrontEnd.py -> code that attempted to implement functionality for the algorithm using locally stored cards
				rather than fetching them from the database.
	cards.txt -> the cards to be used in exampleFrontEnd.py

$overview.txt -> this text file gives an overview of how I intended the algorithm to work
