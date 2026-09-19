# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image bg falling_stars = Movie(play="images/backgrounds/animated/falling_stars.webm", loop=True)

# The game starts here.

label start:

    stop music fadeout 2.0
    play music "zen.ogg"  fadein 2.0
    scene knewton
    scene bg falling_stars
    with Fade(1.0, 0.5, 2.0)

    #wait 1 seconds
    pause 0.5

    "Who.... am I?"
    "What... am I doing here? What is my purpose? Why am I here?"
    pause 1.0
    "Hmm... I feel like I've been here before."
    "I feel like I've been here for a long time."
    pause 0.5
    "A... very long time..."
    pause 1.0
    "I... I feel like I have a purpose here."
    "For the longest time, I've always had a feeling that I would become a..."


    #jump to intro chapter
    jump ch1_intro

    return
