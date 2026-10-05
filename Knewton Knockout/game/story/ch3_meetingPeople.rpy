# game/story/ch3_meetingPeople.rpy

# =========================================================
# 1. CLICKABLE SCREEN FOR THIS SCENE
# =========================================================
screen ch3_interact():

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


    # --- EXPLORATION LOOP ---
    label .explore_loop:

        stop music fadeout 2.0
        #play music "chill_music01.ogg" fadein 2.0
        scene courtyard2 day with dissolve
        with Fade(1.0, 2.0, 1.0)
        pause 1.0

        # Pauses gameplay until the player clicks Allenna or Celeste
        call screen ch3_interact

        # --- TALK TO ALLENNA ---
        if _return == "allenna":
            scene courtyard2 day
            show allenna default with dissolve
            
            allenna "Hey! Nice to meet you!"
            # $ speak_random("allenna") # <--- Optional: Use your random dialogue pool!

            jump .explore_loop

        # --- TALK TO CELESTE ---
        elif _return == "celeste":
            scene courtyard2 day
            show celeste default with dissolve

            celeste "Oh hi there! Are you excited for class?"
            # $ speak_random("celeste") # <--- Optional: Use your random dialogue pool!

            jump .explore_loop

    return