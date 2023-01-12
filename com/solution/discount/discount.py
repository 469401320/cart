from typing import List
from com.solution.data import Data


class Discount:
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

    def get_discount(self, products: List[str], product_info: Data) -> float:
        """get description string for a discount rule

           Args:
               products: products name
               product_info: products prices and rates


           Returns:
               discount of a discount rule

           Raises:
           Exception:
        """
        return 0.0

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
