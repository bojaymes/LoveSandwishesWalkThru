import gspread
from google.oauth2.service_account import Credentials

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
    """
    print("Please enter sales data from the last market")
    print("Data should be six numbers seperated by commas.")
    print("Example: 30,21,20,14,6,25\n")

    data_str = input("Please enter your data here: ")
    print(f"The data provided is: {data_str}")

get_sales_data()


