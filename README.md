
# Time Zone and Address Fetcher

This Python script fetches time zones and addresses for given geographical coordinates using the Google Maps API. It reads coordinates from an Excel file, processes them, and outputs the results in another Excel file.

## Features

- Reads coordinates (latitude and longitude) from an Excel file.
- Uses Google Maps API to fetch corresponding time zones and addresses.
- Outputs results in an Excel file with additional columns for address and time zone.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a basic understanding of Python programming.
- You have a Google Maps API key. [Learn how to get one here](https://developers.google.com/maps/documentation/javascript/get-api-key).

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/hyunjekim2000/GeoTimeZoneFetcher.git
   ```
2. Install the required Python packages:
   ```
   pip install pandas googlemaps openpyxl
   ```

## Configuration

1. Open the script in a text editor.
2. Replace `YOUR-API-KEY` in the script with your actual Google Maps API key.

## Usage

To use this script, follow these steps:

1. Prepare your input Excel file with two columns: `Latitude` and `Longitude`.
2. Run the script from your command line:
   ```
   python script_name.py <input_file.xlsx> <output_file.xlsx>
   ```
   Replace `script_name.py` with the name of your script, `<input_file.xlsx>` with the name of your input file, and `<output_file.xlsx>` with the desired name for your output file.


## Contact

If you want to contact me, you can reach me at [k3h0j8@vt.edu].

## License

This project is free to use. 
