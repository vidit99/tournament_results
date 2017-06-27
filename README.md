Tournament-Results

My solution for the Tournament Results project. 

It is a Part of Udacity's full stack developer Nanodegree Course.

It is a python module to manage players, matches and number of matches won in a Swiss Style Tournament.

Instructions for running project.

1. Open terminal.

2. In terminal, type command vagrant up. The vagrant virtual machine will start.

3. In terminal, vagrant ssh to login to the virtual machine and cd /vagrant/tournament to go to the shared directory.

4. In the VM, type psql to start up postgres. For it use sudo apt-get install postgresql command to download postgres.

5. Create a database with CREATE DATABASE DATABASE_NAME;

6. Connect to the tournament database with \c DATABASE_NAME

7. Import the tables and views with \i DATABASE_NAME.sql 

8. to exit postgres type \q

9. Run the test cases with python tournament_test.py

10. If all test cases pass, things are good. 

11. Import tournament.py into your Python project and build the Swiss Style tournament app.


