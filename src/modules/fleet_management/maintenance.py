def schedule_maintenance(vehicle, date, service_type):
    """Schedules maintenance for a vehicle."""
    # Future Enhancement: Add maintenance record to a database
    return f"Scheduled {service_type} for {vehicle.display_info()} on {date}."
