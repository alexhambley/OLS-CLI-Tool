#!/usr/bin/env python3
import argparse
from typing import NoReturn
from ontology_tools.ontology import fetch_ontology_details, print_ontology_details


def process_ontology(ontology_id: str) -> None:
    """
    Fetches and displays details of the specified ontology.

    Args:
        ontology_id (str): The ID of the ontology.
    """
    details = fetch_ontology_details(ontology_id)
    if details:
        print_ontology_details(details)
    else:
        print("No data available or error occurred.")


def main() -> NoReturn:
    """The main function to run. Called from run_app.py. Parses CLI arguments and calls process_ontology."""

    parser = argparse.ArgumentParser(description="Fetch and display details of a specified ontology from OLS.")
    parser.add_argument("ontology_id", type=str, help="The ID of the ontology to fetch. e.g. 'efo'")
    args = parser.parse_args()

    process_ontology(args.ontology_id)


if __name__ == "__main__":
    main()
