# STORES ALL VARIABLES USED IN THE GAME

# Prologue #
default player_gender = "M"
default brother_name = "Jake"
default sister_name = "Nana"
default likes_art = False
default likes_science = False
default likes_games = False
default likes_sports = False


# Chapter 1 - Intro #



init python:
    def sibling_name():
        return store.brother_name if store.player_gender == "M" else store.sister_name