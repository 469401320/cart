import pytest
from com.solution.invoice import Invoice


@pytest.fixture(scope="module")
def create_invoice():
    invoice = Invoice(["T-shirt", "Pants", "Blouse", "Shoes", "Jacket"])
    invoice.calc_total()
    return invoice


def test_check_input1(create_invoice):
    invoice = create_invoice
    assert invoice.check() == True

def test_check_total(create_invoice):
    invoice = create_invoice
    assert int(100 * invoice.total) == 43312

def test_check_subtotal(create_invoice):
    invoice = create_invoice
    assert int(100 * invoice.subtotal) == 38695


def test_check_shipping(create_invoice):
    invoice = create_invoice
    assert int(invoice.shipping) == 110


def test_check_vat(create_invoice):
    invoice = create_invoice
    assert int(1000 * invoice.vat) == 54173


def test_check_total_discount(create_invoice):
    invoice = create_invoice
    assert int(1000 * invoice.discount_manager.total_discount()) == 117994
