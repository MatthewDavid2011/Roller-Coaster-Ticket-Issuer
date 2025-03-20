'''
Ticket issuing system that issues tickets based
on height and age.
'''

height = int(input("Enter your height"))

if height >= 120:
    age=int(input("What is your age"))
    if age <12:
        print("You have to pay £5")
    elif 12<age<18:
            print("You have to pay £7")
    elif age >=60:
         print("You can ride for free")
    
    else:
        print("You have to pay £12")
else:
    print("Sorry, You cant ride.")
    