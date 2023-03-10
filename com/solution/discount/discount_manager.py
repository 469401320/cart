from typing import Dict
from typing import List
from com.solution.solutionlog import logger
from com.solution.discount.discount import Discount
from com.solution.data import Data


class DiscountManager:

    def __init__(self):
        self.discounts = dict()
        self.total_off = 0.0

    def add(self, dis: Discount):
        """add a discount rule.

                    Args:
                        dis: discount rule

                    Returns:

                    Raises:
                    Exception:
        """
        if dis.get_desc() in self.discounts:
            logger.warn("update discount %s", dis.get_desc())
        self.discounts[dis.get_desc()] = dis

    def delete_discount(self, dis_name: str):
        """delete a discount rule.

                            Args:
                                dis_name: discount rule name

                            Returns:

                            Raises:
                            Exception:
        """
        if len(self.discounts) > 0 and dis_name not in self.discounts:
            logger.warn("no discount %s", dis_name)
        del self.discounts[dis_name]

    def before_calc(self):
        """do init job before iterating products.

            Args:

            Returns:


            Raises:
            Exception:
        """
        for item_discount in self.discounts.values():
            item_discount.before_calc()
        return

    def calc(self, product: str, product_info: Data):
        """calc during iterating products.

            Args:
                product: product name
                product_info: products prices and rates

            Returns:

            Raises:
            Exception:
        """
        for item_discount in self.discounts.values():
            item_discount.calc(product, product_info)
        return

    def after_calc(self, products: List[str], product_info: Data) -> float:
        """get discount with iterating data.

            Args:
                products: products name
                product_info: products prices and rates

            Returns:
                discount

            Raises:
            Exception:
        """
        self.total_off = 0.0
        for item_discount in self.discounts.values():
            self.total_off += item_discount.after_calc(products, product_info)
        return self.total_off

    def total_discount(self) -> float:
        """delete a discount rule.

                                    Args:


                                    Returns:
                                        total_discount of all products

                                    Raises:
                                    Exception:
         """

        return self.total_off

    def discount_print(self, products: List[str], product_info: Data) -> None:
        """print discount.

            Args:

            Returns:
            None

            Raises:
            Exception:
        """
        discounts_info = []
        has_discount = False
        for item_discount in self.discounts.values():
            info = item_discount.get_print_str(products, product_info)
            discounts_info.append(info)
            if len(info) > 0:
                has_discount = True
        if has_discount:
            print("Discounts:")
            for item in discounts_info:
                if len(item) > 0:
                    print("       " + item)
