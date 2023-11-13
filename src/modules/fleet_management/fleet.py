from vehicle import Vehicle
from maintenance import schedule_maintenance

class FleetManagement:
    def __init__(self):
        self.fleet = {}

    def add_vehicle(self, vehicle):
        """Adds a vehicle to the fleet."""
        if vehicle.vin in self.fleet:
            raise ValueError("A vehicle with this VIN already exists in the fleet.")
        self.fleet[vehicle.vin] = vehicle
        return f"Vehicle {vehicle.display_info()} added to fleet."

    def remove_vehicle(self, vin):
        """Removes a vehicle from the fleet."""
        if vin not in self.fleet:
            raise ValueError("Vehicle not found in fleet.")
        del self.fleet[vin]
        return f"Vehicle with VIN {vin} removed from fleet."

    def schedule_vehicle_maintenance(self, vin, date, service_type):
        """Schedules maintenance for a vehicle."""
        if vin not in self.fleet:
            raise ValueError("Vehicle not found in fleet.")
        return schedule_maintenance(self.fleet[vin], date, service_type)

    # More functions can be added here for editing vehicle details, tracking maintenance, etc.

# Example usage
fleet_manager = FleetManagement()
new_vehicle = Vehicle("Toyota", "Camry", 2022, "1234VIN")

try:
    print(fleet_manager.add_vehicle(new_vehicle))
    print(fleet_manager.schedule_vehicle_maintenance("1234VIN", "2023-01-01", "Oil Change"))
    # print(fleet_manager.remove_vehicle("1234VIN"))
except ValueError as e:
    print(e)
