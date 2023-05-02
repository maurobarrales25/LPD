print("importing rng...")
import random
print("Loading story...")
print("pre-assigning value to variables...")
print("Welcome to","Leave your Punctuation at the Door.","By JF")
a=input("State your name.")
print("Hello,",a,)
b=input("What's your business here??")
laugh=("ha")
Laugh=("Ha")
yes=1
no=0
magic_wand=0
wep_selection=0
shots=0
fake_it=0
question=0
"""
If name==str():
    do something
"""
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
            if 32<shots:
                print("Your weapon is empty")
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
            print("You projectile vomit all over the shadhibaerman, leaving a near-perfect (albeit slowly changing in shape) outline of him on the wall and absolutely ruining his clothes.")
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
    print("It's a tavern, like any other in this region. Lots of wood, some glass, a couple stairwells on your right & left, and of course a shallow, sturdy bar along the entire far wall.")
#    walkpast=int(input("Walk past the 16 5-seat tables of patrons to || 5:The left stairwell  6:The Bar  7:A Table  8:The right stairwell ||"))
    if wep_selection==1 or wep_selection==2 and shots>0:
        print("Everyone inside looks towards the entrance expectantly to see who just shot at Jerry")
npc_opinn=random.randint(0,32)
if npc_opinn<15:
    print("No one says anything. Everyone stares for a second and goes back to their drinks.")
if npc_opinn>15:
    if wep_selection==1 and shots==3:
        print("Everyone inside looks towards the entrance expectantly to see who just shot at Jerry")
        print("Baerkeep: So that's who's paying for the wall...")
        print("Patron:",laugh)
        print("Welcome, stranger!")
if cont==0:
    where_next=int(input("You walk || 1. Nowhere  2.   3.   4.   5. Out of town :"))
    if where_next==1:
        print("You stand outside the bar.")
        input("Think to yourself: ")
        print("A minute passes...")
        input("Think to yourself: ")
        print("A traveler walks up to the front of the bar.")
        fake_it=int(input("Act like a bouncer? (00/01): "))
        if fake_it==1:
                print("You cross your arms and try to look tough.")
                ques=input("Ask the traveler... 1. Their name  2. Their business  3. Who they think they are walking up to YOUR bar without cash in their hand ||: ")
                if ques==1:
                    print("Traveler: John")
                if ques==2:
                    print("Traveler: I'm here to play poker.")
                if ques==3:
                    print("Traveler: Oh, is there an entry fee today? Here you go.")
                    print("The traveler hands you 2 pieces of silver...")
        if fake_it==0:
            print("The traveler walks by you into the bar.")

    if where_next==5:
        print("You walk down the street, towards the sign that says 'Now leaving Shady Hotel's town'. The dirt road crunches and groans under your steps, getting ever closer to the edge...")
        print("Once the town is but a thumb's height on the horizon, you reach a fork in the road. It reads 'where to?'")
        where_next=int(input("Where to?... 1. Left  2. Center left  3. Center right  4. Right right"))
        if where_next==3:
            print("You take the center-right path. Walking along, you notice another forrest up ahead. Dense.")
            print("A lone person is standing by the edge of the road, unmoving under the shade of a tree.")
            talk=int(input("Stop to talk to the stranger? (01/00)"))
            if talk==0:
                print("You pass by silently.")
            if talk==1:
                print("Stranger: Hello! How're you on this fine cloudy day, traveler?")
                input()
                print("I see. Well, regardless I should warn thee not to name the forrest thy see. All who name it have met their end inside those trees...")
            print("you keep walking down the path, through plenty  of tall and sturdy trees. These seem to've been here for ages.")
            print("Looking up into the branches, a gremlin meets your gaze.")
            print("The gremlin hisses")
            print("Gremlin: What business might you have in MY forrest, traveller...")
            input("Input: ")
            print("Hahahahaha. Riiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiight, hahe. Thine should be on your way before sundown, or I'll make you name the forrest!")
            print("More gremlins hiss in the trees: Paint the forrest!!!")
            leave=int(input("Leave on your way? (00/01) )"))
            if leave==1:
                print("You continue down the path, walking towards an opening in the trees barely noticable among the dark net of leaves and branches that seem so safe and yet so trapping...")
            print("You come out the other end of the forrest, and see a large city with a grand castle inset just a couple hundred meters behind the messy rows of wodden buildings and thatched rooves.")
            print("There is a permanent-looking bridge over the moat. Cross?")
            input("00/01: ")
            print("The bridge creaks under your feet as you cross it, the whole structure's solid enough even despite the slight wobble. This thing has been here a while.")
            print("You reach a guard gate.")
            print("Guard: Who are you?")
            input("Input: ")
            print("Guard: Okay. Take this and be on your way.")
            print("The guard hands you a sheet of paper.")
            print("The sheet of paper seems to be a flyer, advertising a circus act near the castle, just to the left of the main gate.")
            print("")
            if leave==0:
                print("You stay static, staring at the creature...")
                print("1= Say something || 2= Do karate || 3. Laugh at the gremlin for living in trees like some sort of bird")