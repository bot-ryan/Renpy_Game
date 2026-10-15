# game/QuestSheet.rpy

# =========================================================
# 1. QUEST CLASS & QUEUE ENGINE
# =========================================================
init python:
    class Quest(object):
        def __init__(self, id, title, category, desc, steps, reward_text="None"):
            self.id = id
            self.title = title
            self.category = category  # "Main Quest" or "Side Quest"
            self.desc = desc
            self.steps = steps        # List of objective strings
            self.reward_text = reward_text
            
            # Runtime states
            self.status = "LOCKED"    # "LOCKED", "ACTIVE", "COMPLETED", "FAILED"
            self.current_step = 0

        def start(self):
            if self.status == "LOCKED":
                self.status = "ACTIVE"
                self.current_step = 0
                if hasattr(store, "notify_event"):
                    store.notify_event(f"New {self.category}: {self.title}")

        def advance(self):
            if self.status == "ACTIVE":
                self.current_step += 1
                if self.current_step >= len(self.steps):
                    self.status = "COMPLETED"
                    if hasattr(store, "notify_event"):
                        store.notify_event(f"Completed: {self.title}")
                else:
                    if hasattr(store, "notify_event"):
                        store.notify_event(f"Updated: {self.title}")

        def fail(self):
            if self.status == "ACTIVE":
                self.status = "FAILED"
                if hasattr(store, "notify_event"):
                    store.notify_event(f"Failed: {self.title}")

        def complete(self):
            """Immediately completes the quest regardless of current step progress."""
            if self.status in ["LOCKED", "ACTIVE"]:
                self.status = "COMPLETED"
                self.current_step = len(self.steps)  # Set step pointer to the end
                if hasattr(store, "notify_event"):
                    store.notify_event(f"Completed: {self.title}")


    class QuestManager(object):
        def __init__(self):
            self.quests = {}

        def register(self, quest_obj):
            self.quests[quest_obj.id] = quest_obj

        def start(self, quest_id):
            if quest_id in self.quests:
                self.quests[quest_id].start()

        def advance(self, quest_id):
            if quest_id in self.quests:
                self.quests[quest_id].advance()

        def fail(self, quest_id):
            if quest_id in self.quests:
                self.quests[quest_id].fail()

        def get_by_status(self, status):
            return [q for q in self.quests.values() if q.status == status]

        def complete(self, quest_id):
            """Convenience wrapper to immediately complete a quest by ID."""
            if quest_id in self.quests:
                self.quests[quest_id].complete()


    # Initialize Manager Store Object
    if not hasattr(store, "quest_mgr"):
        store.quest_mgr = QuestManager()


# =========================================================
# 2. MASTER QUEST REGISTRY & INITIALIZATION
# =========================================================
label init_quests:
    python:
        # MAIN QUEST 1
        quest_mgr.register(Quest(
            id="main_courtyard",
            title="Making the Rounds",
            category="Main Quest",
            desc="Get acquainted with your new classmates in the courtyard before class starts.",
            steps=[
                "Talk to Allenna in the courtyard.",
                "Talk to Celeste in the courtyard.",
                "Head inside to class."
            ],
            reward_text="Unlocks Chapter 3 Story Progression"
        ))

        # CONDITIONAL SIDE QUEST 1
        quest_mgr.register(Quest(
            id="side_allenna_snack",
            title="A Favor for Allenna",
            category="Side Quest",
            desc="Allenna mentioned she forgot her morning snack. See if you can find something for her.",
            steps=[
                "Ask Celeste if she has spare food.",
                "Deliver the snack to Allenna."
            ],
            reward_text="Increased affection with Allenna"
        ))

    return


