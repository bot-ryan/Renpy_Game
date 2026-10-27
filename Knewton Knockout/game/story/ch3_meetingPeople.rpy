# game/story/ch3_meetingPeople.rpy

default talked_allenna = False
default talked_celeste = False

# =========================================================
# 1. CLICKABLE SCREEN FOR THIS SCENE
# =========================================================
screen ch3_interact():
    imagebutton:
        idle "images/characters/student/allenna/allenna_default.png"
        hover Transform("images/characters/student/allenna/allenna_default.png", matrixcolor=BrightnessMatrix(0.15))
        at Transform(zoom=1.5) # <--- Apply zoom to the button itself!
        xalign 0.25
        yalign 1.0
        focus_mask True
        action Return("allenna")

    
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

    show allenna_default with dissolve:
        zoom 1.5
        xalign 0.25
        yalign 1.0

    show celeste_default with dissolve:
        xalign 0.75
        yalign 1.0

    pause 0.5

    "You reach the school's courtyard, where you see two students standing nearby. They seem friendly and approachable."
    "You should probably talk to them to get to know them better. You can click on either of them to start a conversation."
    "Talk to both of them before going to class! You're forced to do this, cause it's part of the main quest..."
    "Press (Q) or navigate to the menu to check your quest log if you forget what to do next."

    if player_gender == "M":
        "I know you're a dude... but don't be an introvert! Just go talk to them!"
    else:
        "Don't be shy! They're girls, so just go talk to them! #girlpower"

    $ quest_mgr.start("main_courtyard") # start the first main quest

    # --- EXPLORATION LOOP ---
    label .explore_loop:

        # Check if both girls have been talked to
        if talked_allenna and talked_celeste:
            "You've talked to both students! You can now proceed to class."
            
            # Complete Step 3 (Head inside to class) and finish the main quest!
            $ quest_mgr.advance("main_courtyard")
            
            #return # or jump to next chapter label

        scene courtyard2 day

        # Show screen and wait for player to click a character
        call screen ch3_interact

        # --- TALK TO ALLENNA ---
        if _return == "allenna":
            scene courtyard2 day
            show allenna_default with dissolve:
                zoom 2
                xalign 0.5
                yalign 1.0

            if talked_allenna:
                $ speak_random("allenna")
            else:
                $ talked_allenna = True
                # Complete Step 1 specifically (index 0)
                $ quest_mgr.complete_step("main_courtyard", 0)
                allenna "Hey there! You must be new here. I'm Allenna, nice to meet you!"
                allenna "During the term break, I went to a magic show in Mexico."
                allenna "The magician told us that he would disappear on a count of 3."
                allenna "He counted... 'uno... dos...'"
                allenna "Then he disappeared, without a tres!"
                

                menu AllennaChoice01:
                    allenna "Get it? Hahaha!" 

                    "Laugh at her joke":
                        $ Allenna_friendship += 0.1
                        $ notify_event("Allenna appreciates you.", icon="images/ui/icons/relationship_positive.png")
                        allenna "Finally, someone who appreciates fine comedy!"

                    "Poker face":
                        $ Allenna_friendship -= 0.1
                        $ notify_event("Allenna feels offended.", icon="images/ui/icons/relationship_negative.png", sfx="audio/sfx/peppa-pig-fail.wav")
                        allenna "Hey! Don't judge my humor!"


            jump .explore_loop

        # --- TALK TO CELESTE ---
        elif _return == "celeste":
            scene courtyard2 day
            show celeste_default with dissolve:
                zoom 1.3
                xalign 0.5
                yalign 1.0

            if talked_celeste:
                $ speak_random("celeste")
            else:
                $ talked_celeste = True
                # Complete Step 2 specifically (index 1)
                $ quest_mgr.complete_step("main_courtyard", 1)
                celeste "you talked to me"

            jump .explore_loop

    return