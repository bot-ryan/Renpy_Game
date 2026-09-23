# game/test_character.rpy

label test_character:
    scene bg room with dissolve

    # 1. Test auto-registered character name & 'default' sprite
    show nana default with dissolve:
        yoffset 100
        xalign 0.5

    nana "Hey! If you can see my sprite and read my name tag, the CharacterSheet setup worked!"

    # 2. Test sprite switching ('cake' variant)
    show nana cake with dissolve:
        yalign 0.1
        xalign 0.5
    nana "Look, I brought a cake!"

    # 3. Test random dialogue loop
    nana "Click the button below to test pulling lines randomly from my character sheet."

    menu random_test_menu:
        "Talk to Nana (Random Line)":
            $ speak_random("nana")
            jump random_test_menu

        "Done testing":
            nana "Awesome! Everything is working cleanly."

    # Return back to wherever you called/jumped from
    jump ch1_intro