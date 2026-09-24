# game/CharacterSheet.rpy

init python:
    # 1. Base relative paths (relative to the game/ folder)
    adult_path = "images/characters/adult"
    student_path = "images/characters/student"

    # 2. Master character database
    CHARACTER_DATA = {
        "nana": {
            "name": "Nana",
            "gender": "Female",
            "color": "#ff9999",
            "images": {
                "cake": f"{student_path}/nana/nana_cake.png",
                "default": f"{student_path}/nana/nana_default.png",
            },
            "random_dialogues": [
                "Hello there! I'm Nana, your friendly guide.",
                "I hope you're ready for an exciting adventure!",
                "Let's explore the world together!",
            ]
        },

        "aiko": {
            "name": "Aiko",
            "gender": "Female",
            "color": "#d94747",
            "images": {
                "default": f"{student_path}/aiko/aiko_default.png",
            },
            "random_dialogues": [
                "I'm Aikokokokoko"
            ]
        }

    }

    # 3. Boot registration loop
    for char_id, data in CHARACTER_DATA.items():
        # Automatically creates character variables (e.g., define nana = Character(...))
        char_obj = Character(data["name"], color=data.get("color", "#ffffff"), image=char_id)
        setattr(store, char_id, char_obj)

        # Automatically registers images (e.g., image nana cake = "...")
        for emotion, path in data.get("images", {}).items():
            renpy.image((char_id, emotion), path)

    # Helper function to speak a random line from the character's list
    def speak_random(char_id):
        if char_id in CHARACTER_DATA and CHARACTER_DATA[char_id].get("random_dialogues"):
            lines = CHARACTER_DATA[char_id]["random_dialogues"]
            chosen_line = renpy.random.choice(lines)
            char_obj = getattr(store, char_id)
            renpy.say(char_obj, chosen_line)