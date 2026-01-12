balance = 0.0
kyc_documents = {}

def check_balance():
    print(f"Your balance is {balance}")
    print("====================================================")

def deposit(amt):
    global balance
    if amt > 0:
        balance += amt
    else:
        print("You cannot deposit negative and zero amount")
        print("====================================================")

def withdraw(amt):
  global balance
  if amt <= 0:
      print("You cannot withdraw negative and zero amount")
  elif amt > balance:
      print("invalid amount . insufficient balance")
  else:
       balance -= amt
  print("====================================================")

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)


def check_kyc():
     if len(kyc_documents) == 0:
         print("kyc not done")
         print("====================================================")   
     else:
          for docs in kyc_documents:
              print(f"{docs} : {kyc_documents[docs]}")
     print("====================================================")

if __name__ == "__main__":

    print("====================================================")
    print("Welcome to the HDFC bank")
    print("====================================================")
    print()

    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. update kyc")
        print("5. check kyc")
        print("6. Exit")

        choice = input("Enter your choice: ")
        print("====================================================")

        if choice == "1":
            check_balance()

        elif choice == "2":
            amt = float(input("Enter the amount to deposit: "))
            deposit(amt)
            print(f"amount {amt} successfully deposited")
            print("====================================================")

        elif choice == "3":
            amt = float(input("Enter the amount withdrawing: "))
            withdraw(amt)
            print(f"amount {amt} successfully withdrawn")
            print("====================================================")

        elif choice == "4":
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to add: "))
            for i in range (n_documents):
                key = input("Enter the document type: ")
                value = input("Enter the document number: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print(" kyc updated")
            print("====================================================")

        elif choice == "5":
            check_kyc()

        elif choice == "6":
            print("Quiting !! Have a good day")
            break

        else:
            print("an invalid choice !! Re- try")
            print("====================================================")
    print()
    print("Thank you for banking with us ")



