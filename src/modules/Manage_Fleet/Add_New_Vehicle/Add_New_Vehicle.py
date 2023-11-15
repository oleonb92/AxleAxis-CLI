import sys
sys.path.append('/Users/osmanileon/Desktop/AxleAxis-CLI')
import os
import re
from src.database.database import add_or_update_vehicle, create_connection
from src.utils import display_top_menu
import urwid
# from PyInquirer import prompt
from colorama import Fore, Style, init
init()

def validate_vin(vin):
    """Validate the VIN (Vehicle Identification Number)."""
    return bool(re.match(r"^[A-HJ-NPR-Z0-9]{17}$", vin))

def is_valid_year(year):
    """Check if the entered year is valid."""
    try:
        year = int(year)
        return 1900 <= year <= 2023  # Adjust the year range as needed
    except ValueError:
        return False

def on_save(button, user_data):
    vin, make, model, year = [edit.edit_text for edit in user_data]
    if not validate_vin(vin):
        raise urwid.ExitMainLoop()
    if not is_valid_year(year):
        raise urwid.ExitMainLoop()

    conn = create_connection()
    if conn is not None:
        add_or_update_vehicle(conn, vin, make, model, int(year))
        conn.close()
    else:
        print("Failed to connect to the database.")

    raise urwid.ExitMainLoop()

def main():
    # Navigation bar
    nav_bar = display_top_menu()

    # Form fields
    vin_edit = urwid.Edit("Enter VIN (17 characters): ")
    make_edit = urwid.Edit("Enter Make: ")
    model_edit = urwid.Edit("Enter Model: ")
    year_edit = urwid.Edit("Enter Year: ")

    # Buttons
    save_button = urwid.Button("Save")
    back_button = urwid.Button("Back")
    buttons = urwid.GridFlow([save_button, back_button], cell_width=15, h_sep=2, v_sep=1, align='center')

    # Padding and spacing
    form_fields = urwid.Pile([vin_edit, urwid.Divider(), make_edit, urwid.Divider(), model_edit, urwid.Divider(), year_edit])
    padded_form = urwid.Padding(form_fields, left=2, right=2)  # Add horizontal padding to form
    padded_buttons = urwid.Padding(buttons, left=2, right=2)  # Add horizontal padding to buttons

    # Combine padded form and buttons into a single pile
    form = urwid.Pile([padded_form, urwid.Divider('-', 1), padded_buttons])

    # Main layout with navigation bar and form
    layout = urwid.ListBox(urwid.SimpleFocusListWalker([nav_bar, urwid.Divider('=', 1), form]))

    urwid.MainLoop(layout).run()

if __name__ == "__main__":
    main()
# def back_to_manage_fleet():
#     """
#     Exit the current Urwid main loop.
#     This function should ideally handle the transition back to the Manage_Fleet page.
#     Currently, it just exits the main loop of the Urwid interface.
#     """
#     raise urwid.ExitMainLoop()


# def main():
#     top_menu = display_top_menu()
#     vin_edit = urwid.Edit("Enter VIN (17 characters): ")
#     make_edit = urwid.Edit("Enter Make: ")
#     model_edit = urwid.Edit("Enter Model: ")
#     year_edit = urwid.Edit("Enter Year: ")

#     save_button = urwid.Button("Save")
#     urwid.connect_signal(save_button, 'click', lambda button: on_save(button, [vin_edit, make_edit, model_edit, year_edit]))

#     pile = urwid.Pile([top_menu, vin_edit, make_edit, model_edit, year_edit, save_button])
#     top = urwid.Filler(pile, valign='top')

#     urwid.MainLoop(top).run()
