
import pytest

from lexnlp import is_stanford_enabled
from lexnlp.tests import lexnlp_tests


@pytest.mark.skipif(not is_stanford_enabled(), reason="Stanford is disabled.")
def test_stanford_name_example_in():
    from lexnlp.extract.en.entities.stanford_ner import get_persons
    lexnlp_tests.test_extraction_func_on_test_data(get_persons,
                                                   expected_data_converter=lambda row: row[0],
                                                   test_only_expected_in=True)


@pytest.mark.skipif(not is_stanford_enabled(), reason="Stanford is disabled.")
def test_stanford_org_example_in():
    from lexnlp.extract.en.entities.stanford_ner import get_organizations
    lexnlp_tests.test_extraction_func_on_test_data(get_organizations,
                                                   expected_data_converter=lambda row: row[0],
                                                   test_only_expected_in=True)


@pytest.mark.skipif(not is_stanford_enabled(), reason="Stanford is disabled.")
def test_stanford_locations():
    from lexnlp.extract.en.entities.stanford_ner import get_locations
    lexnlp_tests.test_extraction_func_on_test_data(get_locations)
