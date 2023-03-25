import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('orchid-shop')

def get_colour():
    """
    Requests the colour of orchids from the user 
    """
    print("." * 40)
    print("Please enter the colour you'd like to enter data about.")
    print("Type w for white, p for pink, y for yellow, p for purple.")
    print("." * 40)

    colour = input("Enter the letter here: ")
    print(f"Your entered {colour}")

get_colour()