from typing import List
from com.solution.data import Data


class Discount:
    def __init__(self):
        self.off = 0.0
    def get_sep(self) -> str:
        """get separator string.

           Args:

           Returns:
               ": -$"

           Raises:
           Exception:
        """
        return ": -$"

    def get_desc(self) -> str:
        """get description string for a discount rule

           Args:

           Returns:
               description string

           Raises:
           Exception:
        """
        return ""

    def get_discount(self) -> float:
        """get description string for a discount rule

           Args:
               products: products name
               product_info: products prices and rates


           Returns:
               discount of a discount rule

           Raises:
           Exception:
        """
        return self.off

    def get_print_str(self, products: List[str], product_info: Data) -> str:
        """print discount details.

            Args:
                products: products name
                product_info: products prices and rates

            Returns:
            discount details string

            Raises:
            Exception:
        """
        return ""

    def before_calc(self):
        """do init job before iterating products.

            Args:

            Returns:


            Raises:
            Exception:
        """
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
        return 0.0
