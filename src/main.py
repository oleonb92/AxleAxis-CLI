import sys
import os
import curses  # For advanced terminal handling
sys.path.append('/Users/osmanileon/Desktop/AxleAxis-CLI')
import urwid
from modules.Dispatch.Dispatch import main as dispatch_main
from src.utils import display_top_menu
from colorama import Fore, Style, init
init()
# ... import other main functions from modules ...

# Import main functions from modules
from src.modules.Manage_Fleet.Manage_Fleet import manage_fleet_menu as manage_fleet_menu
# ... other imports ...

# Main menu function
def main_menu():
    top_menu = display_top_menu()

    # Define buttons for main menu options
    buttons = []
    options = [
        ("Manage Fleet", manage_fleet_menu),
        ("Dispatch", dispatch_main),
        # ... other options...
    ]

    for label, callback in options:
        button = urwid.Button(label)
        urwid.connect_signal(button, 'click', lambda button, callback=callback: callback())
        buttons.append(urwid.AttrMap(button, None, focus_map='reversed'))

    # Layout for buttons (vertically stacked)
    buttons_layout = urwid.Pile(buttons)

    pile = urwid.Pile([urwid.Text(top_menu), urwid.Divider(), buttons_layout])
    top = urwid.Filler(pile, valign='top')

    urwid.MainLoop(top).run()

    while True:
        # Run the main loop
        main_loop = urwid.MainLoop(top)
        main_loop.run()

if __name__ == "__main__":
    main_menu()