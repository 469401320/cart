from typing import List
from com.solution.data import Data
from com.solution.solutionlog import logger
from com.solution.discount.discount import Discount


class ShoeDiscount(Discount):
    def get_desc(self) -> str:
        return "10% off shoes"

    def get_discount(self, products: List[str], product_info: Data) -> float:
        shoe_cost = 0.0
        try:
            for product in products:
                if product == "Shoes":
                    shoe_cost += product_info.items[product]['item_price']
        except Exception as err:
            logger.error(err)
        return shoe_cost * 0.1

    def get_print_str(self, products: List[str], product_info: Data) -> str:
        discount = self.get_discount(products, product_info)
        if discount > 0:
            return self.get_desc() + self.get_sep() + str(f"{discount:g}")
        else:
            return ""
