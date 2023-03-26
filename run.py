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
    There must be exactly 4 numbers separated by commas.
    """
    while True:
        print("." * 50)
        print("Please enter the number of orchids you ordered for sale.")
        print("Type numbers separated by commas in the following order:\n")
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


def get_sales_num():
    """
    Requests a number from the user for each colour of orchids sold.
    A while loop will ask for the input all over again
    until the data entered is valid. 
    There must be exactly 4 numbers separated by commas.
    """
    while True:
        print("." * 50)
        print("Please enter the number of orchids you sold.")
        print("Type numbers separated by commas in the following order:\n")
        print(" white\n pink\n yellow\n purple\n")
        print("Example: 25, 30, 50, 45")
        print("." * 50)

        sales_num = input("Enter numbers here: ")
        print(f"Your entered {sales_num}\n")

        sales_num_data = sales_num.split(",")
        
        if valid_data(sales_num_data):
            print("Data is valid\n")
            break
    return sales_num_data


def calculate_surplus(sales_row):
    """
    Calculates surplus subtracting sold items from bought ones.
    """
    print("Calculating surplus data...\n")
    bought = SHEET.worksheet("bought").get_all_values()
    bought_row = bought[-1]

    surplus_data = []
    for bought, sales in zip (bought_row, sales_row):
        surplus = int(bought) - int(sales)
        surplus_data.append(surplus)

    return surplus_data   


def update_worksheet(bought_data, worksheet):
    """
    Gets a list of numbers to be inserted into a worksheet.
    Updates the relevant worksheet.
    """
    print(f"Updating the {worksheet} worksheet with new information...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(bought_data)
    print(f"{worksheet} worksheet updated successfully\n")


def get_last_week_sales():
    """
    Gets columns of data for the last 7 days(a week).
    Returns the data as a list of lists.
    """
    sales = SHEET.worksheet("sales")

    columns = []
    for ind in range(1, 5):
        column = sales.col_values(ind)
        columns.append(column[-7:])

    return columns


def calculate_recommendation(sales_data):
    """
    Calculates the average week's sales for each item colour.
    Adds 5%
    """
    print("." * 50)
    print("Calculating the average week's sales...\n")

    recommendation = []

    for column in sales_data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / 7
        recomend_num = average * 1.05
        recommendation.append(round(recomend_num))
        
    return recommendation

    print("Updating recommended amount of items to buy...\n")
    update_recommendation_worksheet = SHEET.worksheet("recommendation")
    update_recommendation_worksheet.append_row(recommendation)
    print("Recommendation worksheet updated successfully\n")


def get_money_spent(bought_row):
    """
    Calculates money spent for each type.
    Takes a number of ordered orchids and multiplies by trade price.
    Trade price is 7 euros.
    Updates the worksheet with costs data.
    """
    print("Calculating costs...\n")
    bought_money = []
    for bought in bought_row:
        bought_money_spent = int(bought) * 7
        bought_money.append(bought_money_spent)
    
    bought_money_worksheet = SHEET.worksheet("bought-money")
    bought_money_worksheet.append_row(bought_money)
    print("Worksheet updated successfully\n")


def get_money_earned(sales_row):
    """
    Calculates money earned for each sold item type.
    Takes a number of sold orchids and multiplies by retail price.
    Retail price is 9 euros.
    Updates the worksheet with new data.
    """
    print("Calculating earned money...\n")
    sales_money = []
    for sales in sales_row:
        sales_money_earned = int(sales) * 9
        sales_money.append(sales_money_earned)
    
    #sales_money_worksheet = SHEET.worksheet("sales-money")
    #sales_money_worksheet.append_row(sales_money)
    #print("Worksheet updated successfully\n")


def main():
    """
    Runs all main functions 
    """
    bought_data = get_bought_num()
    bought_data_int = [int(num) for num in bought_data]
    update_worksheet(bought_data_int, "bought")
    sales_data = get_sales_num()
    sales_data_int = [int(num) for num in sales_data]
    update_worksheet(sales_data_int, "sales")
    new_surplus = calculate_surplus(sales_data)
    update_worksheet(new_surplus, "surplus")
    money_spent = get_money_spent(bought_data)
    money_earned = get_money_earned(sales_data)   
    sales_cols = get_last_week_sales()
    recommendation_data = calculate_recommendation(sales_cols)
    update_worksheet(recommendation_data, "recommend")
    

print("." * 50)
print("Welcome to Orchid Shop data automation")
main()

