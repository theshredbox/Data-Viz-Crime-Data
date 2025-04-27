import pandas as pd
import numpy as np

# --- Load dataset ---
file_path = r"C:\Users\Aryan\PycharmProjects\DataViz\crime_dataset.csv"  # adjust path if needed
df = pd.read_csv(file_path)

# --- STEP 1: Basic EDA ---
# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# View initial structure
print("\nData Sample:\n", df.head())

# --- STEP 2: Date-Time Enrichment ---
# Combine date and time into a single datetime column
df['datetime'] = pd.to_datetime(df['Date Occurred'] + ' ' + df['Time Occurred'], errors='coerce')

# Extract hour and weekday
df['hour'] = df['datetime'].dt.hour
df['weekday'] = df['datetime'].dt.day_name()

# Tag records as "Day" or "Night"
df['day_night'] = df['hour'].apply(lambda h: 'Night' if h < 6 or h >= 18 else 'Day')

# --- STEP 3: Crime Category Simplification ---
def categorize_crime(description):
    desc = description.lower()
    if "theft" in desc:
        return "Theft"
    elif "possession" in desc:
        return "Larceny"
    elif "assault" in desc or "battery" in desc or "intimidation" in desc:
        return "Assault"
    elif "rape" in desc or "sexual" in desc:
        return "Sexual Assault"
    elif "stalking" in desc:
        return "Stalking"
    elif "fraud" in desc:
        return "Fraud"
    elif "porn" in desc:
        return "Sexual Exploitation"
    elif "trespass" in desc:
        return "Trespassing"
    elif "odor" in desc:
        return "Larceny"
    elif "child" in desc and "porn" in desc:
        return "Sexual Exploitation"
    elif "leave" in desc or "scene" in desc or "behavior" in desc:
        return "Misdemeanor"
    else:
        return "Other"

df['crime_category'] = df['Description'].apply(categorize_crime)

# --- STEP 4: Cleaned Data Export ---
final_columns = [
    'Report ID', 'datetime', 'hour', 'weekday', 'day_night',
    'Crime Type', 'crime_category', 'Description', 'Status',
    'Location', 'Full Address', 'Latitude', 'Longitude'
]

df_cleaned = df[final_columns]

# Save to CSV
df_cleaned.to_csv("preprocessed_crime_dataset.csv", index=False)
print("\n✅ Preprocessing complete. Saved as 'preprocessed_crime_dataset.csv'")
