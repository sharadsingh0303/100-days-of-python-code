print('''
*******************************************************************************
                                    Teasure
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first = input("Left or Right?\nType Right/Left: ").lower()
if first == "right":
    print('''                     -     =    .--._
                - - ~_=  =~_- = - `.  `-.
              ==~_ = =_  ~ -   =  .-'    `.
            --=~_ - ~  == - =   .'      _..:._
           ---=~ _~  = =-  =   `.  .--.'      `.
          --=_-=- ~= _ - =  -  _.'  `.      .--.:
            -=_~ -- = =  ~-  .'      :     :    :
             -=-_ ~=  = - _-`--.     :  .--:    D
               -=~ _=  =  -~_=  `;  .'.:   ,`---'@
             --=_= = ~-   -=   .'  .'  `._ `-.__.'
            --== ~_ - =  =-  .'  .'     _.`---'
           --=~_= = - = ~  .'--''   .   `-..__.--.
             --==~ _= - ~-=  =-~_-   `-..___(  ===;
          --==~_==- =__ ~-=  - -    .'       `---'
    ''')
    print("Sonic got the treasure before you, try again.")

elif first == "left":
    print("""  _
  | |
  | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __
  | __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \
  | |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
  \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/
                                                        | |
                                                        |_|
    """)
    print("Nice, you made it to the next level!")

second = input("Your map shows that you need to get to Treasure Island, you can wait to board a ship or swim accross the sea, pick one.\nType Swim/Wait: ").lower()
if second == "swim":
    print("""

                    (`.
                    \ `.
                      )  `._..---._
    \`.       __...---`         o  )
    \ `._,--'           ,    ___,'
      ) ,-._          \  )   _,-'
    /,'    ``--.._____\/--''
        """)
    print("Unfortunately, you were eaten by a Great White Shark, try again.")

elif second == 'wait':
    print("Nice, you made it to the next level, you're pretty good at this!")
    print("Welcome to:")
    print('''
     _                                     _     _                 _ 
    | |                                   (_)   | |               | |
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
    | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
    | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
    \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
    ''')

third = input(
    "Now that you've made it to Treasure Island, you can dig or search the cave. \n Type Dig/Cave: ").lower()

if third == 'dig':
    print("You've found the treasure, you win!")
elif third == 'cave':
    print('''
      _                     
      | |                    
      | |__   ___  __ _ _ __ 
      | '_ \ / _ \/ _` | '__|
      | |_) |  __/ (_| | |   
      |_.__/ \___|\__,_|_| 
    ''')
    print("you were eaten by bear")