# =========================================================
# 3. TWO-PANEL QUEST LOG SCREEN
# =========================================================
screen quest_log_screen():
    tag menu
    modal True

    # Hotkey & Escape toggles
    key "K_q" action Hide("quest_log_screen")
    key "game_menu" action [Hide("quest_log_screen"), Return()]

    # Default selected quest ID variable
    default selected_quest_id = None
    
    # Grab active/completed quests
    $ active_quests = quest_mgr.get_by_status("ACTIVE")
    $ completed_quests = quest_mgr.get_by_status("COMPLETED")

    # If no quest is selected, select the first active quest by default
    python:
        if selected_quest_id is None and active_quests:
            selected_quest_id = active_quests[0].id

    # Background Dimmer
    add Solid("#000000cc")

    # Main Window Frame
    frame:
        align (0.5, 0.5)
        xsize 1100
        ysize 650
        background Frame(Solid("#111827"), 12, 12)
        padding (25, 25)

        vbox:
            spacing 15

            # Header & Close Button
            hbox:
                xfill True
                text "QUEST JOURNAL" size 26 bold True color "#f59e0b" yalign 0.5
                textbutton "✕ Close" action Hide("quest_log_screen") align (1.0, 0.5)

            # Two-Panel Layout Divider
            hbox:
                spacing 25
                xfill True
                ysize 540

                # -------------------------------------------------
                # LEFT PANEL: Quest Selector List
                # -------------------------------------------------
                frame:
                    xsize 380
                    ysize 540
                    background Frame(Solid("#1f2937"), 8, 8)
                    padding (15, 15)

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 12
                            xfill True

                            # --- Active Quests Section ---
                            text "ACTIVE QUESTS" size 14 bold True color "#9ca3af"
                            
                            if not active_quests:
                                text "No active quests." size 14 italic True color "#6b7280"
                            else:
                                for q in active_quests:
                                    textbutton f"• {q.title}":
                                        action SetScreenVariable("selected_quest_id", q.id)
                                        text_size 16
                                        text_color ("#f59e0b" if selected_quest_id == q.id else "#ffffff")

                            null height 15

                            # --- Completed Quests Section ---
                            text "COMPLETED" size 14 bold True color "#9ca3af"
                            
                            if not completed_quests:
                                text "None completed yet." size 14 italic True color "#6b7280"
                            else:
                                for q in completed_quests:
                                    textbutton f"✓ {q.title}":
                                        action SetScreenVariable("selected_quest_id", q.id)
                                        text_size 16
                                        text_color ("#10b981" if selected_quest_id == q.id else "#9ca3af")

                # -------------------------------------------------
                # RIGHT PANEL: Quest Details View
                # -------------------------------------------------
                frame:
                    xsize 645
                    ysize 540
                    background Frame(Solid("#1f2937"), 8, 8)
                    padding (25, 20)

                    if selected_quest_id and selected_quest_id in quest_mgr.quests:
                        $ cur_q = quest_mgr.quests[selected_quest_id]

                        vbox:
                            spacing 12
                            xfill True

                            # Category & Title
                            text cur_q.category.upper() size 12 bold True color "#f59e0b"
                            text cur_q.title size 24 bold True color "#ffffff"

                            # Description
                            text cur_q.desc size 15 color "#d1d5db"

                            null height 10
                            text "OBJECTIVES" size 14 bold True color "#9ca3af"

                            # Objectives Step Checklist
                            vbox:
                                spacing 8
                                for idx, step_text in enumerate(cur_q.steps):
                                    hbox:
                                        spacing 10
                                        if cur_q.status == "COMPLETED" or idx < cur_q.current_step:
                                            text "[[✓]]" size 16 bold True color "#10b981"
                                            text step_text size 15 color "#9ca3af" strikethrough True
                                        elif idx == cur_q.current_step and cur_q.status == "ACTIVE":
                                            text "[[►]]" size 16 bold True color "#f59e0b"
                                            text step_text size 15 bold True color "#ffffff"
                                        else:
                                            text "[[ ]]" size 16 color "#6b7280"
                                            text step_text size 15 color "#6b7280"

                            null height 15
                            if cur_q.reward_text != "None":
                                text "REWARD" size 14 bold True color "#9ca3af"
                                text cur_q.reward_text size 14 italic True color "#10b981"

                    else:
                        text "Select a quest from the list to view details." align (0.5, 0.5) size 16 color "#6b7280"
