class PhoneBook:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        PhoneBook.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Phone Number: {self.phone}"    
    
    @classmethod
    def show_all_contacts(cls):
            if len(cls.phone_directory) == 0:
                print("Phone book is empty.")
            else:
                for contact in cls.phone_directory:
                    print(contact.show_contact())    

    @classmethod
    def search_contact(cls, search_name):
            for contact in cls.phone_directory :
                 if contact.name.lower() == search_name.lower():
                    return contact.phone
            return  f"Contact not found {search_name}"
    
    @staticmethod
    def validate_phone_number(number):
            if len(number) >= 10 and number.isdigit():
                return True
            else:
                return False
            
n_contacts = int(input("Enter the number of contacts you want to add: "))   

for i in range(n_contacts):
     name = input("Enter the name: ")
     phone_number = input("Enter the phone number: ")
     if PhoneBook.validate_phone_number(phone_number):
          PhoneBook(name, phone_number)
     else:
          print("Invalid phone number. Please enter a valid number.")     

PhoneBook.show_all_contacts()          
                           