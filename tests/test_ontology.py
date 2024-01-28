import unittest
from unittest.mock import patch

from ontology_tools.ontology import fetch_ontology_details, print_ontology_details


class TestFetchOntologyDetails(unittest.TestCase):
    @patch('ontology_tools.ontology.requests.get')
    def test_fetch_ontology_successful(self, mock_get):
        """Mocks a successful (200) response"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"id": "efo", "config": {"title": "Example Ontology"}}

        result = fetch_ontology_details("efo")
        self.assertIsNotNone(result)
        self.assertEqual(result['id'], "efo")

    @patch('ontology_tools.ontology.requests.get')
    def test_fetch_ontology_not_found(self, mock_get):
        """Mocks a response to an unsuccessful (404) request"""
        mock_get.return_value.status_code = 404

        result = fetch_ontology_details("unknown_id")
        self.assertIsNone(result)

    @patch('ontology_tools.ontology.requests.get')
    def test_fetch_ontology_server_error(self, mock_get):
        """Mocks a server error"""
        mock_get.return_value.status_code = 500

        result = fetch_ontology_details("efo")
        self.assertIsNone(result)


class TestPrintOntologyDetails(unittest.TestCase):
    @patch('builtins.print')
    def test_print_valid_ontology_details(self, mock_print):
        """Tests if valid ontology details are printed correctly"""
        details = {
            "config": {"title": "Example Ontology", "description": "A test ontology"},
            "numberOfTerms": 100,
            "status": "active"
        }
        print_ontology_details(details)
        mock_print.assert_called_with("Status: active")

    def test_print_invalid_ontology_details(self):
        """Tests if an invalid data type raises a ValueError."""
        with self.assertRaises(ValueError):
            print_ontology_details("Test String")

    @patch('builtins.print')
    def test_print_ontology_details_with_missing_fields(self, mock_print):
        """Tests if missing fields are handled by returning N/A"""
        details = {"config": {"title": "Incomplete Ontology"}}
        print_ontology_details(details)
        mock_print.assert_any_call("Description: N/A")
        mock_print.assert_any_call("Number of Terms: N/A")
        mock_print.assert_any_call("Status: N/A")
