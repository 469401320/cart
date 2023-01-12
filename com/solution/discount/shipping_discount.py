from typing import List
from com.solution.data import Data
from com.solution.solutionlog import logger
from com.solution.discount.discount import Discount
import math

class ShippingDiscount(Discount):
    def get_desc(self) -> str:
        return "$10 of shipping"

    def get_discount(self, products: List[str], product_info: Data) -> float:
        shipping = 0.0
        shipping_off = 0.0
        try:
            for product in products:
                country = product_info.items[product]['shipped_from']
                shipping += math.ceil(product_info.items[product]['Weight'] * 10) * product_info.rates[
                    country]
        except Exception as err:
            logger.error(err)
        if len(products) > 1:
            shipping_off = min(10, shipping)
        return shipping_off

    def get_print_str(self, products: List[str], product_info: Data) -> str:
        discount = self.get_discount(products, product_info)
        if discount > 0:
            return self.get_desc() + self.get_sep() + str(f"{discount:g}")
        else:
            return ""
