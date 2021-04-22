#       Expand your IDLE input, and Output window for a more in depth look at the code +
#                   In the output screen for a secret :D
#
import random   
import os
import time
from threading import Thread
import sys
#                ~~~      Ideas/Plan      ~~~
#   Make a story with a few bosses (That is purely luck!)
#   There is a few anime references because I just watched one (Demon Slayer)
#   The idea is to have multiple exits, make it somewhat frustrating but also fun
#   One way of making it fun –– having one guaranteed win (No spoilers of where)
#   Attempt to do something that I have never been able to do (Complication wise) 
#   Attempt to make a timer run while all the things are happening (I was somewhat successful but I didn't implement that into this program)
#   (I have to do a bit more research on these topics to make a more complicated program to make it more fun!(not confusing wise but more functions ect.))
#   Have fun while making a story that I myself would want to have the chance to do!
#   Use a number generator (im familiar with) to create a better game
#   Use my skills that I have newly learned on my own and implement them into something practical (splitting lists, functions, number generators and a few more!)
#   Try to make an enjoyable experience that you can keep trying and not have the exact same experience throughout
#
#            ~~~ Things to improve on (after I programmed this) ~~~
#   Become more knowledgeable on the many different tools in python + the many things I can import... Make use of it and try harder
#   Keep working on that program that I couldn't figure out how to stop the function and figure out how to make it work for future projects!
#
#         (I hope this is enough because most of my time was spent on bug fixing, and creating the code!) 
#         This probably took me around 6 hours of work! But that was because I was going into the unknown so I had to figure out how it worked
#           But I'm glad because of the hard work I can be eledgible for the bonus!
#
#
# Not too sure if you wanted me to explain every function but the names of the functions are mostly straight forward, but this first
# Function is just the beginner room, where the basics happen, presenting a problem, gives two options 
# then if they choose to fight its a 0.25 chance of winning, but also if they choose to run then they have options then from there the functions
# are quite self - explanatory!
def story1():
    print("You have fallen down into a deep crevasse, you look around and notice that you are in a cavernous room."
    "It is important that you get out immediately, impending doom is upon you! You have just 5 minutes.")
    Mon1 = str(input("There is a demon in front of you, are you going to fight, or run: "))
    if (Mon1 == "run"):
        Run1 = str(input("Now, run left, or right: "))
        if (Run1 == "left"):
            left()
        elif (Run1 == "right"):
            right()
    elif (Mon1 == "fight"):
        random_num = random.randint(1,2)
        rng1 = int(input("This is an RNG pick 1, or 2: "))
        if (rng1 == random_num):
            print("Congratulations, you have survived one attack from the beast!")
            random_num1 = random.randint(1,2)
            rng2 = int(input("This is now your second RNG! pick 1, or 2: "))
            if (rng2 == random_num1):
                print("Yay, you have survived the beast. You step over the beast, and walk forward into the room ahead of you!")
                front()
            else:
                deathwish()
        elif (rng1 != random_num) or (rng2 != random_num1):
            deathwish()
def left():
    left1 = str(input("So, you have decided to run, scaredy cat! Now, there is an unsuspecting trapdoor to the left of you, and there is a nice ladder headed to the seemingly clear surface! Where do you go, left, or up: "))
    if (left1 == "left"):
        print("Now, you have made it past two rooms! But don't consider yourselves lucky quite yet!")
        lefty()
    elif (left1 == "up"):
        random_num2 = random.randint(1,5)
        rng3 = int(input("You pop out into the middle of starving demons, you have to struggle! Another RNG! Choose a number between 1-5: "))
        if (random_num2 == rng3):
            print("Wow, you have managed to escape the demons, that was close!!")
            winners()
        elif (random_num2 != rng3):
            deathwish()
