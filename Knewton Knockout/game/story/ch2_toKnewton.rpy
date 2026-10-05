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
return