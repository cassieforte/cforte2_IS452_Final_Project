import sys # want to use .exit() to end the program for certain paths
import time #want to use the .sleep() function for flow

# when incorrect answers are typed
reminder = ("\nPlease choose left, straight, or right, only.")

# you will need the key to get into the closet in the bedroom to win the game
key = 0


# what happens when you find the key have to update
def findkey():
    global key # global variable
    print("You've found a key."
          "\nIt was just lying on the floor under some leaves.")
    key = key + 1
    print("You have,", key, "key.")
    Aviary()


# this is the player's input, changing throughout gameplay
choice = ""


# what happens if you die, the game just ends
def death():
    print("You have died.")
    time.sleep(1)
    print("Game Over.")
    time.sleep(8)
    sys.exit(0)



# what happens if you win, the game still ends
def victory():
    print("You have won!")
    time.sleep(8)
    sys.exit(0)

# what happens when you encounter a monster
def Monster():
    print("This is very, very, very bad, I'm afraid.")
    time.sleep(3)
    print("You've encountered a monster. It is large and hairy and full of teeth.")
    time.sleep(2)
    print("You cannot get away.")
    time.sleep(2)
    print("I told you it wasn't haunted - just infested with beasts.")
    death()


# intro to game that leads player to Foyer()
# the last else statement in Foyer runs intro()
def intro():
    print("Welcome to my house. People have said that it is haunted...")
    time.sleep(2)
    print("But you're too smart to believe a silly rumor like that. "
          "\nMy house is not haunted, and you will see for yourself!")
    time.sleep(6)
    Foyer()


# this function is for when the player is in the Foyer
# it's also the generic starting point of the game after the intro.
def Foyer():
    print("Welcome to the Foyer. This isn't one of my favorite rooms,"
          "\nbut it's still pretty good.")
    time.sleep(5)
    print("There's really just a table in here and some dead flowers. "
          "\nThere's better stuff to see."
          "\nYou should probably move on...")
    time.sleep(4)
    print("You can go [LEFT], [RIGHT], or [STRAIGHT].")

    time.sleep(3)
    print("Which way would you like to go?")
    choice = input("")
    choice = choice.lower().strip()

    if "left" in choice:
        Bathroom()
    elif "right" in choice:
        Garden()
    elif "straight" in choice:
        DiningRoom()
    else:
        print("Sorry, that was not a valid answer.")
        print(reminder)
        time.sleep(2)
        Foyer() # this will replay foyer so the game goes back to the beginning until a correct answer
                    # is submitted


# for when the player is in the Aviary - where key is located
def Aviary():
    print("You've entered the aviary, but there are no birds here anymore.")
    time.sleep(2)
    print("The plants are dead and the trees are sticks and you do not like it in here.")
    time.sleep(2)
    print("You think you hear the fluttering of wings...")
    time.sleep(5)
    print("The noise is getting louder and you know that it is time to go.")
    time.sleep(2)
    print("To your [LEFT] there is the husk of a tree, the concrete at its base split by roots.")
    time.sleep(2)
    print("Corpses of leaves skitter across the ground.")
    time.sleep(5)
    print("You look to the [RIGHT] and you don't really see anything..."
          "\nit's like there's a spot in your vision and you only see black.")
    time.sleep(5)
    print("[STRAIGHT] ahead, there's a glass door ajar leading to somewhere green, you think.")
    time.sleep(2)
    print("The aviary is old and unattended to, the windows and doors are grimy, thick with dirt.")
    time.sleep(2)
    print("But, are you sure of what you see...?")

    time.sleep(5)
    print("Which way would you like to go?")
    choice = input("")
    choice = choice.lower().strip()

    if "left" in choice:
        findkey() # runs the function that shows you've found the key to the closet
    elif "right" in choice:
        Monster() # player sent to Monster and death
    elif "straight" in choice:
        Garden() # player sent to the Garden
    else:
        print("Sorry, that was not a valid answer.")
        print(reminder)
        time.sleep(2)
        Aviary() # replays the room so an invalid answer doesnt break the game

# player is in the Kitchen
def Kitchen():
    print("Welcome to the kitchen!"
          "\nI don't spend much time here anymore...")
    time.sleep(3)
    print("The pipes have long rusted through and we haven't paid the gas bill in decades.")
    time.sleep(2)
    print("I think I still hear them screaming...")
    time.sleep(5)
    print("I take my meals here, if the occasion allows. Dinner guest are so few and far between.")
    time.sleep(5)
    print("You look [LEFT] and see a wooden archway, a warm light glowing from beyond.")
    time.sleep(2)
    print("To the [RIGHT], there are windows covered in filth; opaque from years of grime. And a door.")
    time.sleep(2)
    print("[STRAIGHT] ahead the door is closed; you're not sure where it leads.")
    time.sleep(5)

    print("Which way would you like to go?")
    choice = input("")
    choice = choice.lower().strip()

    if "left" in choice:
        DiningRoom() # player goes to dining room
    elif "right" in choice:
        Aviary()
    elif "straight" in choice:
        Bedroom()
    else:
        print("Sorry, that was not a valid answer.")
        print(reminder)
        time.sleep(2)
        Kitchen() # replay room if wrong answer - I also kind of hope having to go through the whole timed
                    # text block to get to the prompt would be annoying enough to discourage invalid answers

# player is in the Ballroom
def Ballroom():
    print("Ah, this room used to be one of my very favorites!"
          "\n Oh, the parties we had in here - I can still hear them:")
    time.sleep(4)
    print("The swishing of gowns floating across the marble floor,"
          "\n Glasses clinking in celebration, accompanying the band...")
    time.sleep(5)
    print("...")
    time.sleep(2)
    print("I miss it, sometimes...")
    time.sleep(3)
    print("To the [LEFT] there's a door framed by windows. Does it look green out there..."
          "\n or is something glowing?")
    time.sleep(3)
    print("If I was you, I'm not so sure I would even look to the [RIGHT]...")
    time.sleep(3)
    print("You'll have to go through a dark hallway if you go [STRAIGHT].")

    time.sleep(5)
    print("Which way would you like to go?")
    choice = input("")
    choice = choice.lower().strip()

    if "left" in choice:
        Garden()
    elif "right" in choice:
        Monster()
    elif "straight" in choice:
        Foyer()
    else:
        print("Sorry, that was not a valid answer.")
        print(reminder)
        time.sleep(2)
        Ballroom()

# player is in the Bedroom - where Closet is located to win
def Bedroom():
    print("My sleeping chamber - though I don't sleep anymore."
          "\nMy bride, she picked everything out - back when it was new. "
          "\nShe liked purples and blues, and the wallpaper was covered in flowers.")
    time.sleep(5)
    print("I wanted to vomit.")
    time.sleep(3)
    print("I remember walking in - her soft fingers covering my eyes."
          "\nShe smelled of lavender and honey - sweet, like a dessert.")
    time.sleep(5)
    print("She didn't taste that way, in the end."
          "\nShe was gritty and sinewy and flavorless.")
    time.sleep(5)
    print("I remember sprinkling salt - the crystals dissolving into charred flesh -"
          "\nhoping it would taste of anything.")
    time.sleep(5)
    print("You look around. There is a door to the [LEFT]. It's closed."
          "\nYou don't know what's on the other side.")
    time.sleep(5)
    print("To the [RIGHT], there is a sound. You don't turn to look that way."
          "\nIt is a chittering kind of sound -"
          "\nNo - a tapping kind of sound... you're not sure...")
    time.sleep(4)
    print("Don't turn.")
    time.sleep(2)
    print("[STRAIGHT] is another door; smaller but seemingly benign.")


    time.sleep(5)
    print("Which way would you like to go?")
    choice = input("")
    choice = choice.lower().strip()

    if "left" in choice:
        Bathroom()
    elif "right" in choice:
        Monster()
    elif "straight" in choice:
        if key >= 1:
            print("You have the key. You're ready to go in.")
            Closet() #add if/else statements, or not
        else:
            print("That way is locked - you must find a key.")
            Bedroom()
    else:
        print("Sorry, that was not a valid answer.")
        print(reminder)
        time.sleep(2)
        Bedroom()

# player is in the Dining Room
def DiningRoom():
    print("This room is lit - there are candles everywhere-"
          "\ncovering every surface, every piece of furniture."
          "\nIt looks like you're surrounded by ghosts, the furniture clad in white sheets.")
    time.sleep(6)
    print("The sheets billow gently from a phantom breeze. You feel its cold touch but no force."
          "\nThere is a fireplace, glowing embers in the cradle, and ash.")
    time.sleep(3)
    print("It's both a comfortable and unwelcoming room. It feels like you might be safe in here, maybe.")
    time.sleep(4)
    print("But you should persist."
          "\nTo the [LEFT] is a wooden door on a swing latch.")
    time.sleep(3)
    print("On your [RIGHT] there is another wooden door, with an impressive copper doorknob.")
    time.sleep(2)
    print("Looking [STRAIGHT], there is an important-looking archway, "
          "\nthe wood carved into cherubs and roses."
          "\nBeyond, a hallway growing darker; you can't see.")

    time.sleep(5)
    print("Which way would you like to go?")
    choice = input("")
    choice = choice.lower().strip()

    if "left" in choice:
        Kitchen()
    elif "right" in choice:
        Bathroom()
    elif "straight" in choice:
        Ballroom()
    else:
        print("Sorry, that was not a valid answer.")
        print(reminder)
        time.sleep(2)
        DiningRoom()

# player is in the Bathroom
def Bathroom():
    print("I didn't realize you had to... go."
          "\nWe could've stopped sooner, nobody wants an accident.")
    time.sleep(3)
    print("I know what you're going to say- "
          "\n'Who needs a bathroom this big?'")
    time.sleep(3)
    print("The answer is me. I can do whatever I like.")
    time.sleep(3)
    print("Do you need some more time in here?")
    time.sleep(2)
    print("This is getting weird.")

    time.sleep(5)
    print("Which way would you like to go?")
    choice = input("")
    choice = choice.lower().strip()

    if "left" in choice:
        Bedroom()
    elif "right" in choice:
        Aviary()
    elif "straight" in choice:
        Garden()
    else:
        print("Sorry, that was not a valid answer.")
        print(reminder)
        time.sleep(2)
        Bathroom()

# player is in the Garden
def Garden():
    print("Welcome to my garden, though I doubt you could call it that now.")
    time.sleep(2)
    print("There used to be rows and rows and rows of vegetables and herbs-"
          "\nall gone now.")
    time.sleep(3)
    print("There are things that prowl here at night now.")
    time.sleep(2)
    print("I don't know when they arrived, but they're here to stay.")
    time.sleep(2)
    print("I think it's getting dark - you want to head back.")
    time.sleep(2)
    print("To your [LEFT] there is a large, intimidating door.")
    time.sleep(2)
    print("To your [RIGHT], a pair of French doors, curtains billowing on the other side.")
    time.sleep(2)
    print("Hmm... going [STRAIGHT] looks remarkably similar to going [RIGHT]...")
    time.sleep(2)
    print("I wonder if you'll risk it.")

    time.sleep(5)
    print("Which way would you like to go?")
    choice = input("")
    choice = choice.lower().strip()

    if "left" in choice:
        Kitchen()
    elif "right" in choice:
        DiningRoom()
    elif "straight" in choice:
        Ballroom()
    else:
        print("Sorry, that was not a valid answer.")
        print(reminder)
        time.sleep(2)
        Garden()

# player is in the closet - checks for key - if key, then WIN
def Closet():
    print("You found a closet. You try the handle but it is locked."
          "Have you found the key?")
    time.sleep(3)
    if key >= 1:
        print("Well, that was rather lucky. That key had been lost for a very, very long time...")
        time.sleep(2)
        print("I was so looking forward to a new companion.")
        time.sleep(3)
        victory()
    else:
        print("It appears not - what terrible luck.")
        Bedroom()


intro()
