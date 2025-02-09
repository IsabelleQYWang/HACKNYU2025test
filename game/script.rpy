# THE MINI GAME - CLICK COUNTER

init python:
    def click_counter():
        global click_times
        click_times += 1

    def start_game():
        global click_times, countdown_time, count_clicks
        click_times = 0
        countdown_time = 5
        count_clicks = True  # Enable clicking and start countdown

    def reset_click_counter():
        global click_times, countdown_time, count_clicks
        click_times = 0
        countdown_time = 5
        count_clicks = True

transform button_hover:
    on hover:
        easein 0.2 zoom 1.05
    on idle:
        easeout 0.2 zoom 1.0

screen click_counter_game:
    image "background.png"
    key "K_x" action If(count_clicks, Function(click_counter), NullAction())
    
    # Game instructions (only shows before first play)
    if not count_clicks and click_times == 0:
        text "Click as fast as you can in 5 seconds!\nUse the mouse to click the X button or press the X key.\nYour clicks will be counted until the timer runs out.\nClick Start to begin!" align(0.5, 0.3) outlines[(absolute(3.0), "#000000", 0, 0)] size 45

    # Game stats display (always visible)
    text "Clicks: [click_times] Time Left: [countdown_time]" align(0.5, 0.65) outlines[(absolute(3.0), "#000000", 0, 0)] size 45

    # Game elements
    if count_clicks:
        # Display cookie as background image
        image "cookie.png" align(0.5, 0.4)
        
        # Clickable exit button on top-right of cookie
        imagebutton idle "exit.png":
            align(0.60, 0.30)  # Adjust these values to position over cookie's top-right
            sensitive count_clicks
            action Function(click_counter)
            at button_hover

    # Countdown timer
    if count_clicks:
        timer 1.0 action If(countdown_time > 0, 
            SetVariable("countdown_time", countdown_time - 1), 
            SetVariable("count_clicks", False)
        ) repeat True

    # Game over screen
    if not count_clicks:
        if click_times < 5:
            text "DID YOU TRIED??" align(0.5, 0.75) outlines [(3.0, "#000000", 0, 0)] color "#FFF" size 45 
        elif click_times < 15:
            text "TRY HARDER" align(0.5, 0.75) outlines [(3.0, "#000000", 0, 0)] color "#FFF" size 45 
        elif click_times < 30:
            text "You're fast!" align(0.5, 0.75) outlines [(3.0, "#000000", 0, 0)] color "#FFF" size 45
        else:
            text "OMG!! You've got skills!" align(0.5, 0.75) outlines [(3.0, "#000000", 0, 0)] color "#FFF" size 45

        # Start/Restart button or auto-retry
        if click_times == 0:
            imagebutton idle "start.png" action Function(start_game) align(0.5, 0.84) at button_hover
        else:
            if click_times >= 15:
                imagebutton idle "again.png" action Function(reset_click_counter) align(0.5, 0.84) at button_hover
            else:
                text "Too slow! YOU GOT SCAMED!! Trying again in 2 seconds..." align(0.5, 0.9) outlines [(absolute(3.0), "#000000", 0, 0)] color "#FF0000" size 200
                timer 2.0 action Function(reset_click_counter)

default click_times = 0
default countdown_time = 5
default count_clicks = False

label start:
    show screen click_counter_game
    pause
