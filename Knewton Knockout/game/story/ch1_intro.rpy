# game/story/ch1_intro.rpy

define nana = Character("Nana") #Hannah's character welcoming the player to the game

label ch1_intro:

    scene bg room with fade

    show nana:
        yoffset 50
        xalign 0.5

    nana "Welcome to the game!"

    nana "I'm Nana, and I'll be your guide throughout your journey."

    return