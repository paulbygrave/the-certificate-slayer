import sys, time

# Define the scrolltext functions
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_quick(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def intro_text():
    print_slow("\n\n\nA long, long time ago..." + "\n\n" +
    "..." + "\n\n")
    print_quick("(OK, on Monday 7th October at around 2 o'clock in the afternoon.)" + "\n\n")
    print_slow("..." + "\n\n" +
    "In a galaxy far, far away..." + "\n\n" +
    "..." + "\n\n")
    print_quick("(OK, in the Contino Liverpool Street office, meeting room 3.)" + "\n\n")
    print_slow("..." + "\n\n")
    print_quick("A brave and noble warrior (yeah, who am i kidding?!)...made a promise to the PeopleOps team.\n" +
    "That promise? That he would produce (in Python) a story of noble deeds.\n" + 
    "A story foretelling one hero's struggle against the combined forces of the mighty Cloud Certifications.\n\n")
    print_slow("..." + "\n\n" + "..." + "\n\n" +
    "This is that hero's story....\n\n" + "..." + "\n\n" + "..." + "\n\n")
    time.sleep(2)

def fillspace():
    print_slow("..." + "\n\n" + "..." + "\n\n" + "..." + "\n\n")

def quest_text():
    print_slow("\n\nOur hero is new to Contino.\n" +
    "...\n" + 
    "They have completed the onboarding, setup their new equipment and has decided to Upskill!\n" +
    "...\n" + 
    "They start to look for something to study...\n" +
    "...\n" + 
    "Oh no! It's an ambush!\n")

    time.sleep(1)
