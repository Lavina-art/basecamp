inventory = []
puzzle_hint = ""

def add_item(item):
    inventory.append(item)
    print(f"\nYou stored [{item}] in your infinite pocketspace!")

def show_inventory():
    print("\n=== INVENTORY ===")
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(f"- {item}")

def hint(puzzle):
    print("=== HINT ===")
    if puzzle_hint == "":
        print("No hint!")
    else:
        print(puzzle_hint)

def menu():
    print("\n=== MENU ===")
    print("1. Continue")
    print("2. Inventory")
    print("3. Stop Game")
    #print("4. Background music")
    print("4. A tippie is not a biggy C:")

    while True:
        keuze = input("Choose an option: ")
        if keuze == "1":
            break

        elif keuze == "2":
            show_inventory()
            print("\n1. Continue")
            print("2. Inventory")
            print("3. Stop Game")
            print("4. Hint")

        elif keuze == "3":
            print("\nMaybe I'll see you next time!")
            exit()

        elif keuze == "4":
            hint(hint)
            print("\n1. Continue")
            print("2. Inventory")
            print("3. Stop Game")
            print("4. Hint")


        else:
            print("Invalid")

def vraag(vraagtekst):
    while True:
        antwoord = input(vraagtekst)

        if antwoord.lower() == "menu":
            menu()
        else:
            return antwoord

def check_menu(answer):
    if answer.lower() == "menu":
        menu()

def next_value():
    while True:
        antwoord = input("") #Press 'Enter' to continue

        if antwoord.lower() == "menu":
            menu()
        else:
            return antwoord

#Still have to make a def of the inventory :3 We can do it!

#Start of the game
print("Welcome to HR Mystery!")

