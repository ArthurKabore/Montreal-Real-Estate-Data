### Montreal Real Estate Data Scrapper

This Python script reads data about condos (*only condos for now*) from a CSV file and outputs it in a user-friendly format. It's designed to help real estate agents, property managers, and other professionals who need to analyze condo data quickly and efficiently.

## Installation

To use this script, you'll need Python 3 <I used version 3.11.2> installed on your computer and PATH. You can download it from the official website at [Python Download](https://www.python.org/downloads/)

You'll also need to install the following Python packages:

- pandas

- numpy

- snowflake

- spark

You can install these packages using pip, the Python package installer. Simply open a terminal or command prompt and type:
pip install pandas numpy

## Usage

Full usage depends on the services you are in usage of and the purpose of your usage of the script.

Run the scripts in the following order:

1. ingest_webscraped_data.py (*This process may take several hours as it needs to go through more than 4 000 pages of the website!*)
2. cleanup_ingested_data.py (*Clean up the ingested data into a format that can be easily be loeaded to a database*)
3. populate_data_snowflake (*This step is optional / Feel free to use your new CSV data for anything you want*)

<If you wish to use this to full capacity please contact me for detailed information otherwise the following should suffice for whatever needs you have of this.>

## Contributing

If you find a bug or have a suggestion for improving this script, please feel free to connect with me through here or LinkedIn. I welcome contributions from the community and appreciate your feedback.

## License

This script is released under the MIT License. You're free to use it, modify it, and distribute it as you wish, as long as you include the original license in your distribution. See the LICENSE file for more details.