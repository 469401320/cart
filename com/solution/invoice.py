from dataclasses import dataclass, field
from typing import List
from com.solution.data import Data
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
        self.shoe_off = 0.0
        self.jacket_off = 0.0
        self.shipping_off = 0.0

        shoe_cost = 0.0
        two_top_num = 0
        jacket_num = 0
        try:
            for product in self.products:
                self.subtotal += self.product_info.items[product]['item_price']
                country = self.product_info.items[product]['shipped_from']
                self.shipping += math.ceil(self.product_info.items[product]['Weight'] * 10) * self.product_info.rates[country]
                if product == "Shoes":
                    shoe_cost += self.product_info.items[product]['item_price']
                if product == "T-shirt" or product == "Blouse":
                    two_top_num += 1
                if product == "Jacket":
                    jacket_num += 1
        except Exception as err:
            logger.error(err)
        self.vat = self.subtotal * 0.14
        self.shoe_off = shoe_cost * 0.1
        if "Jacket" in self.product_info.items:
            try:
                self.jacket_off = self.product_info.items["Jacket"]['item_price'] * min(jacket_num, int(two_top_num / 2)) * 0.5
            except Exception as err:
                logger.error(err)
        if len(self.products) > 1:
            self.shipping_off = min(10, self.shipping)
        self.total = self.subtotal + self.shipping + self.vat - self.shoe_off - self.jacket_off - self.shipping_off
        logger.info("total %f, subtotal %f, shipping %f, vat %f, shoe off %f, jacket_off %f, shipping_off %f",
                    self.total, self.subtotal, self.shipping, self.vat, self.shoe_off, self.jacket_off,
                    self.shipping_off)

        return self.total

    def invoice_print(self) -> None:
        """print invoice.

            Args:

            Returns:
            None

            Raises:
            Exception: An error occurred accessing json.
        """
        print(f"\r\nSubtotal: ${self.subtotal:g}")
        print(f"Shipping: ${self.shipping:g}")
        print(f"VAT: ${self.vat:g}")
        if self.shoe_off > 0 or self.jacket_off > 0 or self.shipping_off > 0:
            print("Discounts:")
        if self.shoe_off > 0:
            print(f"       10% off shoes: -${self.shoe_off:g}")
        if self.jacket_off > 0:
            print(f"       50% off jacket: -${self.jacket_off:g}")
        if self.shipping_off > 0:
            print(f"       $10 of shipping: -${self.shipping_off:g}")
        print(f"Total: ${self.total:g}")
