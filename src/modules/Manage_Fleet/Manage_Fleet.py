import sys
import os
import curses  # For advanced terminal handling
sys.path.append('/Users/osmanileon/Desktop/AxleAxis-CLI')
import urwid
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import button_dialog
from src.database.database import create_connection, add_or_update_vehicle, delete_vehicle, get_all_vehicles

# Import other necessary functions from modules
from src.utils import display_top_menu

# from src.main import main_menu as main_menu

# # functions from modules
# from modules.Manage_Fleet.Driver_Assignment.Assign_Driver_to_Vehicle import main as Assign_Driver_to_Vehicle_main
# from modules.Manage_Fleet.Driver_Assignment.Remove_Assignment import main as Remove_Assignment_main
# from modules.Manage_Fleet.Driver_Assignment.Update_Assignment import main as Update_Assignment_main
# from modules.Manage_Fleet.Driver_Assignment.View_Current_Assignments import main as View_Current_Assignments_main
# functions from modules
from Update_Vehicle_Information.Update_Vehicle_Information import main as Update_Vehicle_Information_main
from Add_New_Vehicle.Add_New_Vehicle import main as Add_New_Vehicle_main
# from modules.Manage_Fleet.Remove_Vehicle.Remove_Vehicle import main as Remove_Vehicle_main
# from modules.Manage_Fleet.List_All_Vehicles.List_All_Vehicles import main as List_All_Vehicles_main

# # functions from modules
# from modules.Manage_Fleet.Fleet_Utilization_Reports.Generate_Utilization_Report import main as Generate_Utilization_Report_main
# from modules.Manage_Fleet.Fleet_Utilization_Reports.View_Past_Reports import main as View_Past_Reports_main

# # functions from modules
# from modules.Manage_Fleet.Vehicle_Maintenance_Management.Remove_Maintenance_Record import main as Remove_Maintenance_Record_main
# from modules.Manage_Fleet.Vehicle_Maintenance_Management.Schedule_Maintenance import main as Schedule_Maintenance_main
# from modules.Manage_Fleet.Vehicle_Maintenance_Management.Update_Maintenance_Record import main as Update_Maintenance_Record_main
# from modules.Manage_Fleet.Vehicle_Maintenance_Management.View_Maintenance_Records import main as View_Maintenance_Records_main
from colorama import Fore, Style, init
init()
# ... import other main functions from modules ...

def manage_fleet_menu():
    
    top_menu = display_top_menu()

    # Define buttons for each submenu option
    buttons = []
    options = [
        ("Add New Vehicle", add_new_vehicle),
        ("Update Vehicle Information", update_vehicle_information),
        # ("Remove Vehicle", remove_vehicle)
        # ("List All Vehicles", list_all_vehicles)
        # ("Vehicle Maintenance Management", vehicle maintenance management)
        # ("Driver Assignment", driver assignment)
        # ("Fleet Utilization Reports", fleet utilization reports)
        # # ... Add other options here ...
        # ("Return to Main Menu", return_to_main_menu)
    ]

    for label, callback in options:
        button = urwid.Button(label)
        urwid.connect_signal(button, 'click', callback)
        buttons.append(urwid.AttrMap(button, None, focus_map='reversed'))
        
    # Back button
    back_button = urwid.Button("Back", on_press=lambda button:)
    back_button = urwid.AttrMap(back_button, None, focus_map='reversed')

    # Layout for buttons (vertically stacked)
    buttons_layout = urwid.Pile(buttons)
    # Buttons layout
    buttons = urwid.GridFlow([back_button], cell_width=15, h_sep=2, v_sep=1, align='center')


    pile = urwid.Pile([top_menu, urwid.Divider(), buttons_layout])
    top = urwid.Filler(pile, valign='top')

    urwid.MainLoop(top).run()



def add_new_vehicle(button):
    """
    Function to handle Add New Vehicle option.
    This function will invoke the Add_New_Vehicle script or function.
    """
    Add_New_Vehicle_main()

def update_vehicle_information(button):
    """
    Function to handle Update Vehicle Information option.
    This function will invoke the update_vehicle_information script or function.
    """
    Update_Vehicle_Information_main()



# def return_to_main_menu(button):
#     """
#     Function to handle Return to Main Menu option.
#     This function will invoke the return_to_main_menu script or function.
#     """
#     return_to_main_menu()

# def main():
#     manage_fleet_menu()

# Add this check to allow direct calling of manage_fleet_menu
if __name__ == "__main__":
    manage_fleet_menu()