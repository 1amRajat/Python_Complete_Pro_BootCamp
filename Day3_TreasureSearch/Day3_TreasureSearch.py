print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome tp Treasure Island. \n Your mission is to find the Treasure")
choice1 = input("You're at a cross road. Where would you like to go? Type 'Left' or 'Right' \n").lower()
if choice1 == 'left':
    choice2 = input("You've come near lake. Either you can swim across or wait for the boat. Type 'Swim' or 'Wait' \n").lower()
    if choice2 == 'wait':
        choice3 = input("You've arrived at the castle. There are 3 doors there : Red, Blue & Yellow. Where do you wish to enter? \n").lower()
        if choice3 =='red':
            print("You're burned by fire. Game Over!")
        elif choice3 == 'blue':
            print("You're eaten by beasts. Game Over!")
        elif choice3 == 'yellow':
            print('You Win!')
        else:
            print('Game Over!')
    else:
        print("You've been attacked by a trout. Game over!")
else:
    print("You've fallen into the hole. Game over!")