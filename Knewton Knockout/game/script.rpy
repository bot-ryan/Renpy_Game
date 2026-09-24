# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg void = Movie(play="images/backgrounds/animated/the_void.webm", loop=True)

# The game starts here.

label start:

    #jump ch1_intro

    stop music fadeout 2.0
    play music "zen.ogg"  fadein 2.0
    scene knewton
    scene bg void
    with Fade(1.0, 0.5, 2.0)

    #wait 1 seconds
    pause 0.5
    """
    Who.... am I?

    What... am I doing here? Why am I here in the first place?
    """
    pause 1.0
    """
    Hmm... I feel like I've been here before.

    For a long time...
    """
    pause 0.5
    "a... very long time..."
    pause 1.0
    "I... I feel like I have a purpose here."
   
    menu:
        "For the longest time, I've always had a feeling that I would become a..."

        "world-renowned scientist":
            $ likes_science = True
            "...so I could save lives and make the world a better place."
           
        "generational artist":
            $ likes_art = True
            "...one artwork could sell for millions!"
            
        "professional gamer":
            $ likes_games = True
            "...If I make it big, I can just stay home and play games all day!"

        "world-class athlete":
            $ likes_sports = True
            "...I always wanted to share a stage with the best athletes in the world!"

        "... (I don't know)":
            "...I don't know what I want to do with my life. But maybe I will figure that out here... or later."


    "Ah, I'm getting lost in my own world, again. I should probably focus on the task at hand."
   

    "???" "Wake up, {b}[sibling_name()]{/b}! It's your first day at Knewton Academy! You should probably get up and get ready for your first class!"

    "{b}[sibling_name()]{/b}" "Wait... my name is {b}[sibling_name()]{/b}?!"

    #jump to intro chapter
    jump ch1_intro

  
    return
