CREATE TALBLE users
/*Stores the user information*/
(userName VARCHAR(100) NOT NULL,
password VARCHAR(100) NOT NULL,
userId INT NOT NULL,
firstDayUsed DATE  NOT NULL,
CONSTRAINT Users_pkey PRIMARY KEY(userId));

CREATE TABLE cards
/*Stores the card information*/
(cardId NUMERIC(9) NOT NULL,
category decimal(6,1) NOT NULL,
front_content VARCHAR (100) NOT NULL,
back_content VARCHAR (100) NOT NULL,
firstAccessed DATE  NOT NULL,
userId INT NOT NULL
CONSTRAINT Cards_pkey PRIMARY KEY (cardId, userId),
CONSTRAINT users_Cards FOREIGN KEY (userId) REFERENCES users);