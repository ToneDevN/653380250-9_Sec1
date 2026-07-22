import os;

class  ContactBook:
    def __init__(self):
        self.contact_book = {}

    def is_valid_phone(self, phone : int) -> bool:
        if (phone < 10):
            return False
        return True

    def create_or_update_user_data(self) -> str:
        try:    
            name = str(input("Enter name: "))
            if (name in self.contact_book):
                print(f"\n=== Update Contact :{name} ===\n")
            phone = int(input("Enter phone number: "))
            if not (self.is_valid_phone(phone)):
                return "Invalid phone number. Please try again."
            email = str(input("Enter email: "))
            self.contact_book = {
                name : {
                    "phone" : phone,
                    "email" : email
                }
            }
            return f"\nContact '{name}' Saved sucessfuly";
        
        except ValueError:
            return "Invalid input. Please try again."

    def show_user_contact_detail(self):
        try:
            name = str(input("Enter name: "))
            if name not in self.contact_book:
                raise ValueError
            return f"Name: {name}, Phone: {self.contact_book[name]['phone']}, Email: {self.contact_book[name]['email']}"
        except ValueError:
            return "Contact not found. Please try again."
            
    def show_all_contacts(self):
        for contact in self.contact_book:
            print(f"Name: {contact}, Phone: {self.contact_book[contact]['phone']}, Email: {self.contact_book[contact]['email']}")
        return;
    def delete_contact(self):
        try:
            name = str(input("Enter contect name to delete :"))
            if name not in self.contact_book:
                raise ValueError
            self.contact_book.pop(name)
            return f"Contact '{name}' deleted sucessfuly"
        except ValueError:
            return "Contact not found. Please try again."

def chose_choice(contactbook : ContactBook,choice : int) -> str:
    match choice:
        case 1:
            return contactbook.create_or_update_user_data();
        case 2:
            return contactbook.show_user_contact_detail();
        case 3:
            return contactbook.show_all_contacts();
        case 4:
            return contactbook.delete_contact();

def main():
    contactbook = ContactBook()
    while True:
        print("\n=== Contact Book Manager ===")
        print("1. Add/Update Contact")
        print("2. View Contact Details")
        print("3. List All Contacts")
        print("4. Delete Contact")
        print("5. Exit\n")
        try:
            choice = int(input("Enter choice (1-5):"))
            if choice > 5 or choice < 1:
                raise ValueError
            message = chose_choice(contactbook, choice)
            if choice == 5:
                print("Exiting Contact Book Manager. Goodbye!")
                break
            print(message)
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
        except KeyboardInterrupt:
            print("Exiting Contact Book Manager. Goodbye!");
            break;
        

if __name__ == "__main__":
    os.system("clear");
    main()
            