def lefty():
    left2 = str(input("There is a secret passage leading up stairs behind you, and an unsuspecting hall heading forward, do you want to go backward, or forward?: "))
    if (left2 == "backward") or (left2 == "back"):
        random_num3 = random.randint(1,2)
        if (random_num3 == 2):
            print("Haha, you dodged the loose step!")
            Run1 = str(input("A Giant demon is guarding the exit, will you choose to fight, or run?: "))
            if (Run1 == "run"):
                lefty()
            elif (Run1 == "fight"):
                random_num4 = random.randint(1,7)  
                Mon2 = int(input("You have one chance, to hit the weak spot! You have spotted the one string that will win the fight! (Pick a number 1-7): "))
                if (random_num4 == Mon2):
                    print("Success, you have beaten the Demon!")
                    winners()
                elif (random_num4 != Mon2):
                    print("You died! The Demon pounded you into a thin powder for his breakfast seasoning!")
                    deathwish()
        elif (random_num3 == 1):
            print("You slipped on a loose rock, and the stairs crumble! You fall down to never get up again! D:")
            deathwish()
    elif (left2 == "forward"):
        print("There is a man waiting for you at the end of the passageway, he explains to you that YOU are destined to become a "
        "demon hunter! But, he has to put you through a few tests first, and wants to ask you some important questions!")
        hunter()
# FINISH THE HUNTER CODE!!!
def hunter():
    hunt1 = str(input("Do you think you have the strength and integrity to become, THE DEMON HUNTER (yes or no): "))
    if (hunt1 == "no"):
        print("You are unworthy to retry! Banished!")
    elif (hunt1 == "yes"):
        hunt2 = str(input("All right, so you think you've got it in you huh? Well time to put you through the real test! Ready? "))
        if (hunt2 == "no"):
            print("Another unworthy one, BYE! You may not restart!")
        elif (hunt2 == "yes"):
            hunt3 = str(input("You have 30 seconds to beat this challenge or you too will get banished from the training to never attempt it again! Again, ready? "))
            ## MAYBE SOMETHING CAN CHANGE (ONCE AGAIN MY TIMER GAME COULDNT WORK(SEE END FOR EXPLANATION!))
            if (hunt3 == "no"):
                print("Just as expected! You are another weakling! BANISHED!!!!")
            elif (hunt3 == "yes"):
                print("Well, actually that was the challenge! If you had faith in yourself I feel that you are worthy!")
                print("You are trained for years upon end, you become the second best to ever do it (After the game creator)")
                winners()
                # ADD SOME CHALLENGE TYPE THING AND FIGURE OUT A SORT OF MINIGAME (Couldn't do this because the timer func would not quit no matter 
                # how hard I tried)
            else:
                winner = str(input("Now put in the secret passcode! "))
                if (winner == "tanjiro") or (winner == "Tanjiro") or (winner == "Nezuko") or (winner == "nezuko"):
                    print("You are a worthy one, I will take you under my wing, and train you to defeat every monster in this place!")
                    print("The only one who has ever done this! You might actually be able to become THE best demon slayer!")
                    winners()
                else:
                    print("How dare you try to trick the game creator! BANISHED!")
                    deathwish()
                    #Re program the different ones so that its an automatic win (with an epic boss at the end)
                    #This ended after I could not manage to get the timer function to stop D;
def front():
    print("In this room, you find a many desks, with blood splattered over them. There is a grate in the roof! Maybe there is a chance I can climb out, you think to yourself! You look further around the room, under a desk in the far corner there appears to be a hole leading to \"Nothing\"")
    runner1 = str(input("Are you going to attempt to climb out of the grate for an attempt to survive? (Yes or No) "))
    if (runner1 == "no") or (runner1 == "No"):
        print("That was definitely for the better, a demon was strolling above!")
        runner2 = str(input("Now, do you want to run or go forward into the hole? (run or forward): "))
        if (runner2 == "forward"):
            print("hahaha! you survived, a demon had just sniffed you out! One lucky duck you are!")
            front1()
        elif (runner2 == "run"):
            print("Wrong! A demon sniffed you out and bit you! You are now a demon, you jump out the grate and go on a brutal rampage!")
            deathwish()
    elif (runner1 == "yes") or (runner1 == "Yes"):
        attempt1 = str(input("Alright then, this is no easy feat are you sure you want to continue? "))
        if (attempt1 == "no") or (attempt1 == "No"):
            front()
        elif (attempt1 == "yes") or (attempt1 == "Yes"):
            random_num5 = random.randint(1,4)
            if (random_num5 == 1) or (random_num5 == 4) or (random_num5 == 3):
                print("You made it up the hole, but the game isn't done yet!")
                up1()
            else:
                print("You fell, bashed your head and a demon came to devour you up!")
                deathwish()            
