from typing import List
from com.solution.data import Data
from com.solution.solutionlog import logger
from com.solution.discount.discount import Discount


class JacketDiscount(Discount):
    def get_desc(self) -> str:
        return "50% off jacket"

    def get_discount(self, products: List[str], product_info: Data) -> float:
        two_top_num = 0
        jacket_num = 0
        jacket_off = 0.0
        try:
            for product in products:
                if product == "T-shirt" or product == "Blouse":
                    two_top_num += 1
                if product == "Jacket":
                    jacket_num += 1
        except Exception as err:
            logger.error(err)
        if "Jacket" in product_info.items:
            try:
                jacket_off = product_info.items["Jacket"]['item_price'] * min(jacket_num, int(two_top_num / 2)) * 0.5
            except Exception as err:
                logger.error(err)
        return jacket_off

    def get_print_str(self, products: List[str], product_info: Data) -> str:
        discount = self.get_discount(products, product_info)
        if discount > 0:
            return self.get_desc() + self.get_sep() + str(f"{discount:g}")
        else:
            return ""
