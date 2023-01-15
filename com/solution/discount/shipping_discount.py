from typing import List
from com.solution.data import Data
from com.solution.solutionlog import logger
from com.solution.discount.discount import Discount
import math


class ShippingDiscount(Discount):
    def __init__(self):
        self.shipping = 0.0

    def get_desc(self) -> str:
        return "$10 of shipping"

    def get_discount(self, products: List[str], product_info: Data) -> float:
        return self.off

    def get_print_str(self, products: List[str], product_info: Data) -> str:
        discount = self.off
        if discount > 0:
            return self.get_desc() + self.get_sep() + str(f"{discount:g}")
        else:
            return ""

    def before_calc(self):
        self.shipping = 0.0
        self.off = 0.0
        return

    def calc(self, product: str, product_info: Data):
        country = product_info.items[product]['shipped_from']
        self.shipping += math.ceil(product_info.items[product]['Weight'] * 10) * product_info.rates[
            country]
        return

    def after_calc(self, products: List[str], product_info: Data) -> float:
        if len(products) > 1:
            self.off = min(10, self.shipping)
        return self.off
