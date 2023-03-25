import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('orchid-shop')


def get_bought_num():
    """
    Requests a number from the user
    for each colour of orchids bought to the stock.
    A while loop will ask for the input all over again
    until the data entered is valid. 
    There mush be exactly 4 numbers separated by commas.
    """
    while True:
        print("." * 50)
        print("Please enter the number of orchids you ordered for sale.")
        print("Type numbers separated by comma in the following order:\n")
        print(" white\n pink\n yellow\n purple\n")
        print("Example: 25, 30, 50, 45")
        print("." * 50)

        bought_num = input("Enter numbers here: ")
        print(f"Your entered {bought_num}\n")

        bought_num_data = bought_num.split(",")
        
        if valid_data(bought_num_data):
            print("Data is valid\n")
            break
    return bought_num_data


def valid_data(values):
    """
    Validates the user's input to be a list of 4 numbers.
    If there are not exactly 4 numbers 
    or they are not numbers, raises ValueError.
    """
    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
                f"You should enter 4 numbers. You entered {len(values)}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, try again, please.\n")
        return False

    return True


def update_bought_worksheet(bought_data):
    """
    Updates the bought worksheet with numbers of items bought to stock.
    Adds a new row of data to the list.
    """
    print("Updating the worksheet with new information...\n")
    bought_worksheet = SHEET.worksheet("bought")
    bought_worksheet.append_row(bought_data)
    print("Worksheet updated successfully\n")


def calculate_money_spent(bought_money_data):
    """
    Calculates money spent for each type to calculate profit later.
    Takes a number of ordered orchids and multiplies by trade price.
    Trade price is 7 euros.
    """
    print("Calculating costs...\n")
    bought_money = bought_data * 7
    bought_money_worksheet = SHEET.worksheet("bought-money")
    bought_money_worksheet.append_row(bought_money_data)
    print("Worksheet updated successfully\n")

     
   


def main():
    """
    Runs all main functions 
    """
    bought_data = get_bought_num()
    bought_data_int = [int(num) for num in bought_data]
    update_bought_worksheet(bought_data_int)
    calculate_money_spent(bought_data_int)


print("." * 50)
print("Welcome to Orchid Shop data automation")
main()