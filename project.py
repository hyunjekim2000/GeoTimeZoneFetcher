import pandas as pd
import googlemaps
import sys
import concurrent.futures

def convert_to_readable_timezone(timezone_id):
    """Convert Google Maps API timezone ID to a more readable format."""
    mapping = {
        "America/New_York": "Eastern Time Zone",
        "America/Chicago": "Central Time Zone",
        "America/Denver": "Mountain Time Zone",
        "America/Los_Angeles": "Pacific Time Zone",
        "America/Phoenix": "Mountain Standard Time Zone",
        "America/Indiana/Indianapolis": "Eastern Time Zone",
        "America/Anchorage": "Alaska Time Zone",
        "America/Honolulu": "Hawaii-Aleutian Time Zone",
        # Add more mappings as required
    }
    return mapping.get(timezone_id, timezone_id)  # Return the original ID if not found in mapping

def fetch_timezone_and_address(data):
    lat, lng, gmaps_client = data
    try:
        # Fetch the time zone
        timezone_result = gmaps_client.timezone((lat, lng))
        timezone = convert_to_readable_timezone(timezone_result['timeZoneId']) if timezone_result else None

        # Perform reverse geocoding to get the address
        reverse_geocode_result = gmaps_client.reverse_geocode((lat, lng))
        address = reverse_geocode_result[0]['formatted_address'] if reverse_geocode_result else None

        return address, timezone

    except Exception as e:
        print(f"Error processing coordinates ({lat},{lng}): {str(e)}")
        return None, None

def process_excel(input_file, output_file, api_key, max_workers=10):
    # Initialize Google Maps client
    gmaps = googlemaps.Client(key=api_key)

    # Load the .xlsx file into a DataFrame using openpyxl engine
    print("Reading Excel file...")
    df = pd.read_excel(input_file, engine='openpyxl')

    # Prepare data for multi-threading
    data_list = [(row['Latitude'], row['Longitude'], gmaps) for _, row in df.iterrows()]

    # Fetch the address and time zone for each row using multi-threading
    print("Fetching time zones and addresses for coordinates...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(fetch_timezone_and_address, data_list))

    df['Address'], df['Time Zone'] = zip(*results)

    # Save the updated DataFrame to the output .xlsx file
    print("Saving results to output file...")
    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <input_file.xlsx> <output_file.xlsx>")
        sys.exit(1)

    API_KEY = 'YOUR-API-KEY'
    if API_KEY == 'YOUR-API-KEY':
        print("Error: Replace 'YOUR-API-KEY' with your actual Google Maps API key.")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_excel(input_file, output_file, API_KEY)