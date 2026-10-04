# STORES ALL VARIABLES USED IN THE GAME

# Prologue #
default player_gender = "M"
default brother_name = "Shakey"
default sister_name = "Nana"
default likes_art = False
default likes_science = False
default likes_games = False
default likes_sports = False


# Chapter 1 - Intro #



init python:
    # 1. Helper functions to fetch hex colors from CHARACTER_DATA
    def get_brother_color():
        return CHARACTER_DATA.get("jake", {}).get("color", "#66b2ff")  # Default soft blue if 'jake' isn't in dictionary

    def get_sister_color():
        return CHARACTER_DATA.get("nana", {}).get("color", "#ff9999")  # Pulls #ff9999 from Nana's profile

    # 2. Your player and sibling name getters with color formatting merged in
    def player_name():
        if store.player_gender == "M":
            name = store.brother_name
            color = get_brother_color()
        else:
            name = store.sister_name
            color = get_sister_color()
            
        return f"{{color={color}}}{name}{{/color}}"

    def sibling_name():
        if store.player_gender == "F":
            name = store.brother_name
            color = get_brother_color()
        else:
            name = store.sister_name
            color = get_sister_color()
            
        return f"{{color={color}}}{name}{{/color}}"

    def get_player_pronouns():
        return ["his", "him", "he" ] if store.player_gender == "M" else ["her", "her", "she"]

    def get_sibling_pronouns():
        return ["her", "her", "she"] if store.player_gender == "M" else ["his", "him", "he"]

    def just_player_name():
        return store.brother_name if store.player_gender == "M" else store.sister_name

    def just_brother():
        return f"{{color={get_brother_color()}}}{store.brother_name}{{/color}}"

    def just_sister():
        return f"{{color={get_sister_color()}}}{store.sister_name}{{/color}}"
