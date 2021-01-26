# Login python scripts
import os
import time


def restart():
    # Asking user if they want to restart
    print("Do you wish to restart this program?")
    # Recives input
    restart = input("Y or N: ")
    # If user selects 'Y' then program will call main
    if restart == "Y":
        main()
    else:
        # Else if they don't pick 'Y" then program will exit saying goodbye!
        print("Goodbye!")
        quit()


# Main
def main():
    # Series of prints asking the user what they would like to do
    print("Welcome to Justins password storage software")
    print("1) Create a account")
    print("2) Log into a account")
    print("3) Delete all data")
    # Get's the input from the user, their option determines what the program does.
    option = input("1 or 2 or 3: ")

    if option == "1":
        # Get Website
        website_name = str(input("Enter the website name: "))
        # Get Username
        user_name = str(input("Enter username for account: "))
        # Get Password
        pass_word = str(input("Enter password for account: "))
        # Get Email
        email_addr = input("Enter Email for account: ")
        # Open/Create File 'accounts.txt'
        f = open("accounts.txt", "a+")
        # Write account details to accounts.txt
        f.write(f"{website_name}:{user_name}:{pass_word}:{email_addr}\n")
        # Always have to close the file after anything
        f.close()
        # Success message that it works
        print("Sucessfully wrote account details to file.")
        # Calls restart
        restart()

    elif option == "2":
        # Asks for the website name so it can search accounts.txt
        account_name = input("Please enter the website you want to search for: ")
        # Opens accounts.txt as read only
        f = open("accounts.txt", "r")
        # Looks at the lines of the file
        for line in f:
            # Splits them
            info = line.split("-")
            # If the account name is in the file, it'll print
            if account_name == info[0]:
                # Returns the info from the search
                return info[2]
        # Prints the info if there is any
        print(info)
        # Calls restart
        restart()
    else:
        # Checking to see if the file exists
        if os.path.isfile("accounts.txt"):
            # If the file exists, It will delete the file
            os.remove("accounts.txt")
            # Success message that the file was deleted
            print("Deleted accounts.txt")
            # Calls restart
            restart()
        else:
            # if the file name dosen't exists, prints this
            print("File doesn't exists!")
            # Calls restart
            restart()


# Main
if __name__ == "__main__":
    main()
