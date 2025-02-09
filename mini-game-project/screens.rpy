# filepath: /mini-game-project/mini-game-project/screens.rpy

# This file defines custom screens for the game, such as menus, inventory screens, or other user interface elements.

screen main_menu():
    tag menu

    frame:
        style_group "menu"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 20

            text "Mini Game Project" style "menu_title"

            textbutton "Start Game" action Start()
            textbutton "Load Game" action ShowMenu("load")
            textbutton "Options" action ShowMenu("preferences")
            textbutton "Quit" action Quit()

screen inventory():
    tag inventory

    frame:
        style_group "inventory"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 10

            text "Inventory" style "inventory_title"

            # Placeholder for inventory items
            text "You have no items." if not inventory_items else "{inventory_items}"

            textbutton "Close" action Hide("inventory")