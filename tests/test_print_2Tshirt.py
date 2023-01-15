import pytest
from com.solution.invoice import Invoice


@pytest.fixture(scope="module")
def create_invoice():
    invoice = Invoice(["T-shirt", "T-shirt"])
    invoice.calc_total()
    return invoice


def test_check_input1(create_invoice):
    invoice = create_invoice
    assert invoice.check() == True

def test_check_subtotal(create_invoice):
    invoice = create_invoice
    assert int(100 * invoice.subtotal) == 6198


def test_check_shipping(create_invoice):
    invoice = create_invoice
    assert int(invoice.shipping) == 8


def test_check_vat(create_invoice):
    invoice = create_invoice
    assert int(1000 * invoice.vat) == 8677

def test_check_total_discount(create_invoice):
    invoice = create_invoice
    assert int(invoice.discount_manager.total_discount()) == 8


