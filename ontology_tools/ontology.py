from typing import Any

import requests


def fetch_ontology_details(ontology_id: str) -> dict[str, Any] | None:
    """
    Fetches details for a given ontology from the Ontology Lookup Service.

    Args:
       ontology_id (str): The ID of the ontology to fetch. e.g. 'efo'

    Returns:
       str | None:  A dictionary containing the ontology details if found, otherwise None.
    """

    base_url = "https://www.ebi.ac.uk/ols/api/"
    endpoint = f"ontologies/{ontology_id}"
    response = requests.get(base_url + endpoint)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"Ontology ID '{ontology_id}' not found.")
    else:
        print("Failed to fetch data from OLS API.")
    return None


def print_ontology_details(details: dict[str, Any]) -> None:
    """
    Prints the details of an ontology in a human-readable format.

    Args:
        details (dict[str, Any]): A dictionary containing the ontology details.

    Raises:
        ValueError: If 'details' is not a dictionary.

    Returns:
        None
    """

    # Check if 'details' is a valid dictionary first:
    if not isinstance(details, dict):
        raise ValueError("Invalid data format. Expected a dictionary.")

    # Pull desired details from the response:
    title = details.get('config', {}).get('title', 'N/A')
    description = details.get('config', {}).get('description', 'N/A')
    number_of_terms = details.get('numberOfTerms', 'N/A')
    status = details.get('status', 'N/A')

    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Number of Terms: {number_of_terms}")
    print(f"Status: {status}")
