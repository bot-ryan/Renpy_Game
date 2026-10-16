# game/story/ch3_meetingPeople.rpy

default talked_allena = False
default talked_celeste = False

# =========================================================
# 1. CLICKABLE SCREEN FOR THIS SCENE
# =========================================================
screen ch3_interact():

    if talked_allena and talked_celeste:
        "You've talked to both students! You can now proceed to class."
        return
    # Allenna (Left side)
    imagebutton:
        idle "images/characters/student/allenna/allenna_default.png"
        hover Transform("images/characters/student/allenna/allenna_default.png", matrixcolor=BrightnessMatrix(0.15))
        xalign 0.25
        yalign 1.0
        focus_mask True
        action Return("allenna")

    # Celeste (Right side)
    imagebutton:
        idle "images/characters/student/celeste/celeste_default.png"
        hover Transform("images/characters/student/celeste/celeste_default.png", matrixcolor=BrightnessMatrix(0.15))
        xalign 0.75
        yalign 1.0
        focus_mask True
        action Return("celeste")


# =========================================================
# 2. CHAPTER STORY FLOW
# =========================================================
label ch3_meetingPeople:

    stop music fadeout 2.0
    #play music "chill_music01.ogg" fadein 2.0
    scene courtyard2 day
    with Fade(1.0, 1.0, 1.0)
    

    show allenna_default:
        xalign 0.25
        yalign 1.0

    show celeste_default:
        xalign 0.75
        yalign 1.0

    pause 1.0

    "You reach the school's courtyard, where you see two students standing nearby. They seem friendly and approachable."
    $ quest_mgr.start("main_courtyard") #start the first main quest
    "You should probably talk to them to get to know them better. You can click on either of them to start a conversation."
    "Talk to both of them before going to class! You're forced to do this, cause it's part of the main quest..."
    "Press (Q) or navigate to the menu to check your quest log if you forget what to do next."
        
        #If male player, then say dont be introvert, if girl player, then say dont be shy they're girls!
    if player_gender == "M":
        "I know you're a dude... but don't be an introvert! Just go talk to them!"
    else:
        "Don't be shy! They're girls, so just go talk to them! #girlpower"

    # Pauses gameplay until the player clicks Allenna or Celeste
    call screen ch3_interact

    "After dialogue interact"
    
    
    # --- EXPLORATION LOOP ---
    label .explore_loop:

        scene courtyard2 day

        # --- TALK TO ALLENNA ---
        if _return == "allenna":
            scene courtyard2 day
            show allenna default with dissolve

            $ talked_allena = True
            # Complete Step 1 specifically (index 0)
            $ quest_mgr.complete_step("main_courtyard", 0)

            allenna "Hey! Nice to meet you!"
            # $ speak_random("allenna") # <--- Optional: Use your random dialogue pool!

            jump .explore_loop

        # --- TALK TO CELESTE ---
        elif _return == "celeste":
            scene courtyard2 day
            show celeste default with dissolve

            $ talked_celeste = True
            # Complete Step 2 specifically (index 1)
            $ quest_mgr.complete_step("main_courtyard", 1)

            celeste "Oh hi there! Are you excited for class?"
            # $ speak_random("celeste") # <--- Optional: Use your random dialogue pool!

            jump .explore_loop

    return