import sys
import os

# Add the root directory of your project to sys.path
sys.path.append('/Users/osmanileon/Desktop/AxleAxis-CLI')

from src.database.database import create_connection, add_or_update_driver, get_driver, delete_driver

class DriverManagement:
    def __init__(self):
        self.conn = create_connection()

    def register_driver(self, name, license_number, phone_number, email):
        """Registers a new driver or updates an existing one."""
        try:
            add_or_update_driver(self.conn, name, license_number, phone_number, email)
            return f"Driver {name} registered/updated successfully."
        except Exception as e:
            return f"Error in registering/updating driver: {str(e)}"

    def retrieve_driver_info_by_name(self, driver_name):
        """Retrieves information for a specific driver by name."""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT * FROM drivers WHERE name = %s", (driver_name,))
                driver_info = cursor.fetchone()
                if driver_info:
                    return driver_info
                else:
                    return "Driver not found."
        except Exception as e:
            return f"Error in retrieving driver info: {str(e)}"


    def remove_driver_by_name(self, driver_name):
        """Removes a driver from the system by their name."""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("DELETE FROM drivers WHERE name = %s RETURNING driver_id", (driver_name,))
                deleted_id = cursor.fetchone()
                self.conn.commit()
                if deleted_id:
                    return f"Driver {driver_name} (ID: {deleted_id[0]}) removed successfully."
                else:
                    return "Driver not found."
        except Exception as e:
            return f"Error in removing driver: {str(e)}"


    # Don't forget to close the connection when done
    def close_connection(self):
        if self.conn:
            self.conn.close()

# Example usage
if __name__ == "__main__":
    driver_manager = DriverManagement()  # No need to pass conn here

    # Example operations
    print(driver_manager.register_driver("John Doe", "DL12345", "555-1234", "johndoe@example.com"))
    print(driver_manager.retrieve_driver_info_by_name("John Doe"))
    print(driver_manager.remove_driver_by_name("John Doe"))
