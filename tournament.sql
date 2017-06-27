--
-- Table definitions for the tournament project.
--
-- Import using PostgreSQL
--
-- Put your SQL 'create table' statements in this file; 
--
-- also 'create view' statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like--
--
-- Clean up any previous tournament databases
-- 

CREATE DATABASE tournament

\c tournament;


--creating players table
CREATE TABLE player (
    Id serial PRIMARY KEY,
    Name text NOT NULL
);


--creating match table
CREATE TABLE matches (
	p1 integer references player(Id),
	p2 integer references player(Id),
	Winner integer references player(Id),
	Loser integer references player(Id)
);


--creating view for counting total match
CREATE VIEW total_match AS
    SELECT (
    	SELECT count(*) 
    	FROM matches
    	) /
    	(SELECT count(*) / 2
    	FROM player
    	) AS roundcount;

--creating view for counting matches win		
CREATE VIEW win_count AS
SELECT player.Id, COUNT(matches.Winner) as winn
FROM player LEFT JOIN matches
ON player.Id = matches.Winner
GROUP BY player.Id;		
		
--creating view for finding rank		
CREATE VIEW ranking AS
    SELECT player.Id, player.Name, count(matches.Winner) AS rank_num, (SELECT * FROM total_match) as sum_matches
    FROM player LEFT JOIN matches
    ON player.Id = matches.Winner
    GROUP BY player.Id
    ORDER BY rank_num DESC;
    
