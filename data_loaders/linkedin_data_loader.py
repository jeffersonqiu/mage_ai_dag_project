import io
import os
import pandas as pd
import requests
from dotenv import load_dotenv

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Load environment variables from .env file
load_dotenv()

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = "https://linkedin-data-api.p.rapidapi.com/search-jobs-v2"

    querystring = {
        "keywords": "data scientist",
        "locationId": "102454443",
        "datePosted": "pastMonth",
        "jobType": "fullTime",
        "sort": "mostRelevant",
        "offset": 0,  # Start with offset 0
        "limit": 50  # Assuming the API returns 50 items per page
    }

    # Retrieve API key from environment variable
    api_key = os.getenv('RAPIDAPI_KEY')
    if not api_key:
        raise Exception("API key not found. Please set the 'RAPIDAPI_KEY' environment variable.")

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
    }

    all_results = []
    offset = 0
    limit = 50
    count = 0

    while count <= 4:
        querystring.update({'offset': offset, 'limit': limit})
        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

        data = response.json()
        results = data.get('data', [])
        all_results.extend(results)

        # Check if we have fetched all results
        if len(results) < limit:
            break

        # Update the offset for the next iteration
        offset += limit
        count += 1

    return all_results

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
