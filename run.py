import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('cred.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figure input from the user
    Run a While loop to collect valid number of datas (6 numbers seperated by commas) 
    from the user via the terminal, the loop will repeatedly ask for data until the 
    correct amount of data and correct type of data (integers) is supplied by the user
    """
    while True:
        print("Please enter sales data from the last market")
        print("Data should be six numbers seperated by commas.")
        print("Example: 30,21,20,14,6,25\n")

        data_str = input("Please enter your data here: ")
    
        sales_data = data_str.split(",")
    
        if validate_data(sales_data):
            print("Data is valid!")
            break
    
    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required! You provided {len(values)}")
    except ValueError as e:
            print(f"Invalid data {e}, please try again.\n")
            return False
    return True

def update_sales_worksheet(data):
    """
    This function updates the worksheet with the data entered by the user.
    Meaning, it adds a new row containing the data provided by the user everytime 
    user data is entered.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully!\n")

def calculate_surplus_data(sales_row):
    """
    Subtract number of sales from number of available stocks 
    to get the number of surplus for each item type.
    - postive surplus means "waste"
    - negative surplus means extra was made when stock was sold out
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data


def main():
    """
    run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]

    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    print(new_surplus_data)

print("Welcome to Love Sandwishes Data Automation")
main()



