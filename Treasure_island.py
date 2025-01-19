



print( '''  
      
      
      
      __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________  
      
      
      
      '''
)





print('Welcome to the Treasure Island !')
print("Your mission is to find the treasure !")

choice1 = input('\'You are at  a crossroad, where do you want to go ?\n Type "Right" or "Left" ').lower()

if choice1 =="left":
    choice2 =input('You have came to the lake.\n '
          'There is an island in the middle of the lake.\n'
          'Type "wait" to wait for a boat.\n'
          'Type "swim" to swim across.\n').lower()
    
    
    if choice2 =="wait":
        choice3 = input("Your are arrived to the island unharmed.\n"
                        "There is house with the 2 doors. One red ,\n"
                        "One Yellow and One blue\n"
                        "Which colour do you want to choose.\n").lower()
        
        
        if choice3 =="red":
            print("It is full of fire. You lose\n")
        elif choice3 =="Yellow":
            print("you are out of the game . Heavy snowfall.\n")
        else:
            print("Finally you find the treasure.\n")
        
        
    else:
        print("You are out 'cause you are attacked by rhino.\n")


else:
    print("You lose !. Play once more")
    
print("Bye ")



