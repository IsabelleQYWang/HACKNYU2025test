# filepath: /mini-game-project/mini-game-project/game/script.rpy

define e = Character("Eileen")
define l = Character("Liam")

label start:
    scene bg room
    e "Welcome to our mini game!"
    l "Are you ready to begin your adventure?"

    menu:
        "Yes, let's go!":
            jump adventure_start
        "Not yet.":
            e "Take your time. Let me know when you're ready."

label adventure_start:
    e "Great! Let's get started."
    # Add more game logic and narrative here

    return