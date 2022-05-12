# This is the contact book project in python
# Things that a user can do are add contact, update and delete contact

#create a dictionary hold the details of the users

#variables
name = ""
phone_number = ""
email = ""

contact_list = {}

#This function allow the user to add a new contact to the contact lists
def add():
    name = input("Name: ")
    phone_number = input("Phone number: ")
    email = input("email: ")
    contact_list[name] = [phone_number,email]

#create a function to update user details
def update():
    to_update = input("Enter name of the contact your want to update: ")
    if to_update in contact_list:
        print("what do you want to update:\n1. Phone number\n2.Email\n3.Both")
        response = int(input(">>> "))
        if response == 1:
            new_phone_number = input("Enter new phone number: ")
            contact_list[to_update] = [new_phone_number,email]
        elif response == 2:
            new_email = input("Enter new email")
            contact_list[to_update] = [phone_number,new_email]
        elif response == 3:
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            contact_list[to_update] = [new_phone_number,new_email]
        else:
            print("Wrong Input")
    else:
        print("Contact not in contact list")

# this function allows you to rerun the program to perform another task1
def run_again():
    print("Do you want to perform another task on your contact lists")
    response = input("Yes/No: >>>")
    if response == "Yes" or "Y" or "YES" or "yes":
        return main()
    elif response == "No" or "N" or "no" or "NO":
        print("You exited")
    else:
        print("Invalid response")

# function to delete a contact
def delete_contact():
    to_delete = input("Enter the name of the contact you want to delete: ")
    if to_delete in contact_list:
        del contact_list[to_delete]
    else:
        print("Contact does not exist")
    

    
# main function        
def main():
    print("______MY CONTACT BOOK______")

    print("Contact List is empty")
    print("1. Add new contact")
    print("2. update an existing contact")
    print("3. delete a contact")
    response = int(input(">>> "))
    if response == 1:
        add()
        print(contact_list)
        run_again()
    elif response == 2:
        update()
        print(contact_list)
        run_again()
    elif response == 3:
        delete_contact()
        print(contact_list)
        run_again()
    else:
        print("Wrong input")
        
            
main()


