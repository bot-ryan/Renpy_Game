# game/story/ch1_intro.rpy

label ch1_intro:

    stop music fadeout 2.0
    play music "a_good_day.ogg"  fadein 2.0
    scene bg room 
    show nana cake:
        yalign 0.1
        xalign 0.5
    
    with Fade(1, 1, 1)

    nana "Welcome to the game!"

    nana "I'm Nana, and I'll be your guide throughout your journey."

    return