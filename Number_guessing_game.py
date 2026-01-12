import random
print(" welcome to the number guessing game . we have a number that needs to be guessed . you have 10 chances  ")
print(" the secret number is between 1 and 50")

counter = 0
rndm_num = random.randint(1, 50)
while counter < 10:
       your_num = int(input("enter your guess "))

       if your_num==rndm_num:
            print("you guessed correctly")
            print(f"the number was {rndm_num} .Game Over")
            break
       elif your_num < rndm_num:
            print("you guess is wrong . try higher")
            print(f"you have {9 - counter} chances left ")
            counter = counter + 1
       else:
            print("you guessed is wrong . try lower ")
            print(f"you have {9 - counter} chances left ")
            counter = counter + 1
       if counter == 10:
           print("you failed . out of chances")
           print(f"the number was {rndm_num} .Game Over")

