# TESTED AND WORKING FINE!


import psycopg2
from psycopg2 import OperationalError

#Create a DATABASE
def create_connection():
        """Create a database connection to the PostgreSQL database."""
        try:
            conn = psycopg2.connect(
                database="axleaxis_db",
                user="osmanileon92",
                password="Alessgiugu22",
                host="127.0.0.1",
                port="5432"
            )
            return conn
        except OperationalError as e:
            print(f"The error '{e}' occurred")
            return None

#Create Tables in the DATABSAE
def create_table(conn, create_table_sql):
        """Create a table from the create_table_sql statement."""
        try:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
            conn.commit()
        except OperationalError as e:
            print(f"The error '{e}' occurred")


def create_vehicles_table(conn):
    """Create the vehicles table and confirm creation."""
    create_table_vehicles = """
    CREATE TABLE IF NOT EXISTS vehicles (
        vin VARCHAR(50) PRIMARY KEY,
        make VARCHAR(100) NOT NULL,
        model VARCHAR(100) NOT NULL,
        year INT NOT NULL
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_vehicles)
        conn.commit()
        print("Vehicles table created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"Error creating vehicles table: {e}")
        conn.rollback()

def create_maintenance_table(conn):
    """Create the maintenance table and confirm creation."""
    create_table_maintenance = """
    CREATE TABLE IF NOT EXISTS maintenance (
        id SERIAL PRIMARY KEY,
        vin VARCHAR(50) NOT NULL REFERENCES vehicles(vin),
        date DATE NOT NULL,
        service_type VARCHAR(100) NOT NULL
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_maintenance)
        conn.commit()
        print("Maintenance table created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"Error creating maintenance table: {e}")
        conn.rollback()

def create_driver_table(conn):
    """Create the drivers table and confirm creation."""
    create_table_drivers = """
    CREATE TABLE IF NOT EXISTS drivers (
        driver_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        license_number VARCHAR(50) UNIQUE NOT NULL,
        phone_number VARCHAR(15),
        email VARCHAR(100)
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_drivers)
        conn.commit()
        print("Drivers table created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"Error creating drivers table: {e}")
        conn.rollback()
       
def create_financial_table(conn):
    """Create the financial_records table and confirm creation."""
    create_table_financials = """
    CREATE TABLE IF NOT EXISTS financial_records (
        record_id SERIAL PRIMARY KEY,
        date DATE NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        description TEXT,
        category VARCHAR(100)
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_financials)
        conn.commit()
        print("Financial records table created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"Error creating financial records table: {e}")
        conn.rollback()


def create_pdf_table(conn):
    """Create the PDF documents table and confirm creation."""
    create_table_pdf = """
    CREATE TABLE IF NOT EXISTS pdf_documents (
        document_id SERIAL PRIMARY KEY,
        filename VARCHAR(255) NOT NULL,
        created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_updated TIMESTAMP
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_pdf)
        conn.commit()
        print("PDF documents table created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"Error creating PDF documents table: {e}")
        conn.rollback()


def create_reports_table(conn):
    """Create the reports table and confirm creation."""
    create_table_reports = """
    CREATE TABLE IF NOT EXISTS reports (
        report_id SERIAL PRIMARY KEY,
        report_name VARCHAR(100) NOT NULL,
        generated_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        report_data TEXT
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_reports)
        conn.commit()
        print("Reports table created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"Error creating reports table: {e}")
        conn.rollback()


def create_users_table(conn):
    """Create the users table and confirm creation."""
    create_table_users = """
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        email VARCHAR(100),
        role VARCHAR(50),
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_users)
        conn.commit()
        print("Users table created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"Error creating users table: {e}")
        conn.rollback()


def create_freight_brokers_table(conn):
    """Create the freight brokers table and confirm creation."""
    create_table_freight_brokers = """
    CREATE TABLE IF NOT EXISTS freight_brokers (
        broker_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        contact_info TEXT,
        address TEXT
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_freight_brokers)
        conn.commit()
        print("Freight brokers table created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"Error creating freight brokers table: {e}")
        conn.rollback()



def create_factoring_companies_table(conn):
    """Create the factoring companies table and confirm creation."""
    create_table_factoring_companies = """
    CREATE TABLE IF NOT EXISTS factoring_companies (
        company_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        contact_info TEXT,
        address TEXT,
        charge_percentage DECIMAL(5, 2)
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_factoring_companies)
        conn.commit()
        print("Factoring companies table created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"Error creating factoring companies table: {e}")
        conn.rollback()


def create_loads_table(conn):
    """Create the loads table and confirm creation."""
    create_table_loads = """
    CREATE TABLE IF NOT EXISTS loads (
        load_id SERIAL PRIMARY KEY,
        description TEXT,
        origin VARCHAR(255),
        destination VARCHAR(255),
        vehicle_vin VARCHAR(50) REFERENCES vehicles(vin),
        driver_id INT REFERENCES drivers(driver_id),
        broker_id INT REFERENCES freight_brokers(broker_id),
        company_id INT REFERENCES factoring_companies(company_id),
        status VARCHAR(50),
        pickup_date DATE,
        delivery_date DATE
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_loads)
        conn.commit()
        print("Loads table created successfully.")
    except psycopg2.DatabaseError as e:
        print(f"Error creating loads table: {e}")
        conn.rollback()



def initialize_db():
        """Initialize the database by creating required tables."""
        conn = create_connection()
        if conn is not None:
            create_vehicles_table(conn)
            create_maintenance_table(conn)
            create_driver_table(conn)
            create_financial_table(conn)
            create_pdf_table(conn)
            create_reports_table(conn)
            create_users_table(conn)
            create_freight_brokers_table(conn)
            create_factoring_companies_table(conn)
            create_loads_table(conn)
            # ... (any other table creation calls)
            conn.close()
        else:
            print("Error! Cannot create the database connection.")



# CRUD operations for vehicles
def add_or_update_vehicle(conn, vin, make, model, year):
    """Add a new vehicle or update the existing vehicle in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO vehicles (vin, make, model, year)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (vin) DO UPDATE
                SET make = EXCLUDED.make, model = EXCLUDED.model, year = EXCLUDED.year
            """, (vin, make, model, year))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def get_vehicle(conn, vin):
    """Retrieve a vehicle from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vehicles WHERE vin = %s", (vin,))
            return cursor.fetchone()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")

def delete_vehicle(conn, vin):
    """Delete a vehicle from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM vehicles WHERE vin = %s", (vin,))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def get_all_vehicles(conn):
    """Retrieve all vehicles from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vehicles")
            return cursor.fetchall()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        return []




# CRUD operations for maintenance records
def vehicle_exists(conn, vin):
    """Check if a vehicle with the given VIN exists."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 FROM vehicles WHERE vin = %s", (vin,))
            return cursor.fetchone() is not None
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")

def add_maintenance(conn, vin, date, service_type):
    """Add a maintenance record to the database if the vehicle exists."""
    if vehicle_exists(conn, vin):
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO maintenance (vin, date, service_type) VALUES (%s, %s, %s)",
                    (vin, date, service_type)
                )
                conn.commit()
        except psycopg2.errors.DatabaseError as e:
            print(f"Database error: {e}")
            conn.rollback()
    else:
        print(f"No vehicle found with VIN: {vin}")



def get_maintenance(conn, maintenance_id):
    """Retrieve a maintenance record from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM maintenance WHERE id = %s", (maintenance_id,))
            return cursor.fetchone()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")

def update_maintenance(conn, maintenance_id, date, service_type):
    """Update a maintenance record in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE maintenance SET date = %s, service_type = %s WHERE id = %s",
                (date, service_type, maintenance_id)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def delete_maintenance(conn, maintenance_id):
    """Delete a maintenance record from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM maintenance WHERE id = %s", (maintenance_id,))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()



# CRUD operations for drivers
def add_or_update_driver(conn, name, license_number, phone_number, email):
    """Add a new driver or update the existing driver in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO drivers (name, license_number, phone_number, email)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (license_number) DO UPDATE
                SET name = EXCLUDED.name, phone_number = EXCLUDED.phone_number, email = EXCLUDED.email
            """, (name, license_number, phone_number, email))
            conn.commit()
    except errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def get_driver(conn, driver_id):
    """Retrieve a driver from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM drivers WHERE driver_id = %s", (driver_id,))
            return cursor.fetchone()
    except errors.DatabaseError as e:
        print(f"Database error: {e}")

def delete_driver(conn, driver_id):
    """Delete a driver from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM drivers WHERE driver_id = %s", (driver_id,))
            conn.commit()
    except errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()
def delete_driver(conn, driver_id):
        """Delete a driver from the database."""
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM drivers WHERE driver_id = %s", (driver_id,))
            conn.commit()



# CRUD operations for financial records
def add_financial_record(conn, date, amount, description, category):
    """Add a financial record to the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO financial_records (date, amount, description, category) VALUES (%s, %s, %s, %s)",
                (date, amount, description, category)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()


def get_financial_record(conn, record_id):
    """Retrieve a financial record from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM financial_records WHERE record_id = %s", (record_id,))
            return cursor.fetchone()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")

def update_financial_record(conn, record_id, date, amount, description, category):
    """Update a financial record in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE financial_records SET date = %s, amount = %s, description = %s, category = %s WHERE record_id = %s",
                (date, amount, description, category, record_id)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def delete_financial_record(conn, record_id):
    """Delete a financial record from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM financial_records WHERE record_id = %s", (record_id,))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()



# CRUD operations for Loads
def add_load(conn, description, origin, destination, vehicle_vin, driver_id, broker_id, company_id, status, pickup_date, delivery_date):
    """Add a load to the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO loads (description, origin, destination, vehicle_vin, driver_id, broker_id, company_id, status, pickup_date, delivery_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (description, origin, destination, vehicle_vin, driver_id, broker_id, company_id, status, pickup_date, delivery_date)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()


def get_load(conn, load_id):
    """Retrieve a load from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM loads WHERE load_id = %s", (load_id,))
            return cursor.fetchone()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")


def update_load(conn, load_id, description, origin, destination, vehicle_vin, driver_id, broker_id, company_id, status, pickup_date, delivery_date):
    """Update a load in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE loads SET description = %s, origin = %s, destination = %s, vehicle_vin = %s, driver_id = %s, broker_id = %s, company_id = %s, status = %s, pickup_date = %s, delivery_date = %s WHERE load_id = %s",
                (description, origin, destination, vehicle_vin, driver_id, broker_id, company_id, status, pickup_date, delivery_date, load_id)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()


def delete_load(conn, load_id):
    """Delete a load from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM loads WHERE load_id = %s", (load_id,))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()



# CRUD Operations for Freight Brokers
def add_freight_broker(conn, name, contact_info, address):
    """Add a freight broker to the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO freight_brokers (name, contact_info, address) VALUES (%s, %s, %s)",
                (name, contact_info, address)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()


def get_freight_broker(conn, broker_id):
    """Retrieve a freight broker from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM freight_brokers WHERE broker_id = %s", (broker_id,))
            return cursor.fetchone()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")

def update_freight_broker(conn, broker_id, name, contact_info, address):
    """Update a freight broker in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE freight_brokers SET name = %s, contact_info = %s, address = %s WHERE broker_id = %s",
                (name, contact_info, address, broker_id)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def delete_freight_broker(conn, broker_id):
    """Delete a freight broker from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM freight_brokers WHERE broker_id = %s", (broker_id,))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()



# CRUD Operations for Factoring Companies
def add_factoring_company(conn, name, contact_info, address, charge_percentage):
    """Add a factoring company to the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO factoring_companies (name, contact_info, address, charge_percentage) VALUES (%s, %s, %s, %s)",
                (name, contact_info, address, charge_percentage)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()


def get_factoring_company(conn, company_id):
    """Retrieve a factoring company from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM factoring_companies WHERE company_id = %s", (company_id,))
            return cursor.fetchone()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")

def update_factoring_company(conn, company_id, name, contact_info, address, charge_percentage):
    """Update a factoring company in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE factoring_companies SET name = %s, contact_info = %s, address = %s, charge_percentage = %s WHERE company_id = %s",
                (name, contact_info, address, charge_percentage, company_id)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def delete_factoring_company(conn, company_id):
    """Delete a factoring company from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM factoring_companies WHERE company_id = %s", (company_id,))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()



# CRUD operations for PDF documents
def add_pdf_document(conn, filename):
    """Add a PDF document to the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO pdf_documents (filename) VALUES (%s)",
                (filename,)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def get_pdf_document(conn, document_id):
    """Retrieve a PDF document from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pdf_documents WHERE document_id = %s", (document_id,))
            return cursor.fetchone()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")

def update_pdf_document(conn, document_id, new_filename):
    """Update a PDF document in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE pdf_documents SET filename = %s, last_updated = NOW() WHERE document_id = %s",
                (new_filename, document_id)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def delete_pdf_document(conn, document_id):
    """Delete a PDF document from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM pdf_documents WHERE document_id = %s", (document_id,))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()


# CRUD operations for reports
def add_report(conn, report_name, report_data):
    """Add a report to the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO reports (report_name, report_data) VALUES (%s, %s)",
                (report_name, report_data)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def get_report(conn, report_id):
    """Retrieve a report from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM reports WHERE report_id = %s", (report_id,))
            return cursor.fetchone()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")

def update_report(conn, report_id, new_report_name, new_report_data):
    """Update a report in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE reports SET report_name = %s, report_data = %s WHERE report_id = %s",
                (new_report_name, new_report_data, report_id)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def delete_report(conn, report_id):
    """Delete a report from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM reports WHERE report_id = %s", (report_id,))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()


# CRUD operations for Users
def add_or_update_user(conn, username, password_hash, email, role):
    """Add a new user or update the existing user in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO users (username, password_hash, email, role)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (username) DO UPDATE SET
                password_hash = EXCLUDED.password_hash,
                email = EXCLUDED.email,
                role = EXCLUDED.role
            """, (username, password_hash, email, role))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def get_user(conn, user_id):
    """Retrieve a user from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            return cursor.fetchone()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")

def update_user(conn, user_id, new_username, new_password_hash, new_email, new_role):
    """Update a user in the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET username = %s, password_hash = %s, email = %s, role = %s WHERE user_id = %s",
                (new_username, new_password_hash, new_email, new_role, user_id)
            )
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

def delete_user(conn, user_id):
    """Delete a user from the database."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            conn.commit()
    except psycopg2.errors.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()




# Example usage
if __name__ == "__main__":
        # Initialize database
        initialize_db()

        # Example to add and manage a Vehicle
        conn = create_connection()
        if conn is not None:
            # Add or update a vehicle
            add_or_update_vehicle(conn, "VIN123", "Toyota", "Camry", 2022)
            
            # Get a vehicle
            vehicle = get_vehicle(conn, "VIN123")
            if vehicle:
                print("Retrieved Vehicle:", vehicle)
            
            # Delete a vehicle
            delete_vehicle(conn, "VIN123")

            conn.close()

        # Example to add and manage a Financial record
        conn = create_connection()
        if conn is not None:
            # Add a financial record
            add_financial_record(conn, "2023-01-01", 1000.00, "Sample Transaction", "Expense")
            
            # Get a financial record
            record = get_financial_record(conn, 1)  # Assuming the record_id is 1
            if record:
                print("Retrieved Financial Record:", record)
            
            # Update a financial record
            update_financial_record(conn, 1, "2023-01-02", 1500.00, "Updated Transaction", "Income")
            
            # Delete a financial record
            delete_financial_record(conn, 1)

            conn.close()

        # Example to add and manage a Driver
        conn = create_connection()
        if conn is not None:
            # Add or update a driver
            add_or_update_driver(conn, "John Doe", "DL12345", "555-1234", "johndoe@email.com")
            
            # Get a driver
            driver = get_driver(conn, 1)  # Assuming the driver_id is 1
            if driver:
                print("Retrieved Driver:", driver)
        
            # Delete a driver
            delete_driver(conn, 1)  # Assuming the driver_id is 1

            conn.close()

        # Example to add and manage a Maintenance Record
        conn = create_connection()
        if conn is not None:
            # Add a maintenance record
            add_maintenance(conn, "VIN123", "2023-01-01", "Oil Change")
            
            # Get a maintenance record
            maintenance = get_maintenance(conn, 1)  # Assuming the maintenance_id is 1
            if maintenance:
                print("Retrieved Maintenance Record:", maintenance)
            
            # Update a maintenance record
            update_maintenance(conn, 1, "2023-01-02", "Tire Replacement")
            
            # Delete a maintenance record
            delete_maintenance(conn, 1)

            conn.close()

        # Example to add and manage a Freight Broker
        conn = create_connection()
        if conn is not None:
            # Add a freight broker
            add_freight_broker(conn, "Broker A", "contact@brokera.com", "123 Broker Lane")
            
            # Get a freight broker
            broker = get_freight_broker(conn, 1)  # Assuming the broker_id is 1
            if broker:
                print("Retrieved Freight Broker:", broker)
            
            # Update a freight broker
            update_freight_broker(conn, 1, "Broker B", "newcontact@brokerb.com", "456 Broker Avenue")
            
            # Delete a freight broker
            delete_freight_broker(conn, 1)

            conn.close()

        # Example to add and manage a Factoring Company
        conn = create_connection()
        if conn is not None:
            # Add a factoring company
            add_factoring_company(conn, "Factoring Company A", "contact@companya.com", "123 Finance Street", 5.0)
            
            # Get a factoring company
            company = get_factoring_company(conn, 1)  # Assuming the company_id is 1
            if company:
                print("Retrieved Factoring Company:", company)
            
            # Update a factoring company
            update_factoring_company(conn, 1, "Factoring Company B", "newcontact@companyb.com", "456 Finance Avenue", 4.5)
            
            # Delete a factoring company
            delete_factoring_company(conn, 1)

            conn.close()

        # Example to add and manage to Add a Load
        conn = create_connection()
        if conn is not None:
            # Add a load
            add_load(conn, "Cargo", "City A", "City B", "VIN123", 1, 2, 3, "Scheduled", 2023-8-1, 2023-8-2)
            
            # Get a load
            load = get_load(conn, 1)  # Assuming the load_id is 1
            if load:
                print("Retrieved Load:", load)
            
            # Update a load
            update_load(conn, 1, "Cargo Updated", "City C", "City D", "VIN124", 2, 2, 2, "In Transit", "2023-01-02", "2023-01-06")
            
            # Delete a load
            delete_load(conn, 1)

            conn.close()

        # Example to add and manage a PDF Document
        conn = create_connection()
        if conn is not None:
            # Add a PDF document
            add_pdf_document(conn, "example_document.pdf")
            
            # Get a PDF document
            document = get_pdf_document(conn, 1)  # Assuming the document_id is 1
            if document:
                print("Retrieved PDF Document:", document)
            
            # Update a PDF Document
            update_pdf_document(conn, 1, "updated_document.pdf")
            
            # Delete a PDF document
            delete_pdf_document(conn, 1)

            conn.close()

        # Example to add and manage a Report
        conn = create_connection()
        if conn is not None:
            # Add a report
            add_report(conn, "Monthly Sales", "Data about monthly sales...")
            
            # Get a report
            report = get_report(conn, 1)  # Assuming the report_id is 1
            if report:
                print("Retrieved Report:", report)
            
            # Update a report
            update_report(conn, 1, "Monthly Sales Updated", "Updated data about monthly sales...")
            
            # Delete a report
            delete_report(conn, 1)

            conn.close()

        # Example to add and manage Users
        conn = create_connection()
        if conn is not None:
            # Add a user
            add_or_update_user(conn, "john_doe", "hashed_password", "johndoe@example.com", "admin")
            
            # Get a user
            user = get_user(conn, 1)  # Assuming the user_id is 1
            if user:
                print("Retrieved User:", user)
            
            # Update a user
            update_user(conn, 1, "john_doe_updated", "new_hashed_password", "johnupdated@example.com", "user")
            
            # Delete a user
            delete_user(conn, 1)

            conn.close()

        # Example usage
        conn = create_connection()
        if conn is not None:
            vin = "VIN123"
            if vehicle_exists(conn, vin):
                # Add maintenance record for this vehicle
                add_maintenance(conn, vin, "2023-01-01", "Oil Change")
            else:
                print(f"No vehicle found with VIN: {vin}")
            conn.close()