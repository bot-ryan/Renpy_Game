# game/sfx_config.rpy

init python:
    # 1. CHOICE BUTTON SOUND EFFECTS (Style Property)
    # This attaches the sound specifically to dialogue choice buttons
    style.choice_button.activate_sound = "audio/sfx/ui_button_click.wav"
    # (Optional) Sound when hovering over a choice button:
    # style.choice_button.hover_sound = "audio/sfx/ui_button_hover.wav"

    # 2. CONFIRMATION POPUP SOUND EFFECTS (Yes / No)
    style.confirm_button.activate_sound = "audio/sfx/ui_button_click.wav"
    # style.confirm_button.hover_sound = "audio/sfx/ui_button_hover.wav" # Optional hover


    # 3. RANDOM DIALOGUE SFX SCANNER
    DIALOGUE_SFX_FILES = [
        f for f in renpy.list_files() 
        if f.startswith("audio/sfx/dialogue/") and f.endswith((".ogg", ".wav", ".mp3"))
    ]

    def global_text_sfx(event, **kwargs):
        # PRIORITY CHECK: Mute dialogue SFX while a toast notification is showing
        if hasattr(store, "toast_mgr") and store.toast_mgr.is_showing:
            return

        # Regular dialogue SFX logic
        if event == "show" and not renpy.config.skipping and not renpy.in_rollback():
            if DIALOGUE_SFX_FILES:
                random_sfx = renpy.random.choice(DIALOGUE_SFX_FILES)
                renpy.sound.play(random_sfx, channel="sound")

    # Attach callback globally to all characters
    config.character_callback = global_text_sfx