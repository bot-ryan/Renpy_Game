# game/story/ch1_intro.rpy

label ch1_intro:

    stop music fadeout 2.0
    play music "a_good_day.ogg" fadein 2.0
    scene mc_bedroom_morning
    show sibling cake:
        yalign 0.1
        xalign 0.5
    
    with Fade(1.0, 1.0, 1.0)

    sibling "Happy birthday, {b}[player_name()]{/b}! Today is a very special day for you!"

    menu changenameorgender:
        sibling "Are you excited to start your first day at Knewton Academy?"

        "Yes! I can't wait to start my first day at Knewton Academy!":
            show sibling happy with dissolve
            sibling "That's the spirit! Let's get going!"

        "My name isn't {b}[player_name()]{/b}...":
            show sibling surprised with dissolve
            sibling "Oh no! I'm so sorry! What should I call you then?"

            # 1. Grab current active name for the text box default
            $ current_name = player_name()
            $ new_name = renpy.input("What is your real name?", default=current_name).strip()

            # 2. Fallback if the user leaves the text box blank
            if not new_name:
                $ new_name = current_name

            # 3. Save to the actual target variable based on gender
            if player_gender == "M":
                $ brother_name = new_name
            else:
                $ sister_name = new_name

            show sibling happy with dissolve
            sibling "Got it! Let's try that again!"
            show sibling cake:
                yalign 0.1
                xalign 0.5
            sibling "Happy birthday, {b}[player_name()]{/b}!"

            jump changenameorgender

        "(switch to Nana)":
            pass

    return