
import pandas as pd
import os

# Define file paths
base_path = "C:\\Users\\file path"
file_paths = {
    'EmpMaster': os.path.join(base_path, 'EmpMaster.csv'),
    'nycpayroll_2020': os.path.join(base_path, 'nycpayroll_2020.csv'),
    'nycpayroll_2021': os.path.join(base_path, 'nycpayroll_2021.csv'),
    'AgencyMaster': os.path.join(base_path, 'AgencyMaster.csv'),
    'TitleMaster': os.path.join(base_path, 'TitleMaster.csv')
}

# Read CSV files into pandas DataFrames
dfs = {}
for file_name, file_path in file_paths.items():
    dfs[file_name] = pd.read_csv(file_path)

# Print the first few rows of each DataFrame to verify data loading
for file_name, df in dfs.items():
    print(f"First few rows of {file_name}:")
    print(df.head())

# Perform transformations
if 'EmpMaster' in dfs:
    emp_master_df = dfs['EmpMaster']
    emp_master_df = emp_master_df.rename(columns={'emp_id': 'EmployeeID', 'last_name': 'LastName', 'first_name': 'FirstName'})
    # Update the 'EmpMaster' DataFrame in the dictionary
    dfs['EmpMaster'] = emp_master_df

# Print the updated DataFrame to verify the transformation
print("Updated EmpMaster DataFrame:")
print(emp_master_df.head())

import cx_Oracle

def create_table(connection, table_name):
    # Define SQL queries to create tables if not exists
    create_table_queries = {
        'Employee': """
            CREATE TABLE Employee (
                EmployeeID INT PRIMARY KEY,
                LastName VARCHAR2(255),
                FirstName VARCHAR2(255)
            )
        """,
        'Agency': """
            CREATE TABLE Agency (
                AgencyID INT PRIMARY KEY,
                AgencyName VARCHAR2(255)
            )
        """,
        'Title': """
            CREATE TABLE Title (
                TitleCode VARCHAR2(255) PRIMARY KEY,
                TitleDescription VARCHAR2(255)
            )
        """,
        'DateDimension': """
            CREATE TABLE DateDimension (
                DateID INT PRIMARY KEY,
                TransactionDate DATE,
                Month INT,
                Year INT,
                Quarter INT
            )
        """,
        'PayrollTransactions': """
            CREATE TABLE PayrollTransactions (
                TransactionID INT PRIMARY KEY,
                EmployeeID INT,
                AgencyID INT,
                TitleCode VARCHAR2(255),
                DateID INT,
                FiscalYear INT,
                PayrollNumber INT,
                BaseSalary NUMBER(10, 2),
                PayBasis VARCHAR2(255),
                RegularHours NUMBER(10, 2),
                RegularGrossPaid NUMBER(10, 2),
                OTHours NUMBER(10, 2),
                TotalOTPaid NUMBER(10, 2),
                TotalOtherPay NUMBER(10, 2),
                CONSTRAINT fk_employee FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
                CONSTRAINT fk_agency FOREIGN KEY (AgencyID) REFERENCES Agency(AgencyID),
                CONSTRAINT fk_title FOREIGN KEY (TitleCode) REFERENCES Title(TitleCode),
                CONSTRAINT fk_date FOREIGN KEY (DateID) REFERENCES DateDimension(DateID)
            )
        """
    }
    
    try:
        # Execute the create table query
        with connection.cursor() as cursor:
            cursor.execute(create_table_queries[table_name])
        print(f"Table '{table_name}' created successfully.")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        # Check if the error is due to the table already existing
        if error.code == 955:
            print(f"Table '{table_name}' already exists.")
        else:
            # Re-raise the exception if it's not related to table existence
            raise
        def load_data_to_table(connection, table_name, df):
    # Load data into the table using pandas' to_sql method
    df.to_sql(table_name, connection, if_exists='replace', index=False)

def main():
    try:
        # Connect to Oracle Database
        connection = cx_Oracle.connect("username/password@hostname:port/service_name")

        # Define table names
        table_names = list(dfs.keys())  # Assuming table names are the same as the keys in dfs

        # Create tables (if not exists) and load data
        for table_name in table_names:
            if table_name in dfs:
                # Create table
                create_table(connection, table_name)
                # Load data into table
                load_data_to_table(connection, table_name, dfs[table_name])

        print("Data loaded into Oracle Database successfully.")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close connection
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    main()
