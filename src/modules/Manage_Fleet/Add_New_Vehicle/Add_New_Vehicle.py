# Add_New_Vehicle.py
import sys
sys.path.append('/Users/osmanileon/Desktop/AxleAxis-CLI')
import os
import re
from src.database.database import add_or_update_vehicle, create_connection
from src.utils import display_top_menu
import urwid
import datetime
# from PyInquirer import prompt
from colorama import Fore, Style, init
init()

def validate_vin(vin):
    """Validate the VIN (Vehicle Identification Number)."""
    return bool(re.match(r"^[A-HJ-NPR-Z0-9]{17}$", vin))

def is_valid_year(year):
    """Check if the entered year is valid."""
    current_year = datetime.datetime.now().year
    try:
        year = int(year)
        return 1900 <= year <= current_year + 1
    except ValueError:
        return False

def show_error_message(message):
    """Display an error message to the user."""
    urwid.ExitMainLoop()
    print(Fore.RED + message + Style.RESET_ALL)

def on_save(button, user_data):
    # Extracting the edit_text from each Edit widget wrapped in AttrMap
    vin, make, model, year = [edit.base_widget.edit_text for edit in user_data]

    if not validate_vin(vin):
        show_error_message("Invalid VIN. Please enter a valid 17-character VIN.")
        return
    if not is_valid_year(year):
        show_error_message("Invalid Year. Please enter a year between 1900 and " + str(datetime.datetime.now().year + 1))
        return

    conn = create_connection()
    if conn is not None:
        try:
            add_or_update_vehicle(conn, vin, make, model, int(year))
            print(Fore.GREEN + "Vehicle added/updated successfully." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "Failed to add/update vehicle in the database. Error: " + str(e) + Style.RESET_ALL)
        finally:
            conn.close()
    else:
        print(Fore.RED + "Failed to connect to the database." + Style.RESET_ALL)

    urwid.ExitMainLoop()

def main():
    # Navigation bar
    nav_bar = display_top_menu()

    # Form fields
    vin_edit = urwid.Edit("Enter VIN (17 characters): ", edit_text='', wrap='clip')
    vin_edit = urwid.AttrMap(vin_edit, None, focus_map='reversed')
    make_edit = urwid.Edit("Enter Make: ")
    model_edit = urwid.Edit("Enter Model: ")
    year_edit = urwid.Edit("Enter Year: ")

    # This line ensures that the user cannot enter more than 17 characters
    vin_edit.base_widget.set_edit_text = (lambda text: setattr(vin_edit.base_widget, '_edit_text', text[:17]))


    # Buttons
    save_button = urwid.Button("Save")
    back_button = urwid.Button("Back")
    buttons = urwid.GridFlow([save_button, back_button], cell_width=15, h_sep=2, v_sep=1, align='center')

    # Define the actions for the Save button
    urwid.connect_signal(save_button, 'click', lambda button: on_save(button, [vin_edit, make_edit, model_edit, year_edit]))

    # Padding and spacing
    form_fields = urwid.Pile([vin_edit, urwid.Divider(), make_edit, urwid.Divider(), model_edit, urwid.Divider(), year_edit])
    padded_form = urwid.Padding(form_fields, left=2, right=2)
    padded_buttons = urwid.Padding(buttons, left=2, right=2)

    # Combine padded form and buttons into a single pile
    form = urwid.Pile([padded_form, urwid.Divider('-', 1), padded_buttons])

    # Main layout with navigation bar and form
    layout = urwid.ListBox(urwid.SimpleFocusListWalker([nav_bar, urwid.Divider('=', 1), form]))

    urwid.MainLoop(layout).run()

if __name__ == "__main__":
    main()