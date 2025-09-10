import cdsapi
import pygadm
from geopy.geocoders import Nominatim
import geonamescache
import argparse
import os

def get_bounding_box_from_placename(placename):
    """
    Get the bounding box of a placename using geonamescache and geopy.
    """
    # First, try geonamescache
    gc = geonamescache.GeonamesCache()
    cities = gc.get_cities_by_name(placename)
    if cities:
        # Take the first result
        city_info = cities[0]
        city = list(city_info.values())[0]
        lat = float(city['latitude'])
        lon = float(city['longitude'])
        return lat, lon, lat, lon

    # If not found, fall back to geopy
    geolocator = Nominatim(user_agent="meteo_downloader")
    try:
        location = geolocator.geocode(placename)
        if location:
            return location.latitude, location.longitude, location.latitude, location.longitude
        else:
            return None
    except Exception as e:
        print(f"Error with geopy: {e}")
        return None

def get_bounding_box_from_admin_area(country, area_name):
    """
    Get the bounding box of an administrative area using pygadm.
    """
    try:
        # First, try to get the area directly, and filter by country.
        items = pygadm.Items(name=area_name)
        country_items = items[items['NAME_0'] == country]

        if not country_items.empty:
            shape = country_items.iloc[0].geometry
            return shape.bounds

        # If not found, get all areas of the country and search within them.
        # This is useful for level 1 areas like "Toscana".
        country_gdf = pygadm.Items(name=country, content_level=1)
        area = country_gdf[country_gdf['NAME_1'] == area_name]
        if not area.empty:
            shape = area.iloc[0].geometry
            return shape.bounds

        return None

    except Exception as e:
        print(f"Error with pygadm: {e}")
        return None

def download_data(year, month, day, time, area, output_format, variable, product_type):
    """
    Download data from Copernicus.
    """
    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': product_type,
            'variable': variable,
            'year': year,
            'month': month,
            'day': day,
            'time': time,
            'area': area,
            'format': output_format,
        },
        f'download.{output_format}')

def main():
    parser = argparse.ArgumentParser(description="Download Copernicus ERA5 data for a specific location.")
    parser.add_argument('--location_type', choices=['placename', 'admin_area'], required=True, help="Type of location to use.")
    parser.add_argument('--location_name', required=True, help="Name of the placename or administrative area.")
    parser.add_argument('--country', help="Country for administrative area (required if location_type is admin_area).")
    parser.add_argument('--year', required=True, help="Year of the data.")
    parser.add_argument('--month', required=True, help="Month of the data.")
    parser.add_argument('--day', required=True, help="Day of the data.")
    parser.add_argument('--time', default='12:00', help="Time of the data (e.g., 12:00).")
    parser.add_argument('--format', default='netcdf', choices=['netcdf', 'grib'], help="Output format.")
    parser.add_argument('--variable', default='2m_temperature', help="Variable to download.")
    parser.add_argument('--product_type', default='reanalysis', help="Product type.")

    args = parser.parse_args()

    bounding_box = None
    if args.location_type == 'placename':
        lat_lon = get_bounding_box_from_placename(args.location_name)
        if lat_lon:
            lat, lon, _, _ = lat_lon
            bounding_box = [lat + 0.25, lon - 0.25, lat - 0.25, lon + 0.25] # North, West, South, East
    elif args.location_type == 'admin_area':
        if not args.country:
            print("Error: --country is required for admin_area location type.")
            return
        bounds = get_bounding_box_from_admin_area(args.country, args.location_name)
        if bounds:
            min_lon, min_lat, max_lon, max_lat = bounds
            bounding_box = [max_lat, min_lon, min_lat, max_lon] # North, West, South, East

    if bounding_box:
        print(f"Downloading data for bounding box: {bounding_box}")
        download_data(args.year, args.month, args.day, args.time, bounding_box, args.format, args.variable, args.product_type)
        print("Download complete.")
    else:
        print("Could not determine bounding box for the specified location.")

if __name__ == '__main__':
    main()
