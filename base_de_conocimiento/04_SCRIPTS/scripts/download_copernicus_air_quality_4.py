import cdsapi
import os
import pandas as pd
import xarray as xr

# This script is designed to download air quality data from the Copernicus ADS.
# It has been repaired and is being optimized based on user feedback.

def download_air_quality_data(year, month, variables, area, output_filename):
    """
    Downloads CAMS European air quality reanalysis data for a specific month.
    """
    c = cdsapi.Client()

    request = {
        'variable': variables,
        'year': str(year),
        'month': f"{month:02d}",
        'format': 'netcdf',
        'area': area,
        'type': 'validated_reanalysis',
    }

    print(f"Attempting to download data for {year}-{month:02d} with request: {request}")

    try:
        c.retrieve(
            'cams-europe-air-quality-reanalyses',
            request,
            output_filename
        )
        print(f"Successfully downloaded {output_filename}")
        return True
    except Exception as e:
        print(f"Error downloading data for {year}-{month:02d}: {e}")
        return False

def main():
    """
    Main function to test the download for a single month.
    """
    # --- Parameters for the test download ---
    # Using the exact parameters from the user's working example.
    TEST_YEAR = 2022
    TEST_MONTH = 1
    TEST_VARIABLES = [
        'dust', 'nitrogen_dioxide', 'ozone',
        'particulate_matter_10um', 'particulate_matter_2.5um', 'sulphur_dioxide',
    ]
    TEST_AREA = [44.2, -10, 35, 5]
    OUTPUT_FILENAME = f"cams_air_quality_{TEST_YEAR}_{TEST_MONTH:02d}.nc"

    # --- Execute the download ---
    success = download_air_quality_data(
        year=TEST_YEAR,
        month=TEST_MONTH,
        variables=TEST_VARIABLES,
        area=TEST_AREA,
        output_filename=OUTPUT_FILENAME
    )

    if success:
        # --- Basic verification ---
        try:
            print(f"\nVerifying downloaded file: {OUTPUT_FILENAME}")
            ds = xr.open_dataset(OUTPUT_FILENAME)
            print("Dataset opened successfully.")
            print("First 5 rows of the DataFrame:")
            df = ds.to_dataframe()
            print(df.head().to_markdown(index=True, numalign="left", stralign="left"))
            os.remove(OUTPUT_FILENAME)
            print(f"Cleaned up test file: {OUTPUT_FILENAME}")
        except Exception as e:
            print(f"Error verifying or processing the downloaded file: {e}")

if __name__ == "__main__":
    main()
