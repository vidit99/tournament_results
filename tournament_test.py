
#!/usr/bin/env python

# These tests are not exhaustive, but they should cover the majority of cases.

# If you do add any of the extra credit options, be sure to add/modify these test cases

# as appropriate to account for your module's added functionality.

# Test cases for tournament.py

from tournament import *


def testDeleteMatches():
    
	deleteMatches()
    
	print "1) Old match can be removed ."


def testDelete():
    
	deleteMatches()
    
	deletePlayers()
    
	print "2) Player records can be deleted."


def testCount():
    deleteMatches()
    deletePlayers()
    count = countPlayers()
    if count == '0':
        raise TypeError(
            " countPlayers() should return numeric value zero, not string value denoted by '0'.")
    if count != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "3. After deleting, countPlayers() returns zero."



def testRegister():
    
	deleteMatches()
    
	deletePlayers()
    
	registerPlayer("Vidit garg")
    
	count = countPlayers()
    
	if count != 1:
        
	   	raise ValueError("After 1 player registers , countPlayers() should be incremented to 1.")
    
	print "4. After registration of a player, countPlayers() returns 1."


def testRegisterCountDelete():
    
	deleteMatches()
    
	deletePlayers()
    
	registerPlayer("rakshit gupta")
    
	registerPlayer("krishan gupta")
    
	registerPlayer("sahil gupta")
    
	registerPlayer("nilay sagar")
    
	count = countPlayers()
    
	if count != 4:
        
	   	raise ValueError(
            
			"After registering 4 players, countPlayers should be incremented to 4.")
    
	deletePlayers()
    
	count = countPlayers()
    
	if count != 0:
        
		raise ValueError("After deleting, countPlayers should return zero value.")
    
	print "5. Players can be registered and deleted."




def testReportMatches():
	"""
	Test that matches are reported properly.
	Test to confirm matches are deleted properly.
    """
    
	deleteMatches()
    
	deletePlayers()
    
	registerPlayer("Vaishali arora")
    
	registerPlayer("Sahil singla")
    
	registerPlayer("Kanishka kalra")
    
	registerPlayer("Mehak Baweja")
    
	ranks = playerStandings()
    
	[id1, id2, id3, id4] = [row[0] for row in ranks]
    
	reportMatch(id1, id2)
    
	reportMatch(id3, id4)
    
	ranks = playerStandings()
    
	for (i, n, w, m) in ranks:
        
		if m != 1:
            
			raise ValueError("Each player should have one match in record.")
        
		if i in (id1, id3) and w != 1:
            
			raise ValueError("Each match winner should have one win in record.")
        
		elif i in (id2, id4) and w != 0:
            
			raise ValueError("Each match loser should have zero wins in record.")
    
	print "7. After a match, players have updated standings."


def testPairings():

	"""
    Test that pairings are generated properly both before and after match reporting.
    """
    
	deleteMatches()
    
	deletePlayers()
    
	registerPlayer("Rajat goel")
    
	registerPlayer("Tanvi jain")
    
	registerPlayer("Akshat prasad")
    
	registerPlayer("tejasya aggarwal")
    
	ranks = playerStandings()
    
	[id1, id2, id3, id4] = [row[0] for row in ranks]
    
	reportMatch(id1, id2)
    
	reportMatch(id3, id4)
    
	pairs = swissPairings()
    
	if len(pairs) != 2:
        
		raise ValueError(
            
			"For four players, swissPairings should return two pairs.")
    
	[(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairs
    
	right_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    
	main_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    
	if right_pairs != main_pairs:
        
		raise ValueError(
            
			"After one match, players with one win should be paired with each other and so on.")
    
	print "8. After one match, players with one win are paired with each other."


if __name__ == '__main__':
    
	testDeleteMatches()
    
	testDelete()
    
	testCount()
    
	testRegister()
    
	testRegisterCountDelete()
    
	testStandingsBeforeMatches()
    
	testReportMatches()
    
	testPairings()
    
	print "Success!  All tests pass!"
