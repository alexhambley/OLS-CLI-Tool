import unittest
from unittest.mock import patch

from ontology_tools.cli import process_ontology


class TestProcessOntology(unittest.TestCase):
    @patch('ontology_tools.cli.fetch_ontology_details')
    @patch('ontology_tools.cli.print_ontology_details')
    def test_process_ontology_with_valid_id(self, mock_print, mock_fetch):
        """Tests the process_ontology function with a valid ID."""
        mock_fetch.return_value = {
            'config': {
                'title': 'Experimental Factor Ontology',
                'description': 'The Experimental Factor Ontology (EFO) provides a systematic description of many '
                               'experimental variables available in EBI databases, and for external projects such as '
                               'the NHGRI GWAS catalogue. It combines parts of several biological ontologies, such as '
                               'anatomy, disease and chemical compounds. The scope of EFO is to support the '
                               'annotation, analysis and visualization of data handled by many groups at the EBI and '
                               'as the core ontology for OpenTargets.org'
            },
            'numberOfTerms': 51935,
            'status': 'LOADED'
        }

        process_ontology('efo')

        mock_fetch.assert_called_once_with('efo')
        mock_print.assert_called_once()

    @patch('ontology_tools.cli.fetch_ontology_details')
    @patch('ontology_tools.cli.print_ontology_details')
    def test_process_ontology_with_invalid_id(self, mock_print, mock_fetch):
        """Tests the process_ontology function with an invalid ID."""
        mock_fetch.return_value = None
        process_ontology('invalid_id')
        mock_fetch.assert_called_once_with('invalid_id')
        mock_print.assert_not_called()
