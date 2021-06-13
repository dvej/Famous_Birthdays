This program is built to find famous people birthdays, count how many of them have a birthday in each month, and represent it visually.

List of options:
download - reads person names (not case sensitive) from bdays.txt, finds their birthdays on Wikipedia and load them to the list (old list will be deleted)
list - lists all persons which birthdays are loaded to the list
search - searches person in the list for his/her birthday (not case sensitive)
add - searches Wikipedia for birthday of the person user specifies, and adds it to the list. If person or person's birthday can't be found offers an option to enter birthday manually to the list
count - counts how many persons have a birthday in each month and offers to draw a histogram
save - saves list of birthdays to bdays.json file (old file will be overwritten)
help - prints this text
exit - exits program


Files:
birthdays.py - program file
bdays.txt - list of names which is used to find birthdays (file can be edited)
bdays.json - dictionary of saved names and birthdays which is automatically loaded upon starting the program
bdays.html - file created after confirming option to plot a histogram and presents distributions of birthdays per months 
help.txt - this file
requirements.txt - required packages for the program
