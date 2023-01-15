from typing import List
from com.solution.data import Data
from com.solution.solutionlog import logger
from com.solution.discount.discount import Discount


class ShoeDiscount(Discount):
    def __init__(self):
        self.shoe_cost = 0.0

    def get_desc(self) -> str:
        return "10% off shoes"

    def get_discount(self, products: List[str], product_info: Data) -> float:
        return self.off

    def get_print_str(self, products: List[str], product_info: Data) -> str:
        discount = self.get_discount(products, product_info)
        if discount > 0:
            return self.get_desc() + self.get_sep() + str(f"{discount:g}")
        else:
            return ""

    def before_calc(self):
        self.shoe_cost = 0.0
        self.off = 0.0
        return

    def calc(self, product: str, product_info: Data):
        if product == "Shoes":
            self.shoe_cost += product_info.items[product]['item_price']
        return

    def after_calc(self, products: List[str], product_info: Data) -> float:
        self.off = self.shoe_cost * 0.1
        return self.off
