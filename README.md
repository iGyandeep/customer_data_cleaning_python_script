# customer_data_cleaning_python_script
Cleans customer data by standardizing names, generating full names, calculating ages from dates of birth, extracting Indian states from addresses, validating required columns, and exporting the processed data to a structured CSV file while preserving customer IDs and mobile numbers.

# --------------------------------------------

Build a CSV processing script that reads and analyses a CSV file containing customer records. The script should:

    Read and validate the CSV file.
    Standardise customer names into a consistent format (e.g., proper case for first and last names).
    Calculate each customer's age from the Date_of_birth field.
    Determine and extract the customer's state from the Address field.
    Generate an output CSV containing the cleaned and enriched data.

Input CSV columns:

    Customer_ID
    First_Name
    Last_Name
    Mobile_No
    Date_of_Birth
    Address

Expected output CSV columns:

    Customer_ID
    Full_Name (properly formatted)
    Mobile_No
    Date_of_Birth
    Age
    Address
    State

The script should handle missing, invalid, or inconsistent data gracefully and provide appropriate validation and error reporting.
