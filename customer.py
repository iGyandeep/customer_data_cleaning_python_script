import pandas as pd
import numpy as np
from datetime import date

def process_csv(input_file, output_file):
    df = pd.read_csv(input_file, dtype={"Customer_ID": str, "Mobile_No": str})
    
    required = [
        "Customer_ID", "First_Name", "Last_Name",
        "Mobile_No", "Date_of_Birth", "Address"
    ]
    if not set(required).issubset(df.columns):
        raise ValueError("Missing required columns")

    # Clean names
    for col in ["First_Name", "Last_Name"]:
        df[col] = df[col].fillna("").str.strip().str.title()

    df["Full_Name"] = (
        df["First_Name"] + " " + df["Last_Name"]
    ).str.strip()

    # Parse DOB and calculate age
    dob = pd.to_datetime(df["Date_of_Birth"], errors="coerce")
    today = date.today()
    df["Age"] = (
        today.year - dob.dt.year
        - ((dob.dt.month > today.month) |
           ((dob.dt.month == today.month) & (dob.dt.day > today.day)))
    )
    df.loc[dob.isna() | (dob.dt.date > today), "Age"] = np.nan

    # Extract Indian state from address
    states = [
        "Andhra Pradesh", "Bihar", "Delhi", "Goa", "Gujarat",
        "Haryana", "Karnataka", "Kerala", "Maharashtra",
        "Punjab", "Rajasthan", "Tamil Nadu", "Telangana",
        "Uttar Pradesh", "Uttarakhand", "West Bengal"
    ]

    def get_state(address):
        address = str(address)
        return next(
            (s for s in sorted(states, key=len, reverse=True)
             if s.lower() in address.lower()), ""
        )

    df["State"] = df["Address"].fillna("").apply(get_state)
    df["Date_of_Birth"] = dob.dt.strftime("%Y-%m-%d")

    # Select and export output columns
    columns = [
        "Customer_ID", "Full_Name", "Mobile_No",
        "Date_of_Birth", "Age", "Address", "State"
    ]
    df[columns].to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

process_csv("/content/customer.csv", "customers_cleaned.csv")
