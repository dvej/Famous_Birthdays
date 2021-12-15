Birthdays List ver.1.0

This program is built to find famous people birthdays, create database, count how many of them have a birthday in each month, and represent it visually.


List of options:

View All - list whole database in Results box where each entry can be selected

Add from List - read names from 'Enter list..' box and try to retrieve their birthdays from Wikipedia
Names in the list should be entered one below another and they're not case or space sensitive.

Add Manually - insert data from fields: Name, Day, Month and Year to a database
Selected entries in Results box can also be updated with this option.

Search Database - search database by parameters from fields: Name, Day, Month or Year 
Database is searchable by one or more fields combined. 
Note: Name is unique field so it's not combined with others and it's not case sensitive.
Name and Year can be searched by partial data adding sign '%' at end of the entry.
Example 1: 'm% m%' in field Name can give results [Marko Marković, Miljan Miljanić, Mitar Mrkela]
Example 2: '196%' in field Year can give results [1963, 1965, 1968]

Delete Entry - delete selected entry

Births by Month - draw graphical representation showing birthdays per month

Exit - exit program


Files:
bdays.py - program start file
bdays_backend.py - database operations program file
bdays.db - database file (automatically created if not exists)
bdays.html - graph file of birthdays distibution (automatically created if not exists)
requirements.txt - required packages for the program
readme.txt - this file
