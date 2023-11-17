# Update_Vehicle_Information.py
import sys
sys.path.append('/Users/osmanileon/Desktop/AxleAxis-CLI')
import os
import re
import datetime
from src.database.database import get_vehicle, add_or_update_vehicle, create_connection
from src.utils import display_top_menu
import urwid
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
    print(Fore.RED + message + Style.RESET_ALL)

def search_vehicle(vin):
    """Search for a vehicle and display its information."""
    conn = create_connection()
    if conn is not None:
        vehicle = get_vehicle(conn, vin)
        conn.close()
        return vehicle
    else:
        show_error_message("Failed to connect to the database.")
        return None

def on_update(button, vin, make_edit, model_edit, year_edit):
    make = make_edit.edit_text
    model = model_edit.edit_text
    year = year_edit.edit_text

    if not is_valid_year(year):
        show_error_message("Invalid Year. Please enter a year between 1900 and " + str(datetime.datetime.now().year + 1))
        return

    conn = create_connection()
    if conn is not None:
        try:
            add_or_update_vehicle(conn, vin, make, model, int(year))
            print(Fore.GREEN + "Vehicle information updated successfully." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "Failed to update vehicle in the database. Error: " + str(e) + Style.RESET_ALL)
        finally:
            conn.close()
    else:
        print(Fore.RED + "Failed to connect to the database." + Style.RESET_ALL)

def main():
    # Navigation bar
    nav_bar = display_top_menu()

    # VIN search
    vin_search_edit = urwid.Edit("Enter VIN to search (17 characters): ", edit_text='', wrap='clip')
    vin_search_edit = urwid.AttrMap(vin_search_edit, None, focus_map='reversed')

    # Limit VIN search input to 17 characters
    vin_search_edit.base_widget.set_edit_text = lambda text: setattr(vin_search_edit.base_widget, '_edit_text', text[:17])

    search_button = urwid.Button("Search")
    search_results = urwid.Text("")

    def on_search(button):
        vin = vin_search_edit.base_widget.edit_text
        if validate_vin(vin):
            vehicle = search_vehicle(vin)
            if vehicle:
                _, make, model, year = vehicle
                make_edit.set_edit_text(make)
                model_edit.set_edit_text(model)
                year_edit.set_edit_text(str(year))
                search_results.set_text("Update the fields below and press 'Update' to save changes.")
            else:
                search_results.set_text("Vehicle not found.")
        else:
            search_results.set_text("Invalid VIN. Please enter a valid 17-character VIN.")

    urwid.connect_signal(search_button, 'click', on_search)

    # Update form fields
    make_edit = urwid.Edit("Enter Make: ")
    model_edit = urwid.Edit("Enter Model: ")
    year_edit = urwid.Edit("Enter Year: ")

    # Buttons
    update_button = urwid.Button("Update")
    back_button = urwid.Button("Back")
    buttons = urwid.GridFlow([update_button, back_button], cell_width=15, h_sep=2, v_sep=1, align='center')

    # Define actions for the Update button
    urwid.connect_signal(update_button, 'click', lambda button: on_update(button, vin_search_edit.base_widget.edit_text, make_edit, model_edit, year_edit))

    # Padding and spacing
    search_section = urwid.Pile([vin_search_edit, urwid.Divider(), search_button, urwid.Divider(), search_results])
    padded_search = urwid.Padding(search_section, left=2, right=2)
    update_section = urwid.Pile([make_edit, urwid.Divider(), model_edit, urwid.Divider(), year_edit])
    padded_update = urwid.Padding(update_section, left=2, right=2)
    padded_buttons = urwid.Padding(buttons, left=2, right=2)

    # Combine sections into a single layout
    form = urwid.Pile([padded_search, urwid.Divider(), padded_update, urwid.Divider('-', 1), padded_buttons])

    # Main layout with navigation bar and form
    layout = urwid.ListBox(urwid.SimpleFocusListWalker([nav_bar, urwid.Divider('=', 1), form]))

    urwid.MainLoop(layout).run()

if __name__ == "__main__":
    main()
