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
                "Hihi",
                "Ugh, when's there gonna be a new quest..!"
            ]
        },

        "jake": {
            "name": "Shakey",
            "gender": "Male",
            "color": "#9999ff",
            "images": {
                "cake": f"{student_path}/jake/jake_cake.png",
                "default": f"{student_path}/jake/jake_default.png",
            },  
            "random_dialogues": [
                "Wanna play a game of pickup?",
                "Let me think... (he forgot what to say)"
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
        },

        "allenna": {
            "name": "Allenna",
            "gender": "Female",
            "color": "#d94747",
            "images": {
                "default": f"{student_path}/allena/allenna_default.png",
                "happy" : f"{student_path}/allena/allenna_happy.png",
                "think" : f"{student_path}/allena/allenna_think.png",
                "shocked" : f"{student_path}/allena/allenna_shocked.png",
                "angry" : f"{student_path}/allena/allenna_angry.png",
            },
            "random_dialogues": [
                "holeh moleh.",
                "UHH i think it's a carrot..",
                "OH LOWRD HAGE MERCY",
                "i like apples and bananas :9 "
            ]
        },

        "celeste": {
            "name": "Celeste",
            "gender": "Female",
            "color": "#d94747",
            "images": {
                "default": f"{student_path}/celeste/celeste_default.png",
                "happy" : f"{student_path}/celeste/celeste_happy.png",
                "think" : f"{student_path}/celeste/celeste_think.png",
                "shocked" : f"{student_path}/celeste/celeste_shocked.png",
                "angry" : f"{student_path}/celeste/celeste_angry.png",
            },
            "random_dialogues": [
                "random"
                "random2"
                "random3"
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

    #4 Player pronouns
    class PronounSet:
        def __init__(self, is_player=True):
            self.is_player = is_player

        def _is_male(self):
            # Player is male if gender == "M", sibling is male if gender == "F"
            if self.is_player:
                return store.player_gender == "M"
            return store.player_gender == "F"

        # Subject (he / she)
        @property
        def he(self):
            return "he" if self._is_male() else "she"

        @property
        def He(self):
            return self.he.capitalize()

        # Object (him / her)
        @property
        def him(self):
            return "him" if self._is_male() else "her"

        @property
        def Him(self):
            return self.him.capitalize()

        # Possessive (his / her)
        @property
        def his(self):
            return "his" if self._is_male() else "her"

        @property
        def His(self):
            return self.his.capitalize()

# =========================================================
# REN'PY STATEMENTS (MUST BE OUTSIDE THE init python BLOCK)
# =========================================================

# 1. Generic Character speaker that uses sibling_name()
define sibling = Character("[sibling_name()]", image="sibling")

# Dynamic image tags linked to player_gender
image sibling happy = ConditionSwitch(
    "player_gender == 'F'", "images/characters/student/jake/jake_happy.png",
    "True", "images/characters/student/nana/nana_happy.png"
)

image sibling surprised = ConditionSwitch(
    "player_gender == 'F'", "images/characters/student/jake/jake_surprised.png",
    "True", "images/characters/student/nana/nana_surprised.png"
)

image sibling cake = ConditionSwitch(
    "player_gender == 'F'", "images/characters/student/jake/jake_cake.png",
    "True", "images/characters/student/nana/nana_cake.png"
)

#2 for character pronouns
define p = PronounSet(is_player=True)
define s = PronounSet(is_player=False)