# ==============================================================================
# QUEST MANAGER SYSTEM DOCUMENTATION & API REFERENCE
# ==============================================================================
# 
# 1. QUICK FUNCTION API REFERENCE
# ------------------------------------------------------------------------------
# Action                  | Ren'Py Python Command                       | Description
# ------------------------+---------------------------------------------+--------------------------------------------------------------
# Start / Unlock Quest    | $ quest_mgr.start("quest_id")               | Changes state from "LOCKED" to "ACTIVE". Triggers toast notification.
# Advance / Complete Step | $ quest_mgr.advance("quest_id")             | Advances step index by +1. Auto-completes when last step is cleared.
# Fail Quest              | $ quest_mgr.fail("quest_id")                | Directly sets state to "FAILED". Triggers toast notification.
# Complete Immediately    | $ quest_mgr.complete("quest_id")            | Instantly marks quest COMPLETED regardless of step progress.
# Check Quest Status      | quest_mgr.quests["quest_id"].status         | Returns string: "LOCKED", "ACTIVE", "COMPLETED", or "FAILED".
# Check Current Step      | quest_mgr.quests["quest_id"].current_step   | Returns integer index of current active objective (0-indexed).
# 
# 2. REGISTERING QUESTS (label init_quests)
# ------------------------------------------------------------------------------
# Quests must be registered in init_quests before being called in script files.
#
# Syntax Template:
#   quest_mgr.register(Quest(
#       id="unique_quest_id",         # Unique key string
#       title="Display Title",        # Quest name in UI
#       category="Main Quest",        # "Main Quest" or "Side Quest"
#       desc="Description text.",     # Quest details text
#       steps=[                       # List of step strings (ordered 0 to N)
#           "First objective",
#           "Second objective"
#       ],
#       reward_text="Optional Reward" # Text displayed in REWARD section
#   ))
#
#
# 3. WORKFLOW EXAMPLES IN SCRIPT FILES (.rpy)
# ------------------------------------------------------------------------------
# --- Example A: Starting a Main Quest ---
#   label ch3_start:
#       $ quest_mgr.start("main_courtyard")
#
# --- Example B: Unlocking Conditional Side Quests ---
#   menu:
#       "Offer to help Allenna":
#           $ quest_mgr.start("side_allenna_snack")
#       "Ignore her":
#           pass
#
# --- Example C: Advancing Objectives ---
#   $ quest_mgr.advance("main_courtyard") # Step 0 -> Step 1
#   $ quest_mgr.advance("main_courtyard") # Step 1 -> Step 2
#   $ quest_mgr.advance("main_courtyard") # Final Step -> Auto-marks COMPLETED
#
# --- Example D: Failing a Quest ---
#   if missed_deadline:
#       $ quest_mgr.fail("side_allenna_snack")
#
# --- Example E: Conditional Dialogue Gating ---
#   if quest_mgr.quests["side_allenna_snack"].status == "ACTIVE":
#       player "Hey Celeste, do you have spare food?"
#   elif quest_mgr.quests["side_allenna_snack"].status == "COMPLETED":
#       allenna "Thanks for bringing me that apple earlier!"
#
#
# 4. CONTROLS & KEYBINDINGS
# ------------------------------------------------------------------------------
# • Toggle Hotkey : Press "Q" or "Shift + Q" during gameplay.
# • Quick Menu    : Click "Quests (Q)" on the bottom HUD toolbar.
# • Pause Menu    : Access "Quests" directly from the ESC pause navigation menu.
# • Dismiss       : Press "Q", "Esc", or click "✕ Close" in the Journal window.
# ==============================================================================