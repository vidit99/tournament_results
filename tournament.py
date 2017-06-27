
#!/usr/bin/env python

# tournament.py 

# implementation of a Swiss-system tournament


import psycopg2


def connect():
    """Connecting to PostgreSQL. It Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
	"""Remove the match records from database."""
	database1 = connect()
	cursor1 = database1.cursor()
	cursor1.execute("delete from matches")
	database.commit()
	database.close()


def deletePlayers():
	"""Remove the player records from database."""
	database1 = connect()
	cursor1 = database1.cursor()
	query="DELETE FROM PLAYERS"
	cursor1.execute(query)
	database1.commit()
	database1.close()

def countPlayers():
	"""Returns number of players which are present."""
	database1= connect()
	cursor1 = database1.cursor()
	query = "SELECT COUNT(*) AS total FROM players"
	cusror1.execute(query)
	number = cursor1.fetchone()
	database1.commit()
	database1.close()
	
	return number[0]


def registerPlayer(name):
	"""Adds a player to the tournament database.

	The database assigns a unique serial id number for every player. 
	
	(This should be handled by your SQL database schema, not in your Python code)

	Args:
		
		name: the player's name which is need not to be unique.
    
	"""
	database1 = connect()
	cursor1 = database1.cursor()
	query = "INSERT INTO players (name) values (%s)"
	cursor1.execute(query, (name,))
	database1.commit()
	database1.close()


def playerStandings():

    """Returns list of the players with their win records ,sorted by wins.

    The first entry in the list should be the player in first place, 
	
	or a player tied for first place if there is a tie.

    Returns:
	
      A list of tuples, each of which contains (id, name, wins, matches):
	  
        id: the player's unique id given by database
        
		name: Player's full name (as registered)
		
        wins: number of matches player has won
        
		matches: number of matches  layer has played
    
	"""

    database1 = connect()
    cursor1 = database1.cursor()
    query="""SELECT * FROM WIN_VIEW"""
    cursor1.execute(query)

    rank = cursor1.fetchall()

    database1.commit()
    database1.close()

    return rank


def reportMatch(Winner, Loser):
   
    """Record outcome of a single match between two players 
	
	and tells us about the winner and loser of a match.

    Args:
	
      winner:  the id number of the player who won the match
      
	  loser:  the id number of the player who lost the match
    
	"""

    database1 = connect()
    cursor1 = database1.cursor()
    cursor1.execute(" INSERT INTO  match (p1, p2, Winner)"
              "VALUES (%s, %s, %s);",((Winner,), (Loser,), (Winner,)))
    database1.commit()
    database1.close()


def swissPairings():
    
	""" Returns list of pairs of players for next round of a particular match.

	Assuming that there are an even number of players registered ,

	each player appears exactly once in the pairings . Each player is paired 
	
	with another player with an equal or nearly-equal win record, 
	
	that is, a player adjacent to him or her in the standings.

	Returns:
	
		List of tuples, each of which contains (id1, name1, id2, name2)
        
		id1: first player unique id number
       
		name1: first player full name
        
		id2: second player unique id
        
		name2: second player full name
    
	"""

	database1 = connect()
	
	cursor1 = database1.cursor()

	c.execute('SELECT * from WIN_BY_PLAYER_ORDERED_VIEW')

	listp = cursor1.fetchall()

	database1.commit()
	
	database1.close()

	pairing = []

	for j, player in enumerate(listp):
    
		if j % 2 == 0:
			pairs = (listp[j][0],
					listp[j][1],
					listp[j+1][0],
					listp[j+1][1])
			pairing.append(pairs)

	return pairing

