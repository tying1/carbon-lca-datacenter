# src/ci_calculator.py

'''python

import pandas as pd

def load_data():
    # Example data structure — replace with real paths or actual files
    hardware_df = pd.read_csv('data/hardware_profiles.csv')
    emissions_df = pd.read_csv('data/emission_factors.csv')
    return hardware_df, emissions_df

def calculate_ci(hardware_df, emissions_df):
    # Merge emission factors with hardware data
    merged_df = pd.merge(hardware_df, emissions_df, on='hardware_type')

    # Calculate total lifecycle CI (example: manufacturing + operational + EOL)
    merged_df['total_CI'] = (
        merged_df['manufacturing_CI'] +
        merged_df['power_draw_W'] * merged_df['hours_per_year'] * merged_df['lifespan_years'] / 1000 * merged_df['grid_CI_kg_per_kWh'] +
        merged_df['EOL_CI']
    )

    return merged_df[['hardware_type', 'total_CI']]

def main():
    hardware_df, emissions_df = load_data()
    result_df = calculate_ci(hardware_df, emissions_df)
    print("Lifecycle CI Score by Hardware Type:\n")
    print(result_df)

if __name__ == "__main__":
    main()
'''
