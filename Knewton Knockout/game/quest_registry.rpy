# game/quest_registry.rpy

# =========================================================
# MASTER QUEST REGISTRY & INITIALIZATION
# =========================================================
label init_quests:
    python:
        # -------------------------------------------------
        # MAIN QUEST 1: Chapter 3 Courtyard Introductions
        # -------------------------------------------------
        quest_mgr.register(Quest(
            id="main_courtyard",
            title="Making the Rounds",
            category="Main Quest",
            desc="Get acquainted with your new classmates in the courtyard before class starts.",
            steps=[
                "Talk to Allenna in the courtyard.",   # Index 0
                "Talk to Celeste in the courtyard.",   # Index 1
                "Head inside to class."                # Index 2
            ],
            reward_text="Unlocks Chapter 3 Story Progression"
        ))

        # -------------------------------------------------
        # CONDITIONAL SIDE QUEST 1
        # -------------------------------------------------
        quest_mgr.register(Quest(
            id="side_allenna_snack",
            title="A Favor for Allenna",
            category="Side Quest",
            desc="Allenna mentioned she forgot her morning snack. See if you can find something for her.",
            steps=[
                "Ask Celeste if she has spare food.",  # Index 0
                "Deliver the snack to Allenna."        # Index 1
            ],
            reward_text="Increased affection with Allenna"
        ))

    return