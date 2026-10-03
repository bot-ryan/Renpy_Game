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

            # 1. Build the summary text message
            $ summary_msg = (
                f"CHARACTER SUMMARY:\n"
                f"• Your Name: {player_name()}\n"
                f"• Gender: {player_gender}\n"
                f"WARNING: Once you proceed, these choices CANNOT be changed again.\n\n"
                f"Are you sure you want to continue?"
            )

            # 2. Open the built-in Ren'Py GUI popup box
            if renpy.confirm(summary_msg):
                # Player pressed 'Yes' / Confirmed
                sibling "Great! Off to school we go!"
                jump ch2_toKnewton
            else:
                # Player pressed 'No' / Wants to edit
                jump changenameorgender

        "My name isn't {b}[player_name()]{/b}...":
            show sibling surprised with dissolve
            sibling "Oh no! I'm so sorry! What should I call you then?"

            # 1. Grab current active name for the text box default
            $ current_name = player_name()
            # Restrict maximum input length to 12 characters
            $ new_name = renpy.input("What is your real name?", default=current_name, length=12).strip()

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

        "(Switch to [sibling_name()])":
            # 1. Flip gender state
            if player_gender == "M":
                $ player_gender = "F"
            else:
                $ player_gender = "M"

            # 2. React to the change (ConditionSwitch updates the sprite automatically!)
            show sibling surprised with dissolve
            sibling "Oh, my mistake! So you're {b}[player_name()]{/b}, and I'm {b}[sibling_name()]{/b}!"

            show sibling cake:
                yalign 0.1
                xalign 0.5
            
            # 3. Loop back to re-confirm or allow further tweaks
            jump changenameorgender

    return