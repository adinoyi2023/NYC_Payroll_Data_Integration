NYC Payroll Data Integration
Overview
The NYC Payroll Data Integration project aims to integrate payroll data across all agencies of the City of New York. The project involves the development of a Data Analytics platform to analyze financial resource allocation and enhance transparency/public accessibility of payroll data for municipal employees.

Table of Contents
Overview
Project Scope
Data Warehouse Design
ETL Pipeline Development
Data Quality Assurance
User Access Control
Documentation and Version Control
Cloud-Hosted Repository
Installation
Usage
Contributing
License
Project Scope
The project encompasses the following key components:

Designing a Data Warehouse for NYC
Developing a scalable and automated ETL Pipeline
Ensuring data quality and consistency
Creating a public user with limited privileges
Documenting processes for reproducibility
Maintaining a cloud-hosted repository of the codebase
Data Warehouse Design
The data warehouse includes the following tables:

Employee
Agency
Title
DateDimension
PayrollTransactions
ETL Pipeline Development
The ETL (Extract, Transform, Load) pipeline is implemented in Python using pandas for data manipulation and cx_Oracle for database interaction. It automates the extraction, transformation, and loading of CSV data into Oracle database tables.

Data Quality Assurance
Data quality checks are implemented to ensure the integrity and quality of the data. Error handling mechanisms are in place to handle exceptions during the ETL process.

User Access Control
User access control is established in the Oracle Database, with roles and privileges defined for different types of users. A public user role with restricted access is created to enable public access to certain datasets while ensuring data security.

Documentation and Version Control
Thorough documentation of the ETL process, schema design, and pipeline architecture is maintained for reproducibility. Version control is managed using Git, with a README file providing setup and usage instructions.

Cloud-Hosted Repository
The codebase is hosted on GitHub, facilitating collaboration and version control. The repository includes separate directories for code, documentation, and resources.

Installation
To run the project locally, ensure you have Python and cx_Oracle installed. Clone the repository to your local machine and set up the necessary environment variables for database connection.

Usage
Follow the instructions in the README file to set up the project and run the ETL pipeline. Use the provided scripts and documentation for reference.

Contributing
Contributions to the project are welcome! Fork the repository, make your changes, and submit a pull request for review.

License
This project is licensed under the MIT License.