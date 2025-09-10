import cdsapi
import os
import argparse
import calendar
import xarray as xr
import pandas as pd
import shutil
import geonamescache
from pygadm import Items
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import zipfile

# --- User-ordered Credentials ---
GEONAMES_USERNAME = "jfcarrb"

def get_bounding_box(country=None, region=None, placename=None, bbox_str=None):
    """Determines the bounding box from various location inputs."""
    if bbox_str:
        try:
            coords = [float(x.strip()) for x in bbox_str.split(',')]
            if len(coords) != 4: raise ValueError
            return coords, (bbox_str)
        except (ValueError, IndexError):
            print("Error: Bounding box must be four comma-separated numbers: N,W,S,E")
            return None, None

    if country:
        try:
            area_name = region if region else country
            print(f"Using pygadm to find bounding box for '{area_name}'...")
            # Corrected pygadm usage based on latest deprecation warning
            gdf = Items(name=area_name)

            if gdf is None or gdf.empty:
                raise ValueError(f"Could not find administrative area.")

            bounds = gdf.total_bounds
            return [bounds[3], bounds[0], bounds[1], bounds[2]], area_name
        except Exception as e:
            print(f"Error getting bounds from GADM for '{area_name}': {e}")
            return None, None

    if placename:
        print(f"Using geocoders to find coordinates for '{placename}'...")
        try:
            gc = geonamescache.GeonamesCache()
            cities = gc.search_cities(placename)
            if cities:
                city = cities[0]
                lat, lon = city['latitude'], city['longitude']
                print(f"Found '{city['name']}' via geonamescache.")
                return [lat + 0.5, lon - 0.5, lat - 0.5, lon + 0.5], placename
        except Exception as e:
            print(f"Geonamescache search failed: {e}. Falling back to Nominatim.")
        try:
            geolocator = Nominatim(user_agent=f"jules_downloader_{GEONAMES_USERNAME}")
            location = geolocator.geocode(placename, timeout=10)
            if location and location.raw.get('importance', 0) > 0.1:
                print(f"Found '{location.address}' via Nominatim.")
                bbox = [float(x) for x in location.raw['boundingbox']]
                return [bbox[1], bbox[2], bbox[0], bbox[3]], placename
        except (GeocoderTimedOut, GeocoderUnavailable):
            print("Nominatim service timed out or is unavailable.")
        except Exception as e:
            print(f"Nominatim geocoding failed: {e}")
    return None, None

def download_monthly_data(year, month, area, output_dir):
    """Downloads ERA5-Land hourly data for a specific month and area."""
    os.makedirs(output_dir, exist_ok=True)
    _, num_days = calendar.monthrange(year, month)
    temp_download_path = os.path.join(output_dir, f"temp_download")
    final_grib_path = os.path.join(output_dir, f"era5_land_{year}_{month:02d}.grib")

    c = cdsapi.Client()
    days = [f"{day:02d}" for day in range(1, num_days + 1)]
    times = [f"{hour:02d}:00" for hour in range(24)]
    request = {
        'product_type': 'reanalysis', 'format': 'grib',
        'variable': ['2m_dewpoint_temperature', '2m_temperature', 'relative_humidity'],
        'year': str(year), 'month': f"{month:02d}",
        'day': days, 'time': times, 'area': area,
    }

    print(f"Attempting download for {year}-{month:02d} | Area: {area}")
    try:
        c.retrieve('reanalysis-era5-land', request, temp_download_path)

        if zipfile.is_zipfile(temp_download_path):
            print("Downloaded file is a ZIP, which indicates a server-side error.")
            with zipfile.ZipFile(temp_download_path, 'r') as zip_ref:
                for a_file in zip_ref.infolist():
                    print(f"--- Contents of {a_file.filename} in error ZIP ---")
                    print(zip_ref.read(a_file.filename).decode('utf-8', 'ignore'))
            os.remove(temp_download_path)
            return False

        os.rename(temp_download_path, final_grib_path)
        print(f"Successfully downloaded {final_grib_path}")
        return True
    except Exception as e:
        print(f"ERROR: Download failed for {year}-{month:02d}. Reason: {e}")
        return False

def process_yearly_data(temp_dir, year, final_output_dir, area_name):
    """Processes all monthly GRIB files for a year into a single CSV file."""
    print(f"\nStarting post-processing for year {year}...")
    os.makedirs(final_output_dir, exist_ok=True)

    grib_files = sorted([os.path.join(temp_dir, f) for f in os.listdir(temp_dir) if f.endswith('.grib')])
    if not grib_files:
        print("No GRIB files found to process.")
        return

    try:
        print(f"Combining {len(grib_files)} GRIB files...")
        ds = xr.open_mfdataset(grib_files, engine='cfgrib')
        print("Converting to DataFrame...")
        df = ds.to_dataframe()
        df.reset_index(inplace=True)

        safe_area_name = "".join(x for x in area_name if x.isalnum() or x in " _-").rstrip().replace(" ", "_")
        final_csv_path = os.path.join(final_output_dir, f"era5_land_meteo_{safe_area_name}_{year}.csv")
        print(f"Saving final CSV to {final_csv_path}...")
        df.to_csv(final_csv_path, index=False)
        print("Successfully saved CSV.")

        print(f"Cleaning up temporary directory: {temp_dir}")
        shutil.rmtree(temp_dir)
        print("Cleanup complete.")
    except Exception as e:
        print(f"An error occurred during post-processing: {e}")

def main():
    """Main function to orchestrate the download and processing workflow."""
    parser = argparse.ArgumentParser(description="Download and process ERA5-Land meteorological data.")
    parser.add_argument("--year", type=int, required=True, help="Year for data download.")
    parser.add_argument("--temp-dir", type=str, default="temp_meteo_data", help="Temporary directory for monthly files.")
    parser.add_argument("--final-dir", type=str, default="base_de_conocimiento/03_DATOS/datos/crudos/", help="Final output directory for the yearly CSV.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--country", type=str, help="Country name for administrative boundaries. Use with --region for specifics.")
    group.add_argument("--placename", type=str, help="Specific place name to search (e.g., 'Soria, Spain').")
    group.add_argument("--bbox", type=str, help="Explicit bounding box [N,W,S,E] as comma-separated string.")

    parser.add_argument("--region", type=str, help="Region/state within a country (requires --country).")

    args = parser.parse_args()

    if args.region and not args.country:
        parser.error("--region requires --country.")

    target_area, area_name_for_file = get_bounding_box(country=args.country, region=args.region, placename=args.placename, bbox_str=args.bbox)
    if not target_area:
        print("Could not determine a valid target area. Exiting.")
        return

    for month in range(1, 2): # Test loop for 1 month
        if not download_monthly_data(args.year, month, target_area, args.temp_dir):
            print(f"Stopping download process due to failure.")
            break
    else:
        print(f"\nAll monthly downloads for {args.year} seem to be complete.")
        process_yearly_data(args.temp_dir, args.year, args.final_dir, area_name_for_file)

if __name__ == "__main__":
    main()
