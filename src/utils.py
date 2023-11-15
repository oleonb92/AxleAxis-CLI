import os
import urwid
from colorama import Fore, Style, init

# init()

# def display_top_menu():
#     width = os.get_terminal_size().columns
#     # menu_options = "Manage Fleet | Dispatch | Brokerage Services | Generate Reports | Manage Finances"

#     top_menu_text = [
#         ("center", "=" * width + "\n"),
#         ("center", "AxleAxis-CLI | Fleet Management | Dispatch System\n"),
#         ("center", "=" * width + "\n"),
#         ("center", menu_options + "\n"),
#         ("center", "Press 1-5 to navigate, or 'X' to exit.\n")
#     ]
    
#     return urwid.Text(top_menu_text)

# def back_to_main_menu():
#     """
#     Function to handle return to the main menu.
#     This can be a placeholder function that just raises ExitMainLoop for now.
#     """
#     raise urwid.ExitMainLoop()

# # def back_to_manage_fleet():
# #     return 'back_to_manage_fleet'

def navigate_to_manage_fleet(button):
    # Import the function to navigate to Manage Fleet
    from modules.Manage_Fleet.Manage_Fleet import manage_fleet_menu
    manage_fleet_menu()

def navigate_to_dispatch(button):
    """
    Placeholder function for navigating to the Dispatch section.
    """
    # TODO: Implement the actual navigation logic
    print("Navigate to Dispatch section - Functionality to be implemented")

def navigate_to_Brokerage_Services(button):
    """
    Placeholder function for navigating to the Brokerage Services section.
    """
    # TODO: Implement the actual navigation logic
    print("Navigate to Brokerage Services section - Functionality to be implemented")
def navigate_to_Generate_Reports(button):
    """
    Placeholder function for navigating to the Generate Reports section.
    """
    # TODO: Implement the actual navigation logic
    print("Navigate to Generate Reports section - Functionality to be implemented")

def navigate_to_Manage_Finances(button):
    """
    Placeholder function for navigating to the Manage Finances section.
    """
    # TODO: Implement the actual navigation logic
    print("Navigate to Manage Finances section - Functionality to be implemented")
# Add similar functions for other menu options...

def display_top_menu():
    # Define buttons for each main menu option
    menu_buttons = [
        urwid.Button("Manage Fleet", on_press=navigate_to_manage_fleet),
        urwid.Button("Dispatch", on_press=navigate_to_dispatch),
        urwid.Button("Brokerage Services", on_press=navigate_to_Brokerage_Services),  # Define on_press if needed
        urwid.Button("Generate Reports", on_press=navigate_to_Generate_Reports),    # Define on_press if needed
        urwid.Button("Manage Finances", on_press=navigate_to_Manage_Finances)      # Define on_press if needed
        # Add more buttons for other options...
    ]

    # Style the buttons if needed
    styled_buttons = [urwid.AttrMap(button, None, focus_map='reversed') for button in menu_buttons]

    # Create a horizontal flow of buttons
    menu_bar = urwid.Columns(styled_buttons)

    return menu_bar





