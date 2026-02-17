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
password_correct: bool = False
#Ask the user to provide their username.
print("Enter username: ")
username: str = input()
#Check if the username is in the dictionary. If it is not, print an error and exit.
if(username not in login_system):
    print("User not found. Exiting.")
#If the username is valid, ask the user to provide their password.
print("Enter password: ")
password: str = input()
#Check if the provided password matches the one stored in the dictionary for that user.
if(password != login_system.get(username)):
    print("Access Denied.")
else:
    password_correct = True
#If the password is correct, assign a security level.
if(password_correct == True):
    #If the user is "guest", assign a "Guest" security level. 
    if(username == "guest"):
        print(f"Welcome, {username}. You have Guest access.")
    #For all other valid users, assign a "Security Level 1".
    else:
        print(f"Welcome, {username}. You have Security Level 1")
#The program should end by printing a greeting to the username and letting them know their security level.
#If the password is incorrect, print an "Access Denied" message and exit.