while True:
    ready = vraag("Are you ready to play? (yes/no): ")

    if ready.lower() == "no":
            print("Maybe next time!")
            break

    elif ready.lower() == "yes":
        while True:
            uitleg = vraag("Do you want an explanation? (yes/no):")

            if uitleg.lower() == "yes":
                print("\nIn this game you have to solve a missing case.")
                print("Search for clues.")
                print("Answer questions.")
                print("Find the truth.")

                next_value()

                print("\nPress 'Enter' to continue")
                print("Type 'menu' to go into the menu")

                break
            elif uitleg.lower() == "no":
                break
            else:
                print("Please type 'yes' or 'no'")

        next_value()
        
        print("\nThe game starts now!")

        #Point of view from missing person!
        print("\n point of view from '???'")
        print("\n___________________________________")
        print("\nIt's a cold night at Hogeschool Rotterdam.")
        print("You are on your way home after a long day of classes")

        next_value()

        print("Suddenly you realise you've forgotten your bag.")
        print("With a sigh, you turn around and head back inside.")

        next_value()

        print("\nAs you walk towards your classroom,")
        print("you hear a loud noise coming from somewhere nearby.")

        while True:
            follow = vraag("\nDo you want to follow the sound? (yes/no): ")

            if follow.lower() == "yes":
                print("\nYou carefully follow the sound.")
                break

            elif follow.lower() == "no":
                print("\nYou decide to ignore the sound.")
                print("You continue walking towards your classroom.")
                print("Then you remember that your bag is somewhere in that direction")
                print("With no other choice, you keep walking.")
                break

            else: 
                print("\nPlease enter 'yes' or 'no'")

        next_value()

        print("\nThe hallway becomes darker.")
        print("The sound suddenly stops.")
        print("You slowly walk around the corner.")

        next_value()

        print("\nOn the floor, you find your bag.")
        print("Something looks strange.")
        print("There is a note sticking out of it.")

        while True:
            pick_up = vraag("\nType 'pick up' to pick up your bag: ")
            
            if pick_up.lower() == "pick up":
                print("\nYou pick up your bag.")
                break
            else:
                print("Please type 'pick up'")

        print("\nThe note says:")
        print("'Meet me in room B302 at 21:00.'")

        next_value()

        print("\nYou don't remember putting this note in your bag.")
        print("Someone must have placed it there.")

        next_value()

        print("\nYou look at your phone.")
        print("21:00.")

        print("\nYou: What the...?")


        while True:
            choice = vraag(
            "\nWhat do you want to do?\n"
            "A. Go to room B302\n"
            "B. Leave the building\n"
            "Choose A or B: ")

            if choice.upper() == "A":
                print("\nYou decide to go to room B302.")
                break
                
            elif choice.upper() == "B":
                print("\nYou decide to leave.")
                print("This is way too weird.")
                print("You quickly walk towards the exit.")
                break
            else:
                print("Please enter 'A' or 'B'")

        next_value()

        print("\nYou push against the door.")
        print("Nothing happens.")

        print("\nYou try again.")

        next_value()

        print("\nThe door won't open.")
        print("Every exit is locked.")

        next_value()

        print('\nYou: What the helly...?')

        next_value()

        print("\nYour eyes fall back on the note.")
        print("'Meet me in room B302 at 21:00.'")

        next_value()

        print("\nLooks like you don't have much of a choice.")

        next_value()
        
            
        #Point of view from the detective
        print("\nPoint of view from the detective")
        print("\n_______________________________________")
        print("\nTwo weeks later...")
        
        print("\nThere has been a missing case regarding a college student.")
        print("You have been given the task of finding evidence for the missing case.")

        next_value()

        print("\nThe last time the student has been seen was 2 weeks before at school.")
        print("The student has been known for staying at school till night.")
        print("It has been stated that nobody decided to report it at first, but people began to get worried about this person's whereabouts.")
        
        next_value()

        print("\nYou don't really want to take on the case...")
        print("This case in particulair makes you feel uneasy for some reason...")

        TakeCase = vraag("Should I take on a different case?(yes/no) ")
        if TakeCase == "yes":
            print("\nThe detective sergeant comes through the door.")
            print("'On the other hand, I guess I shouldn't disobey my superiors... '")
        elif TakeCase == "no":
            print("'I shouldn't do that'")
        else:
            print("\n...")
            print("\nThere is no escaping out of this.")

        next_value()

        print("\n3 hours later...")

        next_value()

        print("\nLooks like this is the place the missing person has been seen last.")
        print("There is a sign above the school, 'Hogeschool Rotterdam'")
        print("The school has been closed for the week...")
        print("It has been snowing so the school decided to close because of safety reasons.")

        next_value()

        print("\nYou have been given a warrant for permission to search on the school premise.")
        print("You sigh as the cold takes a hold on you.")

        print("\n'Where should I start investigating...'")

        print("1. > Around the school.")
        print("2. > Inside the school.")

        while True:
            answer = vraag("Choose option 1 or 2 ")
            if answer == "1":
                print("|Search around the school|")
                print("\nIt's currently still snowing.")
                print("'It is very cold.'")

                next_value()

                print("\nI'm slowly making my way to the schoolground.")
                print("I am shivering...")
                break
            elif answer == "2":
                print("|Search inside the school|")
                print("My shoes are leaving footprints on the snow...")

                next_value()

                print("\nI make up my way to the school.")
                print("The school gates won't budge...")

                next_value()

                print("[There is a combination lock on the schoolgate]")
                print("'Maybe I should search around the school first anyway.'")
                break
            else:
                print("Looks like you wanted a 3rd option...? ")
                print("Welp. Too bad! Try again!")

        next_value()

        print("\nWalking...")

        next_value()

        print("\nYou barely see something sticking out of the snow.")

        next_value()

        print("\nYou found... [rope]?")
        add_item("rope")

        next_value()

        print("\nYou examine the rope in your hands.")
        print("It feels worn and dirty, as if it has been used recently.")

        next_value()

        print("\nA chill runs down your spine...")
        print("What was it doing here?")

        next_value()

        print("\nYou keep walking...")

        puzzle1_running = True
        while puzzle1_running:
            print("\n1. > Look under a stone.")
            print("2. > Search in a tree.")
            print("3. > Search the trashbin nearby.")
            print("4. > Look up in the sky.")
            print("5. > Found everything?")
            choose = vraag("Choose one of the options above! ")
            if choose == "1":
                while True:
                    print("\nYou find a fragment of a note.")
                    print("\n'I am the number of little pigs in a famous story.'")
                    answer1 = vraag("What number am I? (type a number)")
                    if answer1 == "3":
                        print("You chose the number 3.")
                        print("That is the correct answer.")
                        next_value()
                        break
                    else:
                        print("Silly! That's not the correct answer =D")
            
            elif choose == "2":
                while True:
                    print("\nYou see another fragment of a note")
                    print("\n 'A cube has this many faces.'")
                    answer3 = vraag("What number am I? (type a number)")
                    if answer3 == "6":
                        print("Which kindergartener has left this behind?")
                        print("The answer is of course 6")
                        next_value()
                        break
                    else:
                        print("The correct answer just facepalmed ;-;")
                        next_value()

            elif choose == "3":
                while True:
                    print("\nYou climb up and find a fragment of a note.")
                    print("\n'I am the number of points on a star.'")
                    answer2 = vraag("What number am I? (type a number) ")
                    if answer2 == "5":
                        print("You chose the number 5.")
                        print("That is the correct answer.")
                        next_value()
                        break
                    else:
                        print("...")
                        print("'Let me try that again.'")
                        next_value()

            elif choose == "4":
                print("\nUm, why are you looking up in the sky?")
                print("There is nothing to see but the snow falling down the sky")
                next_value()
            elif choose == "5":
                while True:
                    answer1 = vraag("which answer is question 1? ")
                    print("type 'exit' if you want to exit 'found everything?'")
                    if answer1 == "3":
                        answer2 = vraag("which answer is question 2? ")
                        if answer2 == "5":
                            answer3 = vraag("which answer is question 3? ")
                            if answer3 == "6":
                                print("\n'The equivalent of '365' connects to a year...?'")
                                next_value()
                                print("\nMaybe this is a hint for the schoolgate lock.")
                                next_value()
                                print("\nYou obtain a [note with the number '365']")
                                add_item("A note with the number '365'")
                                puzzle1_running = False
                                break
                    elif answer1 == "exit":
                        break

        print("\nYou feel like you have explored everything outside.")

        next_value()

        print("\nYou walk back to the front of the school.")

        next_value()

        print("\nYou see a sign on the schoolgate.")

        next_value()

        print("'The school is \033[1mcurrently\033[0m closed.'")

        next_value()

        print("\n'Why is one word emphasized?'")

        next_value()

        print("\nYou try to open the schoolgate.")

        next_value()

        print("\nIt doesn't open.")

        print("\nYou try the gate again, harder this time.")

        next_value()

        print("\nIt still doesn't open.")
        print("The metal rattles loudly in the silence.")

        next_value()

        print("\n'Ah...'")
        print("\nYou weren't paying attention to the combination lock on the schoolgate.")
        print("You should have known.")

        next_value()

        print("\nYou thought maybe someone would still be at school.")

        next_value()

        print("\nYou look back at the combination lock.")
        print("A thin layer of snow is covering it.")

        next_value()

        print("\n[It has a 4 digit number lock]")

        next_value()

        print("\n'A 4 digit lock..?'")
        print("The note in your pocket might contain a hint...")

        next_value()

        puzzle_hint = "'The school is \033[1mcurrently\033[0m closed.'"
        
        code1 = True
        while code1:
            lock = vraag("Input a 4 digit code: ")
            if lock.isdigit() and len(lock) == 4:
                #change the code to 2027 when the year = 2027
                if lock == "2026":
                    print("The schoolgate is opening..")
                    puzzle_hint = ""
                    code1 = False
                else:
                    print("The lock doesn't budge.")
            else:
                print("Try again!")

        next_value()

        print("'Huff... Who thought of this stupid code??'")

        print("\033[2mme :)\033[0m")
        
        inventory.remove("A note with the number '365'")

        next_value()

        print("\nYou are glad to have found the code to the schoolgate")

        next_value()

        print("\nYou shiver as you enter the school")
        print("That was very cold.")

        next_value()

        print("\nIt is very dark..")
        print("All the lights in the building are off.")

        next_value()

        #maybe you find a light switch to turn on the power or you get a flashlight somewhere or your phone flashlight
        #maybe task to find or turn on light, or just do everything
        
            
        break
    else:
        print("Please enter 'yes' or 'no'.")

#idee raadsel
#Abcderfffdjcj llg 
#Om dit op te lossen als raadsel, krijg je ergens anders in de lokaal een hint om een generator te gebruiken en andere letters kan shuffelen ( A = B, B = C etc)
#Misschien staat er in dit gibberish woord “look under the cupboard” en als je dat doet vindt je een object

#spelling class: kaoamakos
# idea: put the word/sentence in a right order 

# math class: 87+9*8-5/9
# the answer is the number of…

#video evidence in security room. he gets in and finds the pov of the student we played in the beginning and we seem him only disappearing and then it has missing footage
#maybe you found sunglasses outside that are a little broken or a piece of fabric, it was thrown out of the window and is from the missing student in a struggle
#if you use an item, it will get removed from your backpack cuz you used it .remove()
# you also DO have a swatch for blood but not in your inventory and a phone maybe for the flashlight or checking time? or you have to check time via clocks in the school buildings
#locker of missing student with a burned doll

#locker van tweede missing student lijkt suspicious, pasje van tweede op de grond en hij lijkt de dader te zijn. maar hij is dood en geframed