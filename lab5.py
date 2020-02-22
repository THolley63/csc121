import random

def print_intro():
    
    print(
        "Welcome to Camel!")
    print()
    print(
        "In your desperation, you have stolen a camel" 
        " to make your way"
        )
    print(
        "across the great Mobi desert."
        )
    print(
        "The locals want their camel"
        "back and are chasing you down!"
        )
    print(
        "Survive your desert trek and out run the locals."
        )

choices = '''
A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop for the night.
E. Status check.
Q. Quit.
'''
    

def main():
    done = False
    thirst = 0
    miles = 0
    tiredness = 0
    locals_distance = -20
    drinks = 3

    print_intro()
    while not done:
        print(choices)
        oasis = False
        choice = input('What is your choice? ') 
        choice = choice.lower()
        if choice == "q":
            done = True    
        elif choice == "e":
            print(f'Miles traveled: {miles}')
            print('Drinks in canteen:', drinks)
            print('The locals are {} miles beind you.'.format(
                -locals_distance)
            )
        elif choice == "d":
            #Stop for the night
            tiredness = 0
            print('Your camel is happy.')
            locals_distance += random.randrange(3, 11)

        elif choice == 'c':
            #Full speed
            miles += random.randrange(10, 21)
            print(f"You've traveled {miles} miles.")

            thirst += 1
            tiredness += random.randrange(1, 4)
            if random.randrange(10) == 0:
                oasis = True

        elif choice == 'b':
            #Moderate speed
            miles += random.randrange(5, 13)
            print(f"You've traveled {miles} miles.")
            thirst += 1
            tiredness += 1

        if thirst > 4 and thirst <= 6:
            print('You are thirsty')

        elif thirst > 6:
            print("You died of thirst")
            done = True

        if tiredness > 5 and tiredness <= 8:
            print("Your camel is tired")

        elif tiredness > 8:
            print("Your camel is dead.")
            done = True
        
        elif choice == 'a':
            #Drink from canteen
            drinks += -1
            thirst = 0
            print("You drank from your canteen.")
            
        if locals_distance > 15 and locals_distance < 0:
            print('The locals are getting close')

        if locals_distance >= 0:
            done = True

        if drinks <= 0:
            print("Your canteen is out of water.")

        if miles >= 200:
            print("You have escaped! You win!")
            done = True

        if oasis:
            print('You found an oasis')
            thirst = 0
            drinks = 3
            tiredness = 0
            pass




if __name__ == '__main__':
    main()