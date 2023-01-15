from typing import List
from com.solution.data import Data
from com.solution.solutionlog import logger
from com.solution.discount.discount import Discount


class JacketDiscount(Discount):
    def __init__(self):
        self.two_top_num = 0
        self.jacket_num = 0

    def get_desc(self) -> str:
        return "50% off jacket"

    def get_discount(self, products: List[str], product_info: Data) -> float:
        return self.off

    def before_calc(self):
        self.two_top_num = 0
        self.jacket_num = 0
        self.off = 0.0
        return

    def calc(self, product: str, product_info: Data):
        if product == "T-shirt" or product == "Blouse":
            self.two_top_num += 1
        if product == "Jacket":
            self.jacket_num += 1
        return

    def after_calc(self, products: List[str], product_info: Data) -> float:
        if "Jacket" in product_info.items:
            try:
                self.off = product_info.items["Jacket"]['item_price'] * min(self.jacket_num,
                                                                                   int(self.two_top_num / 2)) * 0.5
            except Exception as err:
                logger.error(err)
        return self.off

    def get_print_str(self, products: List[str], product_info: Data) -> str:
        discount = self.off
        if discount > 0:
            return self.get_desc() + self.get_sep() + str(f"{discount:g}")
        else:
            return ""
