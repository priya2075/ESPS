"""

    Title: Python assignment for Singapore Polytechnic
    Desc: Electronic Services and Protection Services Application
    Author: Priya 
    Group: DICS1
    Assignment Part 2 - Client

"""

"""
    
    I will not post the entire codes here to prevent from plagarism. 
    
    But I am sharing the codes added for server + client socket programming using python
    
"""



#-------------------------------------------------------------------------------------- IMPORT STUFF
# import sys to use sys.exit 
# import datetime to display date and time for receipt 
# import locale to add comma and $ to computed numbers
# import random to display receipt number
import sys, datetime, locale, random
# import tabulate for pretty table display
from tabulate import tabulate 
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# seed to repeat same random number per terminal run
random.seed()

# ASSIGNMENT 2
from collections import Counter # for top-selling products to display. Information gathered from purchase receipt files
import os, socket, uuid # Universally Unique Identifier (UUID4) to generate uuid for receipts, can download same receipt multiple times
print(os.getcwd()) # get current directory



#-------------------------------------------------------------------------------- ASSIGNMENT 2
# Get current day, date, and time
now = datetime.datetime.now()
current_day = now.strftime("%A")
current_date = now.strftime("%d-%m-%Y")
current_time = now.strftime("%I:%M %p")

# Define opening hours
opening_hours = {
    "Monday": "4am to 10pm",
    "Tuesday": "4am to 10pm",
    "Wednesday": "4am to 10pm",
    "Thursday": "4am to 10pm",
    "Friday": "4am to 10pm",
    "Saturday": "4am to 10pm",
    "Sunday": "4am to 10pm"
}

# Check if shop is currently open or closed
current_hour = int(now.strftime("%H"))
if current_day in opening_hours:
    opening_time, closing_time = opening_hours[current_day].split(" to ")
    opening_hour = int(opening_time.split(":")[0].replace("am", "").replace("pm", ""))
    closing_hour = int(closing_time.split(":")[0].replace("am", "").replace("pm", ""))
    if "pm" in closing_time:
        closing_hour += 12
    if current_hour >= opening_hour and current_hour < closing_hour:
        shop_status = "Currently Open"
    else:
        shop_status = "Currently Closed"
else:
    shop_status = "Not Available"


#-------------------------------------------------------------------------------------- STORE INFO
# Store tuples into a list to display ESP Services @ 1. Display/Add Services
items = [
    ("Firewall Service", 1200),
    ("Security Ops Center", 4200),
    ("Hot Site", 8500),
    ("Data Protection", 10000)
]
# Takes list of tuples and iterate through dictionary and append key-value pairs to dict_Results
# So basically, this code uses a dictionary comprehension to generate a dictionary
dict_Results = {key: value for key, value in items}
cart = [] # Stores user's selections in this cart
from random import random
receipt = random()
subscription_total = None

#-------------------------------------------------------------------------------------- 1. DISPLAY/ADD SERVICES   --  def display_services():

#-------------------------------------------------------------------------------------- 2. VIEW SERVICES   --   def view_services():

#-------------------------------------------------------------------------------------- 3. SEARCH SERVICES   --   def search_services():

#-------------------------------------------------------------------------------------- 4. REMOVE SERVICE(S)   --   def remove_services():

#-------------------------------------------------------------------------------------- 5. CHECKOUT CART   --   def checkout_cart():

#-------------------------------------------------------------------------------------- 6. MEMBERSHIP   --   def membership():



