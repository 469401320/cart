import pytest
from com.solution.invoice import Invoice
from com.solution.data import Data
import os


@pytest.fixture(scope="module")
def create_invoice():
    product_info = Data(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'item_false2.json')),
                        os.path.abspath(
                            os.path.join(os.path.abspath(os.path.dirname(__file__)), 'shipping_false.json')))
    invoice = Invoice(["Blouse"], product_info)
    return invoice


def test_check_input(create_invoice):
    invoice = create_invoice
    assert invoice.check() == False



