print("importing rng...")
import random
print("Welcome to","Leave your Punctuation at the Door.","By JF")
a=input("State your name.")
print("Hello,",a,)
b=input("What's your business here??")
laugh=("ha")
Laugh=("Ha")
yes=1
no=0
magic_wand=0
print("That doesn't sound like a good reason to be here at all,",a+"!","What're you really here for!?")
input()
print("Right, right. Suure. You're lucky I don't actually work here. Had you going for a minute.", Laugh+laugh+".")
"""print("-----------------------------------")
print("Variable a is:", type(a))
print("Variable b is:", type(b))
print("Variable laugh is:", type(laugh))
print("Variable Laugh is:", type(Laugh))"""
magic_wand=int(input("Retaliate? 0/1: "))
if magic_wand==1:
    wep_selection=int(input("Draw from your inventory || 1:Desert Eagle  2:M1928 pattern Tommy  3:Corrosive acid  :4==Nuke  ||"))
    shots=str("notyet")
    if wep_selection==1:
        shots=int(input("How many caps do you let loose on his punk ass? "))
        if 6<=shots:
            print("Aah! What the hell!")
            print("The shahdiberman crawls swiftly away into the alley...")
            print("The shahdiberman is gone.")
        if 6>shots:
            if not 0==shots:
                print("Oh crud!! ")
                print("The shahdibaerman runs away...")
                print("The shahdiberman is gone.")
    if 0==shots:    
        print("That's a cool gadget! I've gotta hit the road anyway. Excuse my joking.. haha!")
        print("The shahdiberman is gone.")
    if wep_selection==2:
        shots=int(input("Choose a burst length... (00-32) "))
        if 30<=shots:
            print("The shadhibaerman is riddled with countless spells, spraying much beer on the wall behind him.")
            print("The shahdiberman slumps to the ground...")
            print("The shahdiberman is gone.")
        if 20>=shots:
            if not 0==shots and not 10>=shots:
                print("Oh crud!! ")
                print("The shahdibaerman gains many new holes and stumbles before falling to the earth...")
                print("The shahdiberman is gone.")
        if 10>=shots:
            if not 0==shots and not 5>=shots:
                print("The shahdibaerman is hit several times...")
                print("The shadhibaerman runs as quickly as his muscles allow...")
                print("The shahdiberman is gone.")
        if 5>=shots:
            if not 0==shots:
                print("Ow! Ow ow ow!")
                print("The shadhibaerman runs...")
                print("The shahdiberman is gone.")
        if 0==shots:    
            print("That's a cool gadget! I've gotta hit the road anyway. Excuse my joking.. haha!")
            print("The shahdiberman is gone.")
    if wep_selection==3:
        shots=(int(input("Choose power... (0-3)")))
        if shots==0:
            print("You just stand there, staring at the shadhibaerman and making small noises in the back of your throat.")
            print("Are you.. trying to cast a silent spell or something? I'll have you know, this is a no-magic zone and the guards won't take kindly to it.")
            print("I've to leave anyway. Good day!")
            print("The shadhibaerman walks away...")
            print("The shadhibaerman is gone.")
        if shots==1:
            print("You spit a small amout of bile into the shadhibaerman's eyes.")
            print("Aargh, my eyes!! Why!?")
            print("The shadhibaerman walks away in a huff...")
            print("The shahdibaerman is gone.")
        if shots==2:
            print("You throw up on your own shirt.")
            print("Haha. It seems you've had too much to drink *already*! I like your style; hahahaha! Don't get any on the bar!")
            print("The shahdibaerman walks away, satisfied with his social interaction...")
            print("The shadhibaerman is gone.")
        if shots==3:
            print("You projectile vomit all over the shadhibaerman, leaving a near-perfect (albeit slowly changing in shape) outline of him on the wall and ruining his day as well as his clothes.")
            print("Hahahahahaha! Amazing! I've never seen so much vomit in all my days! Not since we gave The Gray Dragon bad whiskey for brunch. Feel better, man!")
            print("The shadhibaerman walks away soaking wet...")
            print("The shadhibaerman is gone.")
    if wep_selection==4:
        shots=int(input("Are you sure? (0/1)"))
        if shots==0:
            print("You fart loudly.")
            print("Wow.")
            print("The shadhibaerman walks away...")
            print("The shadhibaerman is gone.")
        if not shots==0:
            print("You shit yourself.")
            print("The shadhibaerman is silent and walks away, disgusted...")
            print("The shadhibaerman is gone.")
if magic_wand==0:
    print("Well, I've gotta hit the road anyway. Good day!")
    print("The shahdiberman is gone.")
cont=int(input("Continue into the bar? (0/1):"))
if cont==1:
    print("You swing the doors open and step inside...")
if cont==0:
    print("Where do you go? || 1==  || 2==  || 3==  || 4==  || 5==  ||")
print("To be continued.................")
if wep_selection==1 and shots>0:
    print("It's a tavern, like any other in this region. Lots of wood, some glass, a couple stairwells on your right & left, and of course a shallow, sturdy bar along the entire far wall.")
    walkpast=int(input("Walk past the 16 5-seat tables of patrons to || 5:The left stairwell  6:The Bar  7:A Table  8:The right stairwell ||"))
    print("The")
    print("Everyone inside looks towards the entrance expectantly to see who just shot at Jerry")
npc_opinn=random.randint(0,32)
if npc_opinn<15:
    print("No one says anything. Everyone stares for a second and goes back to their drinks.")
if npc_opinn>15:
    print("Baerkeep: So that's who's paying for the wall...")
    print("Patron:",laugh)
    print("")