import pytest
from com.solution.invoice import Invoice


@pytest.fixture(scope="module")
def create_invoice():
    invoice = Invoice(["abc"])
    return invoice


def test_check_input(create_invoice):
    invoice = create_invoice
    assert invoice.check() == False

