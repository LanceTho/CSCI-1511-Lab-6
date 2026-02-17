"""
Lab6_LanceTho-1.py
Lance Thongsavanh
Create a program that simulates a user login system using a dictionary to store usernames and passwords.
2/17/2026
"""

#Create a dictionary of at least four key-value pairs. Each key should be a unique username (string) and the associated value a password (string).
login_system = {
    "guest": "guest",
    "JohnSmith": "password123",
    "Subway": "E@tFr3sH",
    "McDonalds": "ImL0v1ngiT",
    "Nike": "jUstD01t"
}

#Ask the user to provide their username.
#Check if the username is in the dictionary. If it is not, print an error and exit.
#If the username is valid, ask the user to provide their password.
#Check if the provided password matches the one stored in the dictionary for that user.
#If the password is correct, assign a security level. #If the user is "guest", assign a "Guest" security level. For all other valid users, assign a "Security Level 1".
#The program should end by printing a greeting to the username and letting them know their security level.
#If the password is incorrect, print an "Access Denied" message and exit.
