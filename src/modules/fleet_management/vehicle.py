# TESTED AND WORKING FINE!


import sys
import os
import psycopg2

# Add the root directory of your project to sys.path
sys.path.append('/Users/osmanileon/Desktop/AxleAxis-CLI')

# Import necessary database functions for vehicle management
from src.database.database import create_connection, add_or_update_vehicle, get_vehicle, delete_vehicle

class VehicleManagement:
    def __init__(self):
        self.conn = create_connection()

    def add_update_vehicle(self, vin, make, model, year):
        """Add or update a vehicle in the fleet."""
        try:
            add_or_update_vehicle(self.conn, vin, make, model, year)
            return f"Vehicle {vin} - {make} {model}, {year} added/updated successfully."
        except Exception as e:
            return f"Error in adding/updating vehicle: {str(e)}"

    def retrieve_vehicle_info(self, vin):
        """Retrieve information of a specific vehicle."""
        try:
            vehicle_info = get_vehicle(self.conn, vin)
            if vehicle_info:
                return vehicle_info
            else:
                return "Vehicle not found."
        except Exception as e:
            return f"Error in retrieving vehicle info: {str(e)}"

    def remove_vehicle(self, vin):
        """Remove a vehicle from the fleet."""
        try:
            delete_vehicle(self.conn, vin)
            return f"Vehicle with VIN {vin} removed successfully."
        except Exception as e:
            return f"Error in removing vehicle: {str(e)}"

    def close_connection(self):
        if self.conn:
            self.conn.close()

# Example usage
if __name__ == "__main__":
    vehicle_manager = VehicleManagement()

    # Example operations
    print(vehicle_manager.add_update_vehicle("VIN123", "Toyota", "Camry", 2022))
    print(vehicle_manager.retrieve_vehicle_info("VIN123"))
    # print(vehicle_manager.remove_vehicle("VIN123"))  # Uncomment to test removal