#-------------------------------------------------------------------------------------- 7. SOCKET CLIENT    --  def start_client():
#-------------------------------------------------------------------------------- ASSIGNMENT 2
def start_client():
    host = socket.gethostname()
    port = 8888
    # m is for members and s is for everyone to view their membership / purchase receipt
    valid_inputs = ['m', 's', 'q', 'x']  # valid input list, other alphabets are not allowed!

    while True:
        try:
            clientSocket = socket.socket()
            clientSocket.connect((host, port))
        except ConnectionRefusedError:
            print("\n>> Connection refused. The server is currently offline.\n")
            return

        print("\n\n================ VIEW PURCHASE / MEMBERSHIP DETAILS ================")
        # User login section
        while True:
            try:
                # input receipt number
                receipt_number = input("\n>> Enter your receipt number ['q' to quit | 'x' to shutdown server]: ").strip().lower()

                if receipt_number.strip().lower() == 'q':
                    print("\n>> Quitting server session...\n\n")
                    clientSocket.close()
                    return
                
                elif receipt_number.strip().lower() == 'x':
                    print("\n>> Shutting down server.")
                    clientSocket.send(b'x')
                    clientSocket.shutdown(socket.SHUT_WR)
                    response = clientSocket.recv(1024).decode('utf-8', errors='ignore')
                    print(response)
                    clientSocket.close()
                    return
                # input receipt type (m or s)
                receipt_type = input(
                    "\nReceipt Type:"
                    "\n- 'm' for membership"
                    "\n- 's' for sales" 
                    "\n>> Enter the receipt type: ").strip().lower()

                if receipt_type not in valid_inputs:
                    print("Invalid input. Please try again.")
                else:
                    break

            # I encountered issue during coding - I either press ctrl + c / z
            except (KeyboardInterrupt, EOFError):
                print("\nUser interrupted the program.")
                clientSocket.close()
                return

        # receipt_type is for m or s and filename is receipt number
        request = receipt_type + receipt_number
        clientSocket.send(request.encode('utf-8', errors='ignore'))
        clientSocket.shutdown(socket.SHUT_WR)
        response = clientSocket.recv(1024).decode('utf-8', errors='ignore')

        if response == 'File not found':
            print('\n>> Requested file not found on the server.')
            print('\n>> If you have a membership with us and are unable to view your subscription details:')
            print('\n>> Please contact us at +65 6001 1001, thank you! \n')
        else:
            print("\n>> Your receipt details:\n")
            print("\t/" * 7)
            print(response)
            print("\t/" * 7)

        clientSocket.close()



#-------------------------------------------------------------------------------------- 8. DOWNLOAD RECEIPT.TXT FILE TO CWD & USER'S HOME DIR   ------- ADDITIONAL FEATURE
#-------------------------------------------------------------------------------- ASSIGNMENT 2
def request_download():
    try:
        host = socket.gethostname()
        port = 8888
        downloads_folder = "Downloads"  # download to CWD folder
        user_home = os.path.expanduser("~")  # Get user's home directory downloads folder (using ~ for any OS users)
        cwd = os.getcwd()  # Get current working directory

        # Construct the download paths
        download_location_1 = os.path.join(user_home, downloads_folder)  # I want the file to download to our laptop and also
        download_location_2 = os.path.join(cwd, downloads_folder)  # download to this Assignment 2 downloads folder.

        # Create the download folders if they don't exist
        for location in [download_location_1, download_location_2]:
            if not os.path.exists(location):
                os.makedirs(location)

        clientSocket = socket.socket()
        clientSocket.connect((host, port))

    except ConnectionRefusedError:
        return "\n>> Connection refused. The server is currently offline.\n"

    while True:
        try:
            # Input from user - receipt number, q to quit
            receipt_number = input("\n>> Enter your receipt number ['q' to quit | 'x' to shutdown server]: ").strip().lower()

            if receipt_number.strip().lower() == 'q':
                clientSocket.close()
                return "\n>> Quitting server session...\n"
            if receipt_number.strip().lower() == 'x':
                clientSocket.send(b'x')
                clientSocket.shutdown(socket.SHUT_WR)
                response = clientSocket.recv(1024).decode('utf-8', errors='ignore')
                clientSocket.close()
                if response == "!!! You have exited the server.\n\n":
                    return response
                else:
                    return "\n>> Server did not respond properly.\n"

            receipt_type = input(
                "\nReceipt Type:"
                "\n- 'm' for membership"
                "\n- 's' for sales"
                "\n>> Enter the receipt type: "
            ).strip().lower()

            if receipt_type not in ['m', 's']:
                print("\nReceipt Type: \n- 'm' for membership \n- 's' for sales \n>> Enter the receipt type: ")
                continue

            # Perform a basic authentication check based on the receipt number itself
            authenticated = receipt_number
            if not authenticated:
                print("Access denied. Authentication failed.")
                continue

            # receipt_type is for m or s and filename is receipt number
            request = receipt_type + receipt_number
            clientSocket.send(request.encode('utf-8', errors='ignore'))
            clientSocket.shutdown(socket.SHUT_WR)
            response = clientSocket.recv(1024).decode('utf-8', errors='ignore')

            if response == 'File not found':
                if receipt_type == 'm':
                    print(f"\n>> Receipt file not found for receipt number {receipt_number} in Membership folder.")
                else:
                    print(f"\n>> Receipt file not found for receipt number {receipt_number} in Sales folder.")
            else:
                folder = "Membership" if receipt_type == 'm' else "Sales"
                unique_id = str(uuid.uuid4())  # Generate a unique identifier - UUID
                file_path_1 = os.path.join(download_location_1, f"{receipt_number}_{unique_id}.txt")
                file_path_2 = os.path.join(download_location_2, f"{receipt_number}_{unique_id}.txt")
                # fulfil the WRITE requirement
                with open(file_path_1, "w") as f1, open(file_path_2, "w") as f2:
                    f1.write(response)
                    f2.write(response)

                print(f"\n>> Your receipt {receipt_number} from {folder} has been downloaded to:")
                print("-" * 71)
                print("Location 1")
                print(f"{file_path_1}")
                print("\nLocation 2")
                print(f"{file_path_2}\n\n")

                # Write download details to a text file
                # if download_log.txt file does not exist, it automatically creates it
                download_log_file = "download_log.txt"
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # append to download log file
                with open(download_log_file, "a") as log_file: # fulfil the APPEND requirement
                    log_file.write(f"Receipt Number: {receipt_number}\n")
                    log_file.write(f"Timestamp: {timestamp}\n")
                    log_file.write(f"Downloaded File: {file_path_1}\n")
                    log_file.write(f"Downloaded File: {file_path_2}\n")
                    log_file.write("-" * 180 + "\n")
            return None
        
        # I encountered issue during coding - I either press ctrl + c / z
        except (KeyboardInterrupt, EOFError):
            print("\nUser interrupted the program.")
            clientSocket.close()
            return None

