# game/story/ch1_intro.rpy

label ch1_intro:

    stop music fadeout 2.0
    play music "a_good_day.ogg"  fadein 2.0
    scene mc_bedroom_morning
    show nana cake:
        yalign 0.1
        xalign 0.5
    
    with Fade(1, 1, 1)

    nana "Happy birthday, {b}[sibling_name()]{/b}! Today is a very special day for you!"

    menu changenameorgender:
        nana "Are you excited to start your first day at Knewton Academy?"

        "Yes! I can't wait to start my first day at Knewton Academy!":
            pass
        
        "My name isn't {b}[sibling_name()]{/b}...":
            # Scenario 2: Dynamic Name Input
            show nana surprised with dissolve
            nana "Oh no! I'm so sorry! What should I call you then?"

            # Open a text box for the player to type their actual name
            $ player_name = renpy.input("What is your real name?", default="Jake").strip()

            # Fallback if the player enters nothing
            if not player_name:
                $ player_name = "Jake"

            show nana happy with dissolve
            nana "Got it! Happy birthday, {b}[sibling_name()]{/b}! Let's try that again!"

            jump changenameorgender
            

        "(switch to Nana)":
            pass

    return