# FINISH THE UP CODE! ~~ finished
def up1():
    print("You pop up into the middle of nowhere! What are you going to do!")
    run1 = str(input("Run! Do you want to go forward, left, or right: "))
    if (run1 == "right"):
        print("This is your typical story about a long life with your family, being all happy, good job!")
        winners()
    elif (run1 == "left"):
        print("Well, that's unfortunate! This was definitely the wrong path to choose! But good effort! You wandered directly into the demon cave!")
        deathwish()
    elif (run1 == "forward"):
        print("As you make your trek forward, a group of police find you and mistake you for the deadliest murderer, you can't testify and are sentenced to death!")
        deathwish()
    else:
        print("HAHA! You have cheated the game! An old man comes out of the crevasse, takes you under his wing and trains you to become a demon hunter!")
        print("If you got this path, I commend you as the creator! You are a worthy one!")
        # MAYBE RANDOMIZE THIS SO THAT WHATEVER WAY YOU PICK ITS RANDOM! (THIS idea is scratched!)
# TRY TO FIND A WAY TO MAKE THE DEMON HUNTER STORY BE A 100% win rate! ~~~ can't exactly
def front1():
    print("Ducking down into a oddly large hole in the ground you find a serrated sword.")
    sword1 = str(input("Do you pick up the sword in an attempt to combat the demons? "))
    if (sword1 == "no"):
        print("Ya should've picked it up, the demon sniffed you out!")
        deathwish()
    elif (sword1 == "yes"):
        print("You jump out of the hole and slash the demon, the demon disintegrates, it's as though the sword has powers that are unmatched! You look down at the sword! "
        "On the sword is printed \"Inosuke\" you realize that you saw this in your favourite anime.")
        leave1 = str(input("Do you want to leave through the grate with your new powers or stay here and combat demons? (leave, or stay): "))
        if (leave1 == "leave"):
            print("Good choice, the owner of the swords was on his way, and he doesn't seem all too happy!")
            up1()
        elif (leave1 == "stay"):
            print("Three people blast into the room you're standing in through the far right wall, they don't appear all that happy! "
            "Give Inosuke his sword back peacefully before we take it back!")
            leave2 = str(input("Do you want to give it back nicely? "))
            if (leave2 == "yes"):
                print("You give him his sword back, and they bring you back to the town!")
                winners()
            elif (leave2 == "no"):
                print("As nice as they are, Inosuke doesn't play around with his sword, and Tanjiro cuts off your neck!")
                deathwish()
def right():
    print("Dodging the demon, you make your way into a room that opens up. At the far side of the room there is a throne where a man in it."
    "Looking to the left is a stone wall, and to the right is a door")
    fighter1 = str(input("Do you want to fight the demon king? "))
    if(fighter1 == "yes"):
        print("Stupid human!")
        deathwish()
    elif (fighter1 == "no"):
        print("Good choice!")
        fighter2 = str(input("Do you want to go right? "))
        if(fighter2 == "yes"):
            print("Best choice you made all day!")
            print("You come out into a room! You look around. The room has scratches all over it. \"What a creepy place,\" you think to yourself")
            right2()
        elif (fighter2 == "no"):
            print("The demon king didn't like your prescence!")
            deathwish()
def right2():
    print("This room has 3 doorways, one leading left, one leading forward, one leading right!")
    looper = str(input("Which direction do you want to go!! (left, forward, right): "))
    loop()
def loop():
    lopp = ("In this room you find that it branches out into three more directions, right, left, and forward!,,, Woah! this room looks creepy, it branches out left, right, and forward!,,, The room is filled with blood, get out immediately, there are doorways going forward, left, and right!,,, Oh god, get out of here immediately! The roof looks like its crumbling! You can go left, right, or forward!!,,, There is a table, bed, and lamp, blood splattered on the whole thing! Get out! Go forward, right, or left!")
    lopp2 = lopp.split(",,, ")
    print(lopp2[random.randint(0,4)])
    looper2 = str(input("What direction do you want to go? (left, forward, or right!): "))
    variables = ("left, forward, right, forward, right, left, right, forward, left")
    variables2 = variables.split(", ")
    variables4 = random.randint(0,8)
    variables3 = (variables2[variables4])
    if (variables3 == looper2):
        forward()
    else:
        loop()
