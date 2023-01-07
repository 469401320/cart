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


def test_check_shoe_off(create_invoice):
    invoice = create_invoice
    assert int(1000 * invoice.shoe_off) == 0


def test_check_jacket_off(create_invoice):
    invoice = create_invoice
    assert int(1000 * invoice.jacket_off) == 0


def test_check_shipping_off(create_invoice):
    invoice = create_invoice
    invoice.invoice_print()
    assert int(invoice.shipping_off) == 8
