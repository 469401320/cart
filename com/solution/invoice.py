from dataclasses import dataclass, field
from typing import List
from com.solution.data import Data
from com.solution.discount.discount_manager import DiscountManager
from com.solution.discount.shoe_discount import ShoeDiscount
from com.solution.discount.jacket_discount import JacketDiscount
from com.solution.discount.shipping_discount import ShippingDiscount
import math

from com.solution.solutionlog import logger


@dataclass
class Invoice:
    products: List[str]
    product_info: Data = field(default_factory=Data)
    subtotal: float = field(default=0.0)
    shipping: float = field(default=0.0)
    vat: float = field(default=0.0)
    total: float = field(default=0.0)
    shoe_off: float = field(default=0.0)
    jacket_off: float = field(default=0.0)
    shipping_off: float = field(default=0.0)
    discount_manager: DiscountManager = field(default_factory=DiscountManager)

    def __post_init__(self):
        shoe_discount = ShoeDiscount()
        self.discount_manager.add(shoe_discount)
        jacket_discount = JacketDiscount()
        self.discount_manager.add(jacket_discount)
        shipping_discount = ShippingDiscount()
        self.discount_manager.add(shipping_discount)

    def check(self) -> bool:
        """check user input

            check input product is valid and country is valid

            Args:


            Returns:

            Return True if chess pass, otherwise False.

            Raises:

            """
        if self.product_info.items is None or self.product_info.rates is None:
            return False
        for i in self.products:
            try:
                if i not in self.product_info.items:
                    return False
                elif self.product_info.items[i]['shipped_from'] not in self.product_info.rates:
                    return False
            except Exception as err:
                logger.error(err)
        return True

    def calc_total(self) -> float:
        """calculate total cost of cart.

            Args:

            Returns:
            total cost of cart

            Raises:
            Exception: An error occurred accessing json.
            """
        self.subtotal = 0.0
        self.total = 0.0
        self.shipping = 0.0
        self.vat = 0.0

        shoe_cost = 0.0

        try:
            for product in self.products:
                self.subtotal += self.product_info.items[product]['item_price']
                country = self.product_info.items[product]['shipped_from']
                self.shipping += math.ceil(self.product_info.items[product]['Weight'] * 10) * self.product_info.rates[country]

        except Exception as err:
            logger.error(err)
        self.vat = self.subtotal * 0.14

        self.total = self.subtotal + self.shipping + self.vat - self.discount_manager.total_discount(self.products, self.product_info)

        logger.info("total %f, subtotal %f, shipping %f, vat %f",
                    self.total, self.subtotal, self.shipping, self.vat)

        return self.total

    def invoice_print(self) -> None:
        """print invoice.

            Args:

            Returns:
            None

            Raises:
            Exception:
        """
        print(f"\r\nSubtotal: ${self.subtotal:g}")
        print(f"Shipping: ${self.shipping:g}")
        print(f"VAT: ${self.vat:g}")
        self.discount_manager.discount_print(self.products, self.product_info)
        print(f"Total: ${self.total:g}")