def forward():
    print("Well hello there!")
    whopper = str(input("What a weird looking room! There is a hole in the left corner and thats it! Do you want to inpect it or go back? (inspect or back): "))
    if (whopper == "back"):
        loop()
    elif(whopper == "inspect"):
        print("As you are inpecting this odd hole, three men blast through the wall!")
        print("\"Hi, are you stuck, we will help you get out,\" these people say. They are covered in funky looking clothing, nothing that you've ever seen before!")
        helper = str(input("They offer you help out of the crevasse! Are you going to take their help? "))
        if (helper == "no"):
            print("The men walk you back to the start!")
            story1()
        elif (helper == "yes"):
            print("All right, we are going!")
            winners()      
def deathwish():
    # EXPAND DEATH THINGS ~~ Finished
    deathwish1 = ("You're dead! haha!, What a time to die!, Oh noo! Did somebody die?, You died!, Uh oh! You died! D;, How does it feel to die?")
    deathwish2 = deathwish1.split(", ")
    print(deathwish2[random.randint(0,5)])
    death1 = str(input("Do you want to try again? (Play Again? Yes or No?) "))
    if (death1 == "Yes") or (death1 == "yes"):
        story1()
    elif (death1 == "No") or (death1 == "no"):
        print("Seems like someone is salty!")
def winners():
    winners1 = ("Yay! Congrats!, Good Job! You managed to live another day!, You just barely managed huh? Well Congrats! (You win), You? Out of all people won?, Really? You got out? Well good job I guess!")
    winners2 = winners1.split(", ")
    print(winners2[random.randint(0,4)])
    win1 = str(input("Do you want to try your luck again? (Play Again? Yes or No?) "))
    if (win1 == "Yes") or (win1 == "yes"):
        print("Back into the story you go!, try out a different path its lots of fun!")
        story1()
    elif (win1 == "No") or (win1 == "no"):
        print("Alright, see you again another time!")
def map():
    print(" ___________________________________________________________________ ")
    print(" |                                |         |                      | ")
    print(" |                  ?             |         |    ?                 | ")
    print(" |      ?                         |         |                      | ")
    print(" |                         ?      |         |              ?       | ")
    print(" |               ?                |         |_______               | ")
    print(" |__     _________________________|                |        ?      | ")
    print(" |  |   |                                          |               | ")
    print(" |  |   |                                          |               | ")
    print(" |  | ? |                  ____________________    |     ?         | ")
    print(" |  |   |                  |Hatch             |    |               | ")
    print(" |  |   |                  |       _______    |    |               | ")
    print(" |  |   |                  |       |Grate|    |    |               | ")
    print(" |  |   |     ___________  |       |_____|    |    |          ?    | ")
    print(" |  | ? |     |         |  |______    ________|    |    ?          | ")
    print(" |__|   |_____|RoofHatch|________|  |______________|               | ")
    print(" |        |                  |         |           |               | ")
    print(" |       Hatch             Door       Door      ?????????          | ")
    print(" |        |                  |         |           |               | ")
    print(" |___   __|__________________|Entrancee|_____?_____|_______________| ")
    print("    | E |                    |   You   |                             ")
    print("    | X |                    |   are   |     ?          ?            ")
    print("    | I |                    |   Here  |           ?     ?   ?       ")
    print("    | T |                    \   :D    /                             ")
    print("                              \  GL   /                              ")
    print("                               \     /              ?                ")
    print("                                \   /                                ")
    print("                                 \ /                                 ")

#
#
#                  Try to make a minigame where you have to type more of one thing ex "ones (1)" than the computer
#                           having a tic of 0.5 seconds in between the number outputs
#                                       ~~~VERY DIFFICULT~~~
#
#
#                       THESE ARE MY TIMER THINGS I WAS TESTING, I COULDNT FIGURE A WAY TO SHUT OFF THE TIMER SO I HAD TO ABANDON THIS IDEAD D:
#
def func1():
    fun1 = str(input("Heyyy how are you doing? "))
    fun2 = str(input("What are you doing? "))  
# I COULDNT FIND OUT HOW TO QUIT THIS FUNCTION FROM DOING ITS THINGS ~~ D;
def func2(): 
    s = 0
    while s<=15:
        time.sleep(1)
        print()
        s+=1
        if s==15:
            print("You have lost the game, go faster next time you weirdo!")   
def worker():   
    if __name__ == '__main__':
        Thread(target = func1).start()
        Thread(target = func2).start()

map()
story1()

