import requests
import json
import os
import unicodedata
import re

# A free GeoNames username is required.
GEONAMES_USERNAME = "jfcarrb"
BASE_URL = "http://api.geonames.org/childrenJSON"
BASE_PATH = "base_de_conocimiento/paises"

def normalize_name(name):
    """Normalizes a string to be a safe directory name."""
    nfkd_form = unicodedata.normalize('NFKD', name)
    ascii_name = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    safe_name = re.sub(r'[\s-]+', '_', ascii_name)
    safe_name = re.sub(r'[^\w_]', '', safe_name)
    return safe_name.lower()

def get_children(geoname_id):
    """Fetches the administrative children of a given geonameId."""
    params = {'geonameId': geoname_id, 'username': GEONAMES_USERNAME}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if 'status' in data:
            print(f"API Error for geonameId {geoname_id}: {data['status']['message']}")
            return None
        return data.get('geonames', [])
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error for geonameId {geoname_id}: {e}")
        return None

def process_division(geoname_id, parent_path):
    """Recursively processes a geographical division."""
    children = get_children(geoname_id)
    if not children:
        return

    for child in children:
        feature_code = child.get('fcode', '')
        if not feature_code.startswith(('ADM', 'PPL')):
            continue

        official_name = child.get('name', 'unknown')
        if official_name == 'Castille and León':
            official_name = 'Castilla y León'

        normalized = normalize_name(official_name)


        current_path = os.path.join(parent_path, normalized)
        print(f"Creating: {current_path}")
        os.makedirs(current_path, exist_ok=True)

        admin_codes = child.get('adminCodes1', {})
        iso_code = admin_codes.get('ISO3166_2', '')

        metadata = {
            "nombre_oficial": official_name,
            "geoname_id": child.get('geonameId'),
            "codigos_geograficos": {"iso_3166_2": iso_code, "fcode": feature_code},
            "poblacion": child.get('population'),
            "centroide": {"lat": child.get('lat'), "lon": child.get('lng')},
            "fuente_oficial": f"http://www.geonames.org/{child.get('geonameId')}"
        }

        metadata_path = os.path.join(current_path, '_metadata.json')
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        if feature_code.startswith('ADM'):
            process_division(child['geonameId'], current_path)

def main():
    """Main function to start the scaffolding process."""
    # geonameId for United Kingdom is 2635167
    target_geoname_id = 2635167
    target_country_name = "United Kingdom"

    country_name_normalized = normalize_name(target_country_name)
    country_path = os.path.join(BASE_PATH, country_name_normalized)

    print(f"Starting Cartographer for {target_country_name}...")
    process_division(target_geoname_id, country_path)
    print(f"Cartographer execution finished for {target_country_name}.")

if __name__ == "__main__":
    main()
