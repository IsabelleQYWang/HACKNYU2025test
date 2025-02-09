define gui_style = Style("gui_style", "default")

# GUI Definitions
style.default.font = "DejaVuSans.ttf"
style.default.size = 20
style.default.color = "#FFFFFF"

style.button = Style("button", "default")
style.button.size = 24
style.button.color = "#FFFFFF"
style.button.hover_color = "#FFCC00"
style.button.background = "button_normal.png"
style.button.hover_background = "button_hover.png"

style.text = Style("text", "default")
style.text.size = 18
style.text.color = "#FFFFFF"

# Layout Settings
screen main_menu():
    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Welcome to the Mini Game!" style="text"
        textbutton "Start Game" action Start()
        textbutton "Quit" action Quit()