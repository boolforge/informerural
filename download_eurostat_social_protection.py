
import requests
import pandas as pd

def download_eurostat_data(dataset_code, filters=None):
    base_url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
    url = f"{base_url}{dataset_code}?format=JSON&lang=EN"
    
    if filters:
        filter_params = "&".join([f"{dim}={val}" for dim, val in filters.items()])
        url = f"{url}&{filter_params}"

    print(f"Downloading data from: {url}")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Eurostat API returns data in JSON-stat 2.0 format
        # This part needs careful parsing based on the actual JSON structure
        # For simplicity, let's assume a basic structure for now and refine if needed
        
        # Example of basic parsing (this will likely need adjustment)
        try:
            dimensions = data['dimension']
            id_vars = [dim for dim in dimensions.keys() if dim != 'value']
            
            # Extract data values and dimensions
            values = data['value']
            
            # Create a list of records
            records = []
            for i, val in enumerate(values):
                record = {'value': val}
                for dim_key, dim_data in dimensions.items():
                    if 'category' in dim_data and 'index' in dim_data['category']:
                        for category_key, category_index in dim_data['category']['index'].items():
                            if category_index == i:
                                record[dim_key] = category_key
                                break
                records.append(record)
            
            df = pd.DataFrame(records)
            return df
        except KeyError as e:
            print(f"Error parsing JSON: {e}. Full JSON response: {data}")
            return pd.DataFrame()

    else:
        print(f"Error downloading data: {response.status_code} - {response.text}")
        return pd.DataFrame()

# Example usage for the social protection dataset (tps00101)
dataset_code = "tps00101"
# You might need to find the exact dimension codes and values from Eurostat's data browser
# For example, to filter by 'geo' (country) and 'time' (year)
filters = {
    "geo": "ES", # Example: Spain
    "time": "2023" # Example: Year 2023
}

df = download_eurostat_data(dataset_code, filters)

if not df.empty:
    print("Data downloaded successfully:")
    print(df.head())
    df.to_csv("eurostat_social_protection_data.csv", index=False)
    print("Data saved to eurostat_social_protection_data.csv")
else:
    print("No data downloaded or DataFrame is empty.")



