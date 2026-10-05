# game/story/ch2_toKnewton.rpy

label ch2_toKnewton:

    stop music fadeout 2.0
    play music "chill_music01.ogg" fadein 2.0
    scene neighborhood 1 day
    with Fade(1.0, 2.0, 1.0)
    
    pause 1.0

    "Today seems like a normal day. The sun is up yet the air is still and calm."
    "Knewton Academy is just a few minutes away, so [player_name()] and [sibling_name()] would just walk there..."
    "unless it rains! In which case, their parents would drive them to school instead."
    "The route to Knewton Academy is pretty straightforward. First, they would walk across the neighborhood..."

    scene neighborhood 2 day with dissolve

    "make a turn to the left... as that's the only turn they could make."

    scene neighborhood 3 day with dissolve

    "After a few minutes, they would reach a T-junction. Here, they would have to make a {b}right{/b} turn."

    scene playground 3 day with dissolve

    "Then, they would pass by the playground. [player_name()] would play football with [p.his] friends here, every single day!"
    if likes_sports:
        "Since [player_name()] is naturally athletic, [p.he] would always be the top player in the neighborhood."
        "[p.His] stamina and agility would allow [p.him] to make the most impressive moves on the field."
    elif likes_games:
        "Since [player_name()] is a gamer, [p.he] would get too ambitious and make unrealistic moves such as trying to score a goal from the other side of the field."
        "It never worked, but [p.he] would always try to do it anyway."
        "[p.His] friends wouldn't mind, as long as [p.he] was willing to retrieve the ball."
    elif likes_science:
        "Since [player_name()] is a science nerd, [p.he] is somehow able to calculate the trajectory of the ball and make a perfect pass every time..."
        "assuming that [p.he] doesn't have to put in much power, as [p.he] is not very athletic."
    elif likes_art:
        "However, [player_name()] would often get distracted by the beautiful scenery around the playground, and would often forget that [p.he] was supposed to be playing football."
        "Fortunately, [p.his] friends found it hilarious."
    else:
        "[player_name()] is neither good nor bad at sports."
        "So naturally, [p.he] would blend in with his friends, but [p.he] never stood out amongst them either."

    scene gate day with dissolve

    "Finally, they would reach the gate to Knewton Academy."

    menu freehint:
        "Psst... [player_name()]! Would you like a hint?"

        "Okay...?":
            "I'm not supposed to give out hints like this but..."
            "make sure you remember the route to school! [sibling_name()] might not be around to help you if you forget!"
            "Also, choices matter in this game! So make sure you choose wisely!"
            "Finally, make sure you pay attention to the quests and storyline. You might miss something important if you don't!"
            "This game has multiple endings, so make sure you don't regret your choices!"
            "Regardless, you can always replay the game to see what you missed!"

        "No thanks!":
            "Are you sure? You might regret it later if you don't take the hint!"

    "Anyway, have fun!"
    
    jump ch3_meetingPeople     
return