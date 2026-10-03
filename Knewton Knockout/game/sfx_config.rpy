# game/sfx_config.rpy

init python:
    # 1. Automatically scan the folder for all audio variations at game boot
    # (renpy.list_files() works even after compiling/packaging your game into an .rpa file)
    DIALOGUE_SFX_FILES = [
        f for f in renpy.list_files() 
        if f.startswith("audio/sfx/dialogue/") and f.endswith((".ogg", ".wav", ".mp3"))
    ]

    def global_text_sfx(event, **kwargs):
        # 2. GUARDRAILS: Check if dialogue is triggering 'show' AND player is NOT skipping/rolling back
        if event == "show" and not renpy.config.skipping and not renpy.in_rollback():
            if DIALOGUE_SFX_FILES:
                # 3. Pick a random sound variation from the folder
                random_sfx = renpy.random.choice(DIALOGUE_SFX_FILES)
                renpy.sound.play(random_sfx, channel="sound")

    # 4. Attach callback globally to all speakers and dialogue lines
    config.character_callback = global_text_sfx