import os
import json
import csv
import sys

def consolidate_gazetteer(start_path, output_csv):
    """
    Traverses a directory structure of geographic metadata files and consolidates
    them into a single CSV file.

    The directory structure is expected to represent a hierarchy, e.g.,
    .../country/region/locality/_metadata.json

    Args:
        start_path (str): The root directory to start traversal from.
        output_csv (str): The path to the output CSV file.
    """
    headers = [
        'country', 'region', 'sub_region', 'locality_level_1', 'locality_level_2',
        'locality_level_3', 'nombre_oficial', 'geoname_id', 'iso_3166_2',
        'fcode', 'poblacion', 'lat', 'lon', 'fuente_oficial'
    ]

    # Use a temporary file to avoid issues with large datasets
    temp_output_file = output_csv + ".tmp"

    try:
        with open(temp_output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

            for root, dirs, files in os.walk(start_path):
                for file in files:
                    if file == '_metadata.json':
                        filepath = os.path.join(root, file)
                        try:
                            with open(filepath, 'r', encoding='utf-8') as f:
                                data = json.load(f)

                            # Extract hierarchy from path
                            relative_path = os.path.relpath(root, start_path)
                            path_parts = relative_path.split(os.sep)

                            row = {
                                'country': path_parts[0] if len(path_parts) > 0 else '',
                                'region': path_parts[1] if len(path_parts) > 1 else '',
                                'sub_region': path_parts[2] if len(path_parts) > 2 else '',
                                'locality_level_1': path_parts[3] if len(path_parts) > 3 else '',
                                'locality_level_2': path_parts[4] if len(path_parts) > 4 else '',
                                'locality_level_3': path_parts[5] if len(path_parts) > 5 else '',
                                'nombre_oficial': data.get('nombre_oficial'),
                                'geoname_id': data.get('geoname_id'),
                                'iso_3166_2': data.get('codigos_geograficos', {}).get('iso_3166_2'),
                                'fcode': data.get('codigos_geograficos', {}).get('fcode'),
                                'poblacion': data.get('poblacion'),
                                'lat': data.get('centroide', {}).get('lat'),
                                'lon': data.get('centroide', {}).get('lon'),
                                'fuente_oficial': data.get('fuente_oficial')
                            }
                            writer.writerow(row)
                        except json.JSONDecodeError:
                            print(f"Warning: Could not decode JSON from {filepath}", file=sys.stderr)
                        except Exception as e:
                            print(f"Warning: Error processing file {filepath}: {e}", file=sys.stderr)

        # If successful, rename the temporary file to the final name
        os.rename(temp_output_file, output_csv)
        print(f"Successfully created consolidated gazetteer at {output_csv}")

    except Exception as e:
        print(f"An error occurred during CSV writing: {e}", file=sys.stderr)
        # Clean up the temporary file if it exists
        if os.path.exists(temp_output_file):
            os.remove(temp_output_file)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python consolidate_gazetteer.py <start_directory> <output_csv_path>")
        sys.exit(1)

    start_directory = sys.argv[1]
    output_file = sys.argv[2]

    consolidate_gazetteer(start_directory, output_file)