#-------------------------------------------------------------------------------------- B. MAIN MENU LOOP
while True:
    main_Menu()
    option = input("\n\t  >> Please input your choice of action: ")
    if option.strip() == "1":
        display_services()


    #-------------------------------------------------------------------------------- START ASSIGNMENT 2
    elif option.strip() == "6": # 7.SOCKET CLIENT
        start_client()
        if option.strip() == " ":
            print("\n>> Quitting server session...")
            break
        elif option.strip() == " ":
            print("\n>> Shutting down server.")
            break

    elif option.strip() == "7":  # 8. DOWNLOAD RECEIPT.TXT
        print("\n\n=============== PURCHASE / MEMBERSHIP RECEIPT DOWNLOAD =============")
        response = request_download()
        if response is not None:
            print(response)
        
    elif option.strip() == "111": # 9. DISPLAY TOP-SELLING ITEMS 
        get_most_purchased_items()
        print("\n\n======================= TOP SELLING SERVICES =======================")
        print("\n>> These are the items that are top-selling at ESP:")
        print("-" * 68)
        # Get top selling items 
        topSellingItems = get_most_purchased_items()
        # Collate them
        collated_items = collate_purchases(topSellingItems)
        # Display in into a table
        if collated_items:
            headers = ["No.", "Items", "Top Selling Services"]
            table_data = [(index+1, item, count) for index, (item, count) in enumerate(collated_items)]
            print(tabulate(table_data, headers=headers, tablefmt="rounded_grid", stralign="left", numalign="left", colalign=("center", "left", "center")))
            print("\n\n")
        else:
            print("No sales records found.")
    #-------------------------------------------------------------------------------- END ASSIGNMENT 2

    else:
        print("\n>> !!! You have selected an invalid option, please try again! \n\n")


#-------------------------------------------------------------------------------------- C. SOCKET CLIENT - ASSIGNMENT 2
if __name__ == '__main__':
    start_client()
