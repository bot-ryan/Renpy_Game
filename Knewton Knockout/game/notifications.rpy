# game/notifications.rpy

# =========================================================
#                       HOW TO USE
# =========================================================
# 1. To trigger a choice/memory event notification:
#    notify_event("Ashley will remember that", icon="images/ui/icons/memory_icon.png")
# 2. To unlock an achievement and show the achievement card:
#    unlock_achievement("first_meeting")

# =========================================================
# 1. DATA REGISTRIES & PERSISTENCE INITIALIZATION
# =========================================================
init python:
    import queue

    # Global persistent set for unlocked achievements (persists across all saves)
    if persistent.unlocked_achievements is None:
        persistent.unlocked_achievements = set()

    # ACHIEVEMENT REGISTRY
    # Add all your game's achievements here
    ACHIEVEMENTS = {
        "first_meeting": {
            "title": "Making Connections",
            "desc": "Met your classmates in Chapter 3.",
            "icon": "images/ui/achievements/first_meeting.png",
            "sfx": "audio/sfx/achievement_unlock.wav",
        },
        "sports_star": {
            "title": "Athletic Legend",
            "desc": "Showed off your athletic skills.",
            "icon": "images/ui/achievements/sports.png",
            "sfx": "audio/sfx/achievement_unlock.wav",
        }
    }

    # Audio Defaults
    DEFAULT_EVENT_SFX = "audio/sfx/trigger_event.wav"
    DEFAULT_ACHIEVEMENT_SFX = "audio/sfx/trigger_achievement.wav"


# =========================================================
# 2. TOAST QUEUE MANAGER ENGINE
# =========================================================
init python:
    class ToastQueueManager(object):
        def __init__(self):
            self.queue = []
            self.is_showing = False

        def push(self, notif_type, title, desc="", icon=None, sfx=None, duration=3.5):
            self.queue.append({
                "type": notif_type,       # "event" or "achievement"
                "title": title,
                "desc": desc,
                "icon": icon,
                "sfx": sfx,
                "duration": duration
            })
            self.process_next()

        def process_next(self):
            if not self.is_showing and self.queue:
                self.is_showing = True
                current = self.queue.pop(0)

                # Play sound effect only if player is not fast-forwarding/skipping
                if current["sfx"] and not renpy.config.skipping:
                    renpy.sound.play(current["sfx"], channel="sound")

                renpy.show_screen("notification_toast", data=current)

        def dismiss(self):
            renpy.hide_screen("notification_toast")
            self.is_showing = False
            # Check for the next item in queue
            renpy.timeout(0.1)
            self.process_next()

    # Global instance of the queue manager
    toast_mgr = ToastQueueManager()


    # ---------------------------------------------------------
    # HELPER FUNCTIONS FOR DIALOGUE & STORY SCRIPTS
    # ---------------------------------------------------------
    def notify_event(msg, icon=None, sfx=DEFAULT_EVENT_SFX):
        """Triggers a choice/memory event toast (e.g. 'Ashley will remember that')"""
        toast_mgr.push(
            notif_type="event",
            title=msg,
            icon=icon,
            sfx=sfx,
            duration=3.0
        )

    def unlock_achievement(achievement_id):
        """Unlocks an achievement globally and displays the achievement card"""
        if achievement_id not in ACHIEVEMENTS:
            return

        # Only trigger popup if not previously unlocked in persistent data
        if achievement_id not in persistent.unlocked_achievements:
            persistent.unlocked_achievements.add(achievement_id)
            data = ACHIEVEMENTS[achievement_id]
            
            toast_mgr.push(
                notif_type="achievement",
                title=data["title"],
                desc=data["desc"],
                icon=data.get("icon"),
                sfx=data.get("sfx", DEFAULT_ACHIEVEMENT_SFX),
                duration=4.5
            )


# =========================================================
# 3. TOAST DISPLAY SCREEN & TRANSFORMS
# =========================================================

# --- TRANSFORMS (ANIMATIONS) ---
transform event_toast_anim:
    xanchor 0.5 yanchor 0.0
    xpos 0.5 ypos -100
    easein 0.3 ypos 35
    on hide:
        easeout 0.3 ypos -100

transform achievement_toast_anim:
    xanchor 1.0 yanchor 0.0
    xpos 1.3 ypos 40
    easein 0.4 xpos 0.97
    on hide:
        easeout 0.3 xpos 1.3


# --- TOAST SCREEN ---
screen notification_toast(data):
    zorder 500 # Floats over dialogue boxes and character sprites

    # Auto-dismiss timer
    timer data["duration"] action Function(toast_mgr.dismiss)

    if data["type"] == "event":
        # Event Memory Banner (Top-Center Pill)
        frame:
            at event_toast_anim
            style "event_toast_frame"

            hbox:
                spacing 12
                align (0.5, 0.5)

                if data["icon"]:
                    add data["icon"] yalign 0.5 maxsize (32, 32)

                text data["title"] style "event_toast_text" yalign 0.5

    else:
        # Achievement Unlocked Banner (Top-Right Card)
        frame:
            at achievement_toast_anim
            style "achievement_toast_frame"

            hbox:
                spacing 16
                yalign 0.5

                if data["icon"]:
                    add data["icon"] yalign 0.5 maxsize (48, 48)

                vbox:
                    yalign 0.5
                    spacing 2
                    text "ACHIEVEMENT UNLOCKED" style "achievement_header_text"
                    text data["title"] style "achievement_title_text"
                    if data["desc"]:
                        text data["desc"] style "achievement_desc_text"


# =========================================================
# 4. STYLES
# =========================================================
style event_toast_frame:
    background Frame(Solid("#1e222dbe"), 10, 10)
    padding (24, 10)

style event_toast_text:
    size 20
    color "#e0e6ed"
    italic True

style achievement_toast_frame:
    background Frame(Solid("#111827f0"), 12, 12)
    padding (18, 14)
    xminimum 340

style achievement_header_text:
    size 13
    bold True
    color "#f59e0b" # Gold Accent Color

style achievement_title_text:
    size 20
    bold True
    color "#ffffff"

style achievement_desc_text:
    size 15
    color "#9ca3af"