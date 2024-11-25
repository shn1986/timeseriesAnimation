import pandas as pd
import numpy as np

# Read the raw data
df = pd.read_csv('./data/un-country-data.csv', low_memory=False)

# Filter for valid countries and select relevant columns
countries_df = df[df['ISO3_code'].notnull()]
columns = ['ISO3_code', 'Location', 'Time', 'TPopulation1Jan', 'TPopulation1July']
clean_df = countries_df[columns]

# Convert population values to 'in thousands'
clean_df['TPopulation1Jan'] = clean_df['TPopulation1Jan'] / 1000
clean_df['TPopulation1July'] = clean_df['TPopulation1July'] / 1000

# Function to expand data into monthly granularity
def expand_to_monthly(row):
    # Ensure no missing values for interpolation
    if pd.notnull(row['TPopulation1Jan']) and pd.notnull(row['TPopulation1July']):
        # Linear interpolation between January and July
        months = list(range(1, 13))  # 1 to 12 for months
        jan_to_jul = np.linspace(row['TPopulation1Jan'], row['TPopulation1July'], 7)  # Jan to July
        jul_to_dec = np.linspace(row['TPopulation1July'], row['TPopulation1Jan'], 6)[1:]  # July to Dec
        monthly_pop = np.concatenate([jan_to_jul, jul_to_dec])

        # Return expanded data as a list of dictionaries
        return [
            {
                'ISO3_code': row['ISO3_code'],
                'Location': row['Location'],
                'Time': row['Time'],
                'Month': month,
                'Population': pop,
            }
            for month, pop in zip(months, monthly_pop)
        ]
    else:
        return []

# Apply the expansion logic to each row
expanded_data = clean_df.apply(expand_to_monthly, axis=1)

# Flatten the nested list of dictionaries into a single DataFrame
expanded_df = pd.DataFrame([item for sublist in expanded_data for item in sublist])

# Save the expanded dataset to a new CSV file
expanded_df.to_csv('./data/cleaned-data-monthly.csv', index=False)

print("Monthly-level cleaned data saved to './data/cleaned-data-monthly.csv